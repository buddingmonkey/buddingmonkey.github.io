{% for book in books %}
### {{book.title}} 
![Image]({{book.image}})

**Download:** [EPUB]({{book.epuburl}}) [PDF]({{book.pdfurl}})

---

{% else %}
No content found. Place PDFs EPUBs in ebooks folder.
{% endfor %}