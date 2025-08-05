#You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
#You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
      #You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
      #Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
      # Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.


#Solution
def total_fruit(fruits):
    max_count=0
    left=0
    basket = {}
    
    for right in range(len(fruits)):
        fruit=fruits[right]
        basket[fruit]= basket.get(fruit,0)+1
        while len(basket)>2:
            left_fruit=fruits[left]
            basket[left_fruit]-=1
            if basket[left_fruit]==0:
                del basket[left_fruit]
            left+=1
        max_count = max(max_count,right-left +1)  
    return max_count          
            
#test example
fruit_types=[1,2,1,1,2,2,3,2,1]
max_count = total_fruit(fruit_types)            
print("The maximum number of fruits you can pick are: ",max_count)