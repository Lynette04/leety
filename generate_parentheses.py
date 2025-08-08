#This is a function to generate n pairs of parentheses in any order.
def generate_parentheses(n):
    result=[]
    def backtracking(current, open_count,closed_count):
        if len(current)==2*n:
            result.append(current)
            return
        if open_count<n:
            backtracking(current+'(',open_count+1,closed_count)
        if closed_count<open_count:
            backtracking(current+')',open_count,closed_count+1)
                
    backtracking('',0,0)
    return result            

#test example
print(generate_parentheses(3))