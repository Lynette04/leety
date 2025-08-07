#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#Solution:
 
def first_occurence(h:str,n:str)->int:
    for i in range(len(h)-len(n)+1):
        if  h[i:i+len(n)]==n:
            return i
    return -1
#test
haystack = "sadbutsad"    
needle = "sad"
result=first_occurence(haystack,needle)    
print(result)