from subprocess import run
from pathlib import Path
import os

TEMPDIR = Path("temp")

def doc_to_docx(filepath, outdir=TEMPDIR):
    "Given a path to a .doc file, creates a .docx file and returns the path to it."
    command = f"soffice --headless --convert-to docx --outdir {outdir} {filepath}"
    run(command, shell=True, check=True)
    outpath = (outdir / Path(filepath).name).with_suffix('.docx')
    return outpath
    
def docx_to_html(filepath, outdir=TEMPDIR):
    "Given a path to a .docx file, creates a .html file and returns the path to it."
    filepath = Path(filepath).resolve()
    outdir = Path(outdir)
    outpath = (outdir / filepath.name).with_suffix('.html')
    here = os.getcwd()
    os.chdir(outdir)
    command = f"pandoc --extract-media . {filepath} -o {outpath.name}"
    run(command, shell=True, check=True)
    os.chdir(here)
    return outpath

