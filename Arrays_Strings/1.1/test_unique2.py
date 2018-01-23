# A program to test whether a string has unique characters 

def test_unique(myString):
    for char1 in myString:
        count=0
        for char2 in myString:
            if char1==char2:
                count=count+1 

        if count>1:
            return 'NO'
    return 'YES'

print(test_unique('helo'))
print(test_unique('myworld'))
print(test_unique('green'))
