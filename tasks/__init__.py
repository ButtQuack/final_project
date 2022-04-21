from invoke import task
from pathlib import Path
import shutil
from tqdm import tqdm

@task
def test(c):
    "Run all tests"
    import unittest
    test_suite = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(test_suite)

@task
def generate_html(c, limit=0, clean=False):
    "Generate HTML from doc files"
    from src.file_conversion import doc_to_docx, docx_to_html
    docdir = Path("data/doc")
    docxdir = Path("data/docx")
    htmldir = Path("data/html")
    if clean and htmldir.exists():
        shutil.rmtree(htmldir)
    docdir.mkdir(exist_ok=True)
    docxdir.mkdir(exist_ok=True)
    htmldir.mkdir(exist_ok=True)
    docpaths = list(docdir.glob("**/*.doc"))
    if limit:
        docpaths = docpaths[:limit]
    for docpath in tqdm(docpaths):
        docxpath = doc_to_docx(docpath, docxdir)
        html = docx_to_html(docxpath, htmldir)
        
