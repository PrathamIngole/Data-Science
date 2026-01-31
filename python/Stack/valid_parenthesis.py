def valid_parenthesis(s) :
    stack = []
    for p in s :
        if p in '({[' :
            stack.append(p)
        elif p == ')' and stack.pop() != '(':
            return False
        elif p == '}' and stack.pop() != '{':
            return False
        elif p == ']' and stack.pop() != '[':
            return False
    return len(stack) == 0        

print(valid_parenthesis('({[]})'))