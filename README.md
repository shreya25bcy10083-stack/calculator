# Calculator
It is a beginner level calculator designed with python language.

🧮 Calculator App (Python + Tkinter)
This is a beginner-friendly GUI Calculator made using Python and the Tkinter library.
It performs basic arithmetic operations like addition, subtraction, multiplication, division, and a few extra functions such as square, percentage, and backspace.

📌 Features
✔️ Simple and clean user interface
✔️ Basic operations: +, -, *, /
✔️ Square function (x²)
✔️ Percentage (%)
✔️ Decimal support
✔️ Clear (C) and Backspace (⌫) buttons
✔️ Error handling for invalid inputs

📁 Project Structure
calculator.py   →  Main Python file containing the entire calculator code

🚀 How to Run the Program
1. Install Python
2. Run the script
Open a terminal or command prompt in the folder containing calculator.py, then type:
python calculator.py
The calculator window will appear.

🧱 How the Program Works
1. Tkinter Window
The program creates a main window using tk.Tk().
A large entry box at the top displays numbers and results.
2. Button Clicks
Each button is linked to a function.
When you click digits or operators, they are added to the entry box.
3. Special Functions
Function Description-
C-	Clears everything
⌫-	Deletes last character
=	Evaluates the expression
x²-	Squares the number
%	-Converts value to percentage (number/100)
4. Evaluation
The equal() function uses Python’s eval() to calculate results.
Errors are caught and displayed as "Error".

📸 User Interface Layout
Rows and columns are arranged using .grid(), making the layout structured like a real calculator.

🔧 Requirements
This project uses only built-in libraries:

Python
Tkinter (comes with Python)
No extra installation is needed.

🙋‍♀️ Who is this for?
Perfect for:
Beginners learning Tkinter
Students building a GUI project
Anyone wanting a simple calculator app in Python

By-
Shreya Singh
