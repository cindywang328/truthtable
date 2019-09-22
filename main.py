import re
from collections import defaultdict
from pprint import pprint
# only use &, !, |, =>, <=>, T, F, (). Variables must be a letter.
def check_integrity(s):
  for i in s:
    if not re.match("[A-Za-z_0-9\\\/<>\-~()\s\&\|\=\!]", i):
      raise Exception("Illegal character")

def read_operator(s, index):
  # Single char operator
  if re.match("[()TF!&|]", s[index]):
    return s[index]
  
  if index == len(s) -1 :
    return None
  
  #2 char operator; =>, or
  if s[index:index+2] == "=>":
    return s[index:index+2]

  if index == len(s) -2:
    return None

  #3 char
  subs = s[index:index+3]
  if subs == "<=>":
    return subs

  return None

def is_reserved_word(c):
  return c in ["!", "&", "|", "T", "F", "=>", "<=>" ]

def read_variable(s, index):
  if not re.match("[A-Za-z]", s[index]):
    return None
  
  res = ""
  while index < len(s) and re.match("[A-Za-z]", s[index]):
    res += s[index]
    index += 1
  
  return res

def make_identity_token(s, index):
  return {"type": s, "start": index, "end": index + len(s)}

def make_variable_token(index, start, end):
  return {"type": "variable", "index": index, "start": start, "end": end}

def scan_variable(input, index, variableSet):
  var_name = read_variable(input, index)
  variableSet[var_name] = True
  return var_name

def preliminary_scan(input):
  variableSet = defaultdict(bool)
  i = 0
  tokens = []

  while(i <= len(input)):
    if i >= len(input):
      #tokens.append(make_identity_token(input[i], i))
      return {"tokens": tokens, "variableSet": variableSet}

    if read_variable(input, i):
      var = read_variable(input, i)
      variableSet[var] = True
      tokens.append(make_variable_token(var, i, i + len(var)))
      #print(make_variable_token(var, i, i + len(var)))
      i += len(var)
    
    elif read_operator(input, i):
      op = read_operator(input, i)
      tokens.append(make_identity_token(op, i))
      i += len(op)
    
    elif input[i] == " ":
      i += 1
    
    else:
      raise Exception("Invalid character " + input[i])

def number_variables(prelim_dict):
  # {"tokens": tokens, "variableSet": variableSet}
  vars = []
  for key in prelim_dict["variableSet"].keys():
    vars.append(key)
  
  vars.sort()

  for i in range(len(vars)):
    prelim_dict["variableSet"][vars[i]] = i
  
  
  for i in range(len(prelim_dict["tokens"])):
    if prelim_dict["tokens"][i]["type"] == "variable":
      prelim_dict["tokens"][i]["index"] = prelim_dict["variableSet"][prelim_dict["tokens"][i]["index"]]
  
  return {"tokens": prelim_dict["tokens"], "variables": vars}


def scan(input):
  preliminary_dict = preliminary_scan(input)
  return number_variables(preliminary_dict)
class TrueNode:
  def __init__(self):
    pass
  def evaluate(self, assignment):
    return True
  def toString(self, variables):
    return "T"

class FalseNode:
  def __init__(self):
    pass
  def evaluate(self, assignment):
    return False
  def toString(self, variables):
    return "F"
  
class NegateNode:
  def __init__(self, underlying):
    self.underlying = underlying
  
  def evaluate(self, assignment):
    return not self.underlying.evaluate(assignment)
  
  def toString(self, variables):
    return " NOT " + self.underlying.toString(variables)
  
class AndNode:
  def __init__(self, left, right):
    self.left = left
    self.right = right
  
  def evaluate(self, assignment):
    return self.left.evaluate(assignment) and self.right.evaluate(assignment)
  
  def toString(self, variables):
    return "(" + self.left.toString(variables) + " AND " + self.right.toString(variables) + ")"
  
class OrNode:
  def __init__(self, left, right):
    self.left = left
    self.right = right
  
  def evaluate(self, assignment):
    return self.left.evaluate(assignment) or self.right.evaluate(assignment)
  
  def toString(self, variables):
    return "(" + self.left.toString(variables) + " OR " + self.right.toString(variables) + ")"

