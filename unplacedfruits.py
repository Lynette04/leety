#You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.
#From left to right, place the fruits according to these rules:
   #Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
   #Each basket can hold only one type of fruit.
   #If a fruit type cannot be placed in any basket, it remains unplaced.
#Return the number of fruit types that remain unplaced after all possible allocations are made.
#Solution:
 
def unplacedfruit(fruits,baskets):
    unplacedcount = 0
    n=len(fruits)
    used_basket=[False]*n
    
    for i in range(n):
        placed=False
        for j in range(n):
            if not used_basket[j] and baskets[j] >= fruits[i] :
                used_basket[j]=True
                placed = True
                break
        if not placed:
            unplacedcount+=1
    return unplacedcount    
            
    
#test
fruits=[1,4,8]
baskets=[2,3,6]
unplaced_fruits_number=unplacedfruit(fruits,baskets)
print(unplaced_fruits_number)            