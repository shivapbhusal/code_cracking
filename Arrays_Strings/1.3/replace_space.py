# Python program to replace all the spaces in a string 

def replace(string, length):
    temp_str=''
    for char in string:
        if char==' ':
            temp_str=temp_str+'%20'
        else:
            temp_str=temp_str+char
    
    return temp_str 

print(replace('  abc def     ', 4))

       
