# A program to test whether a string has unique characters 

def test_unique(myString):
    sortedString=sorted(myString)

    for i in range(len(myString)-1):
        if sortedString[i]==sortedString[i+1]:
            return 'NO'
    return 'YES'
        


print(test_unique('helo'))
print(test_unique('myworld'))
print(test_unique('green'))
