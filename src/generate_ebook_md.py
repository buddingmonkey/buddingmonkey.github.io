#!/usr/bin/env python3
"""
Used to read the metadata of each ebook in the ebooks directory and generate
the appropiate markdown
"""
import os
import re
import xml.etree.ElementTree as ET
from liquid import Liquid
from urllib.parse import quote

__license__ = "MIT"

rootdir = 'ebooks'
extensions = ('.opf')

def main():
    print(os.getcwd())
    books = []

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.startswith('.'):
                continue
            ext = os.path.splitext(file)[-1].lower()
            if ext in extensions:
                title = get_book_title("ebooks/" + file)
                pdfurl = "ebooks/" + quote(os.path.basename(file) + ".pdf", safe='')
                epuburl = "ebooks/" + quote(os.path.basename(file) + ".epub", safe='')
                imageurl = "ebooks/" + quote(os.path.basename(file) + ".jpg", safe='')
                books.append({
                    "title": title,
                    "image": imageurl,
                    "pdfurl": pdfurl,
                    "epuburl": epuburl
                    })
    render_md(books)

def get_book_title(xml_path):
    print("reading: " +xml_path)
    tree = ET.parse(xml_path)
    root = tree.getroot()
    return root.findall(".//{http://purl.org/dc/elements/1.1/}title")[0].text


def render_md(books):
    # load template from a file
    liq = Liquid('template/README.template.md', liquid_from_file=True)
    md = liq.render(books = books)

    with open("README.md", 'w') as f:
        f.write(md)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()