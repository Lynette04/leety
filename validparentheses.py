#This shows if a given pair of brackets match, for example ( matches with ) but ( does not match with }
def is_valid(p):
    stack=[]
    mapping={
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for char in p:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            continue
    return not stack
    
    
#test example
print(is_valid("()"))    
print(is_valid("(]"))    