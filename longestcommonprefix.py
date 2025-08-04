#This is a function to find the longest common prefix of a group of words in an array
def longestcommonprefix(strings):
    if len(strings)==0:
        return ""
    
    prefix=strings[0]
    
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix=prefix[:-1]
            
            if not prefix:
                return ""
    return prefix        


#Test example
strs=["block", "blow", "bloom"]
result = longestcommonprefix(strs)
print("The longest common prefix is ",result)