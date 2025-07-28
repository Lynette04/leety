#This is a roman to integer solution
def roman_to_integer(roman):
    roman_categories={
        'I': 1, 'V':5, 'X':10, 'L':50,  'C':100, 'D':500, 'M':1000
    }
    total = 0
    previous_value =0
    
    for ch in reversed(roman):
        value = roman_categories[ch]
        if value < previous_value:
            total-=value
        else:
            total+=value
            previous_value = value
    return total

roman = input(" Enter a roman numeral:")
integer = roman_to_integer(roman)        
print(integer)