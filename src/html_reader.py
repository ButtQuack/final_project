from pathlib import Path
from subprocess import run
import os
from bs4 import BeautifulSoup as BS

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

def is_new_question(tag, tokens=None):
    if tokens == None:
        tokens = tag.get_text().split(' ')
    return tag.name == 'p' and starts_with_number(tag, tokens) and not is_answer(tag, tokens)

def starts_with_number(tag, tokens=None):
    if tokens == None:
        tokens = tag.get_text().split(' ')
    return tokens and tokens[0].isdigit()

def is_answer(tag, tokens=None):
    if tokens == None:
        tokens = tag.get_text().split(' ')
    return len(tokens) >= 2 and starts_with_number(tag, tokens) and tokens[1] == "ANS:"

def is_choices(tag):
    return tag.name == "table"

def parse_choices(tag):
    choices = []
    for choice in tag.tbody.find_all('tr'):
        label, choice_text = choice.find_all('td')
        choices.append({
            "label": label.get_text(),
            "choice": str(choice_text),
        })
    return choices

def parse_question(tag):
    tokens = tag.get_text().split(' ')
    for img in tag.find_all('img'):
        del img['style']
    return {
        "index": int(tokens[0]),
        "question": str(tag),
    }

def parse_answer(tag):
    tokens = tag.get_text().split(' ')
    answer = str(tag)
    return int(tokens[0]), answer

def parse_reference(ref):
    "Parses a reference string, returning a dict. NOT DONE."
    month_names = {
        "01": "January",
        "06": "June",
        "08": "August",
    }
    course_names = {
        "ai": "Algebra I",
        "aii": "Algebra II",
        "geo": "Geometry",
    }
    month = month_names[ref[0:2]]
    year = int(ref[2:4]) + 2000
    question_number = int(ref[4:6])
    course = course_names[ref[6:]]
    
    return {
        "month": month,
        "year": year,
        "question": question_number,
        "course": course
    }

def html_to_questions(html):
    "Parses test questions from html string"
    document = BS(html, 'lxml')
    questions = {}
    question = None
    for tag in document.body.contents:
        if is_new_question(tag):
            if question:
                questions[question['index']] = question
            question = parse_question(tag)
        elif is_choices(tag):
            question["choices"] = parse_choices(tag)
        elif is_answer(tag):
            continue
            index, answer = parse_answer(tag)
            questions[index]["answer"] = answer
        else:
            question["question"] += str(tag)
    return questions
