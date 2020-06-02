#!/usr/bin/env python3
"""
Used to read the metadata of each ebook in the ebooks directory and generate
the appropiate markdown
"""
import os
import re
import sys
import xml.etree.ElementTree as ET
from liquid import Liquid
from urllib.parse import quote

__license__ = "MIT"

rootdir = 'ebooks'
extensions = ('.pdf')

def main():
    print(os.getcwd())
    books = []

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.startswith('.'):
                continue
            ext = os.path.splitext(file)[-1].lower()
            if ext in extensions:
                title = get_book_title("ebooks/" + os.path.splitext(os.path.basename(file))[0] + ".opf")
                pdfurl = "ebooks/" + quote(os.path.splitext(os.path.basename(file))[0] + ".pdf", safe='')
                epuburl = "ebooks/" + quote(os.path.splitext(os.path.basename(file))[0] + ".epub", safe='')
                imageurl = "ebooks/" + quote(os.path.splitext(os.path.basename(file))[0] + ".jpg", safe='')
                books.append({
                    "title": title,
                    "image": imageurl,
                    "pdfurl": pdfurl,
                    "epuburl": epuburl
                    })
    render_md(books)

def get_book_title(xml_path):
    print("reading: " + xml_path)
    title = ""
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        title = root.findall(".//{http://purl.org/dc/elements/1.1/}title")[0].text
    except Exception as e:
        print("WARNING Could not find .opf file -- " + str(e))
        title = os.path.basename(xml_path)
    return title


def render_md(books):
    # load template from a file
    liq = Liquid('template/README.template.md', liquid_from_file=True)
    md = liq.render(books = books)

    with open("README.md", 'w') as f:
        f.write(md)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()