class ImpliesNode:
  def __init__(self, left, right):
    self.left = left
    self.right = right
  
  def evaluate(self, assignment):
    return (not self.left.evaluate(assignment)) or self.right.evaluate(assignment)
  
  def toString(self, variables):
    return "(" + self.left.toString(variables) + " IMP " + self.right.toString(variables) + ")"
  
class IffNode:
  def __init__(self, left, right):
    self.left = left
    self.right = right
  
  def evaluate(self, assignment):
    return self.left.evaluate(assignment) == self.right.evaluate(assignment)
  
  def toString(self, variables):
    return "(" + self.left.toString(variables) + " IFF " + self.right.toString(variables) + ")"

class VariableNode:
  def __init__(self, index):
    self.index = index
  
  def evaluate(self, assignment):
    return assignment[self.index]
  
  def toString(self, variables):
    return variables[self.index]

# /* All AST nodes must have functions of the form
#  *
#  *   evaluate(assignment), which returns the value of the expression given the
#  *                         variable assignment as an array of Trues and Falses.
#  *   toString(variables),  which produces a human-readable representation of the
#  *                         AST rooted at the node given the variables information.
#  *                         in variables. The expression should have parentheses
#  *                         added as appropriate.

def isOperand(token):
  return token["type"] == "T" or token["type"] == "F" or token["type"] == "variable"

def wrapOperand(token):
  if token["type"] == "T":
    return TrueNode() 
  elif token["type"] == "F": 
    return FalseNode() 
  elif token["type"] == "variable":
    return VariableNode(token["index"])
  else:
    raise Exception ("invalid operand for wrap")

def priority(token):
  return 0 if token["type"] == "<=>" else 1 if token["type"] == "=>" else 2 if token["type"] == "|" else 3 if token["type"] == "&" else -1 if token ["type"] == "$" else None

def isBinaryOperator(token):
  return token["type"] in ["<=>", "=>", "|", "&"]

def createOperatorNode(left, token, right):
  return IffNode(left, right) if token["type"] == "<=>" else ImpliesNode(left, right) if token["type"] == "=>" else OrNode(left, right) if token["type"] == "|" else AndNode(left, right) if token["type"] == "&" else None 

def addOperand(node, operands, operators):
  while(len(operators)>0 and operators[-1]["type"] == "!"):
    operators.pop(len(operators)-1)
    node = NegateNode(node)
  operands.append(node)

def parse(input):
  scanResult = scan(input)
  tokens = scanResult["tokens"]
  tokens.append({'end': len(input), 'start': len(input), 'type': '$'}) # EOF Constant
  operators = []
  operands = []
  needOperand = True

  for t in tokens:
    if needOperand:
      if isOperand(t):
        addOperand(wrapOperand(t), operands, operators)
        needOperand = False

      elif t["type"] == "(" or t["type"] == "!":
        operators.append(t) #operator stack
      
      elif t['type'] == '$':
        # end
        if len(operators) == 0:
          raise Exception ("Operator stack empty")
        if operators[-1]["type"] == "(":
          raise Exception ("Invalid brackets")
        raise Exception ("Operator missing operand: " + str(operators[-1]))
      else:
        raise Exception ("Expecting variable, constant, or (")
    else:
      if isBinaryOperator(t) or t["type"] == "$":

        while(True):
          if len(operators) == 0 or operators[-1]["type"] == "(":
            break
          #print(t)
          if priority(operators[-1]) <= priority(t):
            break # No more higher priority operators
          
          operator = operators.pop(len(operators)-1)
          right = operands.pop(len(operands) -1)
          left = operands.pop(len(operands) -1)

          addOperand(createOperatorNode(left, operator, right), operands, operators)
          
        operators.append(t)
        needOperand = True # just read an operator.
        if t["type"] == "$":
          break # EOF is ok? 

      elif t["type"] == ")":
        while(True): # keep popping until we get a (
          # Credits for parse algorithm to web.stanford.edu/class/cs103/tools/truth-table-tool/
          if len(operators) == 0:
            raise Exception (") doesn't match any (")
          cur_op = operators.pop(len(operators)-1)

          if cur_op["type"] == "(":
            break
          elif cur_op["type"] == "!":
            raise Exception ("Nothing to negate")
          
          right = operands.pop(len(operands)-1)
          left = operands.pop(len(operands)-1)
          addOperand(createOperatorNode(left, cur_op, right), operands, operators)
        # stack top contains the operand produced from the () expression? 
        exp = operands.pop(len(operands)-1)
        addOperand(exp, operands, operators)
      else:
        raise Exception ("expecting ) or binary operator at "+str(t["start"]))
  
  assert(len(operators) != 0)
  assert(operators.pop(len(operators)-1)["type"] == "$")

  return {"ast": operands.pop(len(operands)-1), "variables": scanResult["variables"]}

