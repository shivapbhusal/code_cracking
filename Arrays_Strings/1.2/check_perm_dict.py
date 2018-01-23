# To decide if one string is the permutation of another 

def check_permutation(str1, str2):
    dict1=dict()

    dict2=dict()

    for char in str1:
        if char not in dict1:
            dict1[char]=1
        else:
            dict1[char]=dict1[char]+1 
    
    for char in str2: 
        if char not in dict2:
            dict2[char]=1 
        else:
            dict2[char]=dict2[char]+1 

    if dict1==dict2:
        return 'YES'
    else:
        return 'NO'


print(check_permutation('abc','cba'))
print(check_permutation('abbc','abc'))
