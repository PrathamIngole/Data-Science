def precedence(o) :
    if o == '+' or o == '-' :
        return 1
    elif o == '*' or o == '/' :
        return 2
    elif o == '^' :
        return 3
    else :
        return -1

def isRightAssociative(o) :
    return o == '^'

def infix_to_prefix(exp) :
    stack = []
    res = ''
    tokens = list(exp) 

    # step 1. reverse the given expression 
    tokens = list(reversed(tokens)) 

    # step 2. replace all '(' to ')' and all ')' to '('
    for i in range(len(tokens)) : 
        if tokens[i] == '(' : 
            tokens[i] = ')'
        elif tokens[i] == ')' : 
            tokens[i] = '('
    
    # step 3. apply infix to postfix 
    for token in tokens :
        if ('a' <= token <= 'b') or ('A' <= token <= 'Z') or ('0' <= token <= '9') :
            res += token
        elif token == '(' :
            stack.append(token)
        elif token == ')' :
            while stack and stack[-1] != '(' :
                res += stack.pop()
            stack.pop()
        else :
            while stack and stack[-1] != '(' and (precedence(token) < precedence(stack[-1]) or precedence(token) == precedence(stack[-1])) and not isRightAssociative(token) :
                res += stack.pop()
            stack.append(token)

    while stack :
        res += stack.pop()
    
    
    return ''.join(reversed(res))

exp = "a*(b+c)/d"
print(infix_to_prefix(exp))
print("fdsf")