# final_project
Isaak DeMaio

## Usage

Use Poetry to install all dependencies (`poetry install`) and then run this package from within a Poetry shell (`poetry shell`).
We use `invoke` to run tasks. Run `invoke --list` (or `inv --list`) to see available tasks.

- `inv test`: Run all the tests.

## Design

### Rationale
	The goal of my project is to create a user-enabled test for the topics of Algebra I, Geometry and Algebra 2, where users practice old New York State Regents Examination (NYSRE) questions based on the common core standards. Questions are provided as a `.doc` and have been converted to `.docx` and then finally HTML. The answers are within each document and the reference code is read as "Month/Year/Question#/Standard". This is important for filtering questions based on each standard. I think it would be beneficial for the reference line to appear with the question so educators and students get an idea of the type of question. For student-produced answers, I'd like for the rubric to be displayed as it was on the examination the question appeared. This allows educators and students to review answers and sufficiently adjust their teaching and learning. I'd like to have the questions available in other languages. I am interested in helping underrepresented ENL students have access to the NYSRE as equally as possible to their English as a first language counterparts.
