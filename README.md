# Log-Parser-Printer
Simple program for parsing a log file according to specific rules

## What does it do ?
Program that takes a log file, reads it line by line and displays a result per line according to the rules described below.

Each printed result line is constructed as follows: [LINE_NUMBER] : [NEW_DATA].
First line of the file is consider as line 0`

Here are the line transformation rules:
- If LINE_NUMBER is a multiple of 5, NEW_DATA is `Multiple de 5` (since 0 is a multiple of any integer).
- If the input line contains at least one '$' character, replace all space characters with '_' and assign the result to NEW_DATA
- If the line ends with the `.` character (ignoring end-of-line characters), NEW_DATA = the input line.
- If the first character of the input line is `{`, deserialize the line, which is in json format, and add the key `pair` to the dictionary, with True as the value if LINE_NUMBER is even (False otherwise). Then serialize this new dictionary in json and assign the result to NEW_DATA.
- If none of the above conditions are met, NEW_DATA is set to `Rien à afficher`.

 Please note: If more than one rule is true for the calculation of NEW_DATA, then only the rule at the top of the list applies.

## How does it works ?


#### Clone the project
`git clone https://github.com/jthillar/log-parser-printer.git`

#### Go inside the project
``cd log-parser-printer``

#### You can run the script by using :
``python main.py your_file.log``

## Additional informations
Project has been written and test with python 3.8.10.

All function are tested. You can use ``python -m unittest discover tests`` to run all tests.


