#!/usr/bin/env python3
"""
fix_borders.py — Corrige a ordem dos elementos de borda em documentos .docx gerados pelo docx-js.

O docx-js gera borders na ordem (top, bottom, left, right), mas o schema OpenXML
exige (top, left, bottom, right). Este script reordena automaticamente.

Uso:
    python fix_borders.py unpacked_dir/word/document.xml

Integrado no pipeline: gerar .docx → unpack → fix_borders → pack → validate
"""

import re
import sys

def fix_border_order(match):
    content = match.group(1)
    top = re.search(r'<w:top[^/]*/>', content)
    left = re.search(r'<w:left[^/]*/>', content)
    bottom = re.search(r'<w:bottom[^/]*/>', content)
    right = re.search(r'<w:right[^/]*/>', content)

    result = '<w:pBdr>\n'
    for elem in [top, left, bottom, right]:
        if elem:
            result += '          ' + elem.group(0) + '\n'
    result += '        </w:pBdr>'
    return result

def main():
    if len(sys.argv) < 2:
        print("Uso: python fix_borders.py <arquivo.xml>")
        sys.exit(1)

    filepath = sys.argv[1]
    with open(filepath, 'r', encoding='utf-8') as f:
        xml = f.read()

    original = xml
    xml = re.sub(r'<w:pBdr>(.*?)</w:pBdr>', fix_border_order, xml, flags=re.DOTALL)

    if xml != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(xml)
        print(f"Borders reordenados em {filepath}")
    else:
        print(f"Nenhuma correção necessária em {filepath}")

if __name__ == '__main__':
    main()
