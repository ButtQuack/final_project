# final_project
Isaak DeMaio

## Usage

Use Poetry to install all dependencies (`poetry install`) and then run this package from within a Poetry shell (`poetry shell`).
We use `invoke` to run tasks. Run `invoke --list` (or `inv --list`) to see available tasks.

- `inv test`: Run all the tests.

## Design

### Rationale
	The goal of my project is to create a user-enabled test for Algebra I standard A.CED.A.4, Transforming Formulas, where users practice old New York State Regents Examination (NYSRE) questions based on the common core standards. There are 19 previous questions, 9 of them being multiple choice and the other 10 being short answers. I feel that the short answer questions could be graded on the program-end (not teacher scored) because solving literal equations doesn't have much room for error. If that’s too difficult, I’d at least like to display the rubric to the user to see how they could improve their score. At the end of the test I would like for a score to display out of a total. (If only using MC, it’d be out of 18 points [two points each]). 


### Pseudocode
Importing from Word Document
I have no idea how to do this, but I’d like to extract each question from the word document.
Checking Answers
I believe each question would be a function and the user would use a checkbox, or input the MC answer and we would check to see if their answer is equivalent to return a boolean. I would then use an if statement to see if the boolean was True and award two points.

### Define function
Print option 1
Print option 2
Print option 3
Print option 4


### Moving to Next Question
Not sure I know how to do this yet, but I’m guessing it’s a new function to be displayed.

### Showing Total Amount of Points
Each if statement from “checking answers” would be stored in a variable. We take these variables and add them together then divide by 18 to display their final score and percentage.

