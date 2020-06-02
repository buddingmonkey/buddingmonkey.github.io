{% for book in books %}
### {{book.title}} 
![Image]({{book.image}})

Download: [EPUB]({{book.epuburl}}) [PDF]({{book.pdfurl}})

---

{% endfor %}