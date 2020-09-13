# truthtable
Prints ASCII Truth Table for Propositional Logic and [SE212](https://www.student.cs.uwaterloo.ca/~se212/index.html) (Logic and Computation) assignments.

- scans the input string and creates lists of variables and operators by regular expression matching
- uses the shunting-yard algorithm to create a tree of operands (variables) and operators; wraps operators in node classes (ex. a "and" operator has a left and right child, and its valuation is (left's valuation) && (right's valuation). Inspired by Stanford's [truthtable tool](https://web.stanford.edu/class/cs103/tools/truth-table-tool/) 
- Added support for multiple expressions, generating truth table with the set union of the variables in all expressions, using the Redundancy Law (a | a&b <-> a)
- Fits the format used by [George, SE212's verification tool](https://www.student.cs.uwaterloo.ca/~se212/george/ask-george/)
- No more typing truth tables for SE212!

![screenshot](https://raw.githubusercontent.com/cindywang328/truthtable/master/Screen%20Shot%202019-09-22%20at%2012.32.01%20AM.png)

## Installation
* Clone the repository
* Make main.py executable
```bash
chmod +x main.py
```
* Create a symlink
```bash
sudo ln -sf /path/to/repo/main.py /usr/local/bin/tt
```
* You can now run the executable:
```bash
tt 'a & b' 'b => c'

a | b | c || a & b | b => c
___________________________
F | F | F || F     | T
F | F | T || F     | T
F | T | F || F     | F
F | T | T || F     | T
T | F | F || F     | T
T | F | T || F     | T
T | T | F || T     | F
T | T | T || T     | T
```

I managed to connect this to a webpage using Flask, but it appears that Flask can't be deployed on [GitHub Pages](https://stackoverflow.com/questions/23807039/flask-app-on-github-pages). It was still a good learning experience. 
![screenshot](https://raw.githubusercontent.com/cindywang328/truthtable/master/Screen%20Shot%202019-09-22%20at%203.04.27%20AM.png)
