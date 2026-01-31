def precedence(o) :
    if o == '+' or o == '-' :
        return 1
    elif o == '*' or o == '/' :
        return 2
    else :
        return -1

def isRightAssociative(o) :
    return o == '^'

def infix_to_postfix(exp) :
    stack = []
    tokens = list(exp)
    res = ''

    for token in tokens :
        if token in '+-/*^' :
            while len(stack) != 0 and precedence(token) <= precedence(stack[-1]) and stack[-1] != ')' and not isRightAssociative(token):
                res += stack.pop()
            stack.append(token)
        elif token == '(' :
            stack.append(token)
        elif token == ')' :
            while len(stack) != 0 and stack[-1] != '(' :
                res += stack.pop()
            stack.pop()
        else :
            res += token
    while len(stack) != 0 :
        if stack[-1] != '(' :
            res += stack.pop()
        else :
            stack.pop()
    return res
    
        
    
            
exp = "a*(b+c)/d"
print(infix_to_postfix(exp))