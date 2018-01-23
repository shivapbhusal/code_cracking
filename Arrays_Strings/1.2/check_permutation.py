# To decide if one string is the permutation of another 

def check_permutation(str1, str2):
    str1=sorted(str1)
    str2=sorted(str2)

    if (str1==str2):
        return 'YES'
    else:
        return 'NO'

print(check_permutation('abc','cba'))
print(check_permutation('abbc','abc'))
