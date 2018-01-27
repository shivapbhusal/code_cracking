# Program to perform string rotation 

def isSubString(S1, S2):
    if (S1=='' or S2==''):
        return True
    else:
        if len(S1)==len(S2):
            return (S1==S2)

        elif len(S1)>len(S2):
            return checkSubString(S1, S2)

        else:
            return checkSubString(S2, S1)

def checkSubString(S1, S2):
    L=0 
    while (L<len(S1)):
        if S1[L]==S2[0]:
            if S1[L:L+len(S2)]==S2:
                return True
        L=L+1
    return False

print(isSubString('abcd','abc'))
print(isSubString('abcd','bc'))
print(isSubString('abcd','bcde'))

print(isSubString('a','bcade'))

print(isSubString('','abc'))


