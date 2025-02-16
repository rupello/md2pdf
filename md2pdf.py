#!/bin/env python3

# /// script
# dependencies = [
#   "markdown<3",
#   "weasyprint",
# ]
# ///

import sys
import os
from markdown import markdown
from weasyprint import HTML, CSS

def convert_md_to_pdf(md_file, pdf_file, template_file='template.html'):
    # Read markdown content
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML
    html_content = markdown(md_content)
    
    # Read HTML template
    with open(template_file, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Insert content into template
    full_html = template.replace('{{content}}', html_content)

    # Convert HTML to PDF
    HTML(string=full_html).write_pdf(pdf_file)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python md2pdf.py input.md output.pdf")
        sys.exit(1)
    
    md_file = sys.argv[1]
    pdf_file = sys.argv[2]
    template_file = os.path.join(os.path.dirname(__file__), 'template.html')
    
    try:
        convert_md_to_pdf(md_file, pdf_file, template_file)
        print(f"Successfully converted {md_file} to {pdf_file}")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
