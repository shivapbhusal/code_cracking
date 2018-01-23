## Using List

def test_unique(myString):
    test_list=[]

    for chars in myString:
        if chars in test_list:
            return 'NO' 
        else:
            test_list.append(chars)
    return 'YES' 

print(test_unique('hello'))
print(test_unique('abcde'))

