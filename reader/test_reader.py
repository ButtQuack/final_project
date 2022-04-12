from pathlib import Path
from reader import doc_to_docx, docx_to_html, html_to_questions
from pprint import pprint

testfile = "import/A.CED.A.4.TransformingFormulas1a.doc"
docx = doc_to_docx(testfile)
html = docx_to_html(docx)
pprint(html_to_questions(html.read_text()))