def next_assign(assign):
  #print(assign)
  flip = len(assign)-1
  while (flip >= 0 and assign[flip]):
    flip -= 1 # find a F to turn to T 
  #FFF
  #FFT
  #FTF
  #FTT 
  #FTFF
  if flip == -1:
    return False #we're done
  #flip += 1
  #print(flip)
  
  assign[flip] = True
  for i in range(flip + 1, len(assign)):
    assign[i] = False
  
  return True

def generate_tt_results_column(parse_res):
  assign = [False] * len(parse_res["variables"])
  ans_col = []
  while(True):
    ans_col.append(parse_res["ast"].evaluate(assign))
    if not next_assign(assign):
      break
  return ans_col

def union_variable_set(input_list):
  #return another input list to parse but only print original
  #input string to list of its variables
  new_input_list = []
  scanned_variables_map = {input_str: scan(input_str)["variables"] for input_str in input_list}#[set(scan(i).variables) for i in input_list]
  union_var_set = set().union(*(scanned_variables_map.values()))
  for input_str in input_list:
    #A.difference(B) for A-B
    extra_vars = union_var_set.difference(set(scanned_variables_map[input_str]))
    if not extra_vars:
      new_input_list.append(input_str)
    else:
      new_input_list.append("("+input_str + ")| (("+input_str + ") &" + " & ".join([v + " " for v in extra_vars]) + ")")

  return new_input_list


def print_multi_truth_table_results(input_list):
  new_input_list = union_variable_set(input_list)
  print("")
  print(new_input_list)

  pr = parse(new_input_list[0])
  # header
  resstr = ""
  for v in pr["variables"]:
    resstr += v + " | "
  resstr = resstr[:len(resstr)-1] + "| "

  for exp in input_list:
    resstr += exp + " | "
  resstr = resstr[:len(resstr)-3]

  print(resstr)
  print("_"*len(resstr))
  parse_res_list = [pr]
  
  num_vars = len(pr["variables"])

  
  for i in range(1, len(new_input_list)):
    p = parse(new_input_list[i])
    # if (p["variables"]) != pr["variables"]:
    #   raise Exception ("different formulas have incompatible variables")
    parse_res_list.append(p)
  

  assign = [False] * len(pr["variables"])
  ans = [[]]
  # left side first
  while(True):
    new_row = []
    for x in assign:
      new_row.append(x)
    ans.append(new_row)
    if not next_assign(assign):
      break
  ans.pop(0)


  for p in parse_res_list:
    assign = [False] * len(pr["variables"])
    index = 0
    while(True):
      ans[index].append(p["ast"].evaluate(assign))
      index += 1
      if not next_assign(assign):
        break
  
  print_tt(ans, num_vars, input_list, pr["variables"])

def print_tt(arr, num_vars, input_list, variables_list):

  for row in arr:
    idx = 0
    res_str = ""
    for el in row[:num_vars]:
      res_str += ("T" if el else "F") + " "*(len(variables_list[idx])-1)+" | " 
      idx += 1
    res_str = res_str[:len(res_str)-1] + "| "

    for i in range(num_vars, len(row)):
      res_str += ("T" if row[i] else "F") + " "*(len(input_list[i - num_vars]) - 1) + " | "
    
    print(res_str[:len(res_str)-3])

def main():
  # put propositional logic formulas in the input list
  # variables should be A-Za-z and not T/F
  # operators should be ! | & => <=> () 
  # generates TT using set union of all variables, using the "a | a&b <-> a" rule
  input_list = ["(!c => a) & a <=> a", "b & c => d", "d | a", "c & !d"]
  print_multi_truth_table_results(input_list)







  



