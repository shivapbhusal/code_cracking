# Python program to test whether two strings are palindrome 

def is_palindrome(str1): ## Just test function

    for i in range(int(len(str1)/2)):
        if str1[i]!=str1[len(str1)-1-i]:
            return 'NO' 
    return 'YES'


def test_perm_palindrome(str1): ## Just test Function
    d=dict()

    for chars in str1:
        if chars in d:
            d[chars]=d[chars]+1 
        else:
            d[chars]=1

    print(d)

def test_palindrome(str1):
    mylist=[]

    for chars in str1:
        if chars in mylist:
            mylist.remove(chars)
        else:
            mylist.append(chars)

    if len(mylist)<=1:
        return 'YES' 

    else:
        return 'NO'

print(test_palindrome('abba')) #YES
print(test_palindrome('abca')) #NO
print(test_palindrome('a')) #YES
print(test_palindrome('ab')) #NO

print(test_palindrome('abca')) #NO

print(test_palindrome('abbac')) #YES

