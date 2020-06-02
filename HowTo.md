# How to edit the website

## Prerequesites

- Python 3 (make sure LiquidPy is installed)
- Calbire (https://calibre-ebook.com/download)

## Adding a book

1. Add your PDF into a Calibre library (https://manual.calibre-ebook.com/gui.html#add-books)
2. Convert the book into EPUB Format (https://manual.calibre-ebook.com/conversion.html)
3. Select all the books you wish to add. `Right Click --> Save To Disk --> Save to disk in a single directory`. Save the books to the `ebooks` directory in the repository

## Building the site

Run the script `generate_ebook_md.py` in the /src folder

## Updating the site

Commit and push the updated files to the master branch and the site should automatically upate in a few minutes.

## More info

- The site uses a template in `template\README.template.md` to generate. Edit that template to change the look of the site
- You can edit the `README.md` manually if you don't want to mess with Python