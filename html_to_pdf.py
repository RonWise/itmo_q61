#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import weasyprint
import os

def html_to_pdf(html_file, pdf_file):
    """Конвертирует HTML файл в PDF с поддержкой русского языка"""
    
    # Создаем CSS для поддержки русского языка
    css = '''
    @page {
        size: A4;
        margin: 2cm;
        @top-center {
            content: "Анализ данных о мошеннических транзакциях";
            font-family: "Times New Roman", serif;
        }
        @bottom-center {
            content: counter(page);
            font-family: "Times New Roman", serif;
        }
    }
    
    body {
        font-family: "Times New Roman", "DejaVu Serif", serif;
        font-size: 12pt;
        line-height: 1.4;
        color: #333;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: "Times New Roman", "DejaVu Serif", serif;
        color: #2c3e50;
        margin-top: 1em;
        margin-bottom: 0.5em;
    }
    
    h1 { font-size: 18pt; }
    h2 { font-size: 16pt; }
    h3 { font-size: 14pt; }
    
    pre, code {
        font-family: "Courier New", monospace;
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 3px;
        padding: 0.5em;
        overflow-x: auto;
    }
    
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 1em 0;
    }
    
    th, td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
        font-family: "Times New Roman", "DejaVu Serif", serif;
    }
    
    th {
        background-color: #f2f2f2;
        font-weight: bold;
    }
    
    img {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 1em auto;
    }
    
    .output_png {
        text-align: center;
        margin: 1em 0;
    }
    '''
    
    # Читаем HTML файл
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Создаем HTML документ
    html_doc = weasyprint.HTML(string=html_content, encoding='utf-8')
    
    # Конвертируем в PDF
    html_doc.write_pdf(pdf_file, stylesheets=[weasyprint.CSS(string=css)])
    
    print(f"PDF файл создан: {pdf_file}")

if __name__ == "__main__":
    html_file = "eda_final_russian.html"
    pdf_file = "eda_final_russian_fixed.pdf"
    
    if os.path.exists(html_file):
        html_to_pdf(html_file, pdf_file)
    else:
        print(f"HTML файл {html_file} не найден!")
