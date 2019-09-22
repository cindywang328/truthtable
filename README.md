# truthtable
Prints ASCII Truth Table for Propositional Logic and [SE212](https://www.student.cs.uwaterloo.ca/~se212/index.html) (Logic and Computation) assignments.

- scans the input string and creates lists of variables and operators by regular expression matching
- uses the shunting-yard algorithm to create a tree of operands (variables) and operators; wraps operators in node classes (ex. a "and" operator has a left and right child, and its valuation is (left's valuation) && (right's valuation). Inspired by Stanford's truthtable [tool](https://web.stanford.edu/class/cs103/tools/truth-table-tool/) 
- Added support for multiple expressions, generating truth table with the set union of the variables in all expressions, using the Redundancy Law (a | a&b <-> a)
- No more typing truth tables for SE212!

![screenshot](https://raw.githubusercontent.com/cindywang328/truthtable/master/Screen%20Shot%202019-09-22%20at%2012.32.01%20AM.png)

