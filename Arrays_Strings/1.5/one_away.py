# A program to test whether two strings are one or zero edits away 
# In this program, order doesn't matter and you can either add or delete a character from the string. 


def check_string (str1, str2):

    list1=list(str1)
    list2=list(str2)

    if abs(len(list1)-len(list2))>1:
        return 'NO'

    else:
        return check_list(list1, list2)


def check_list(list1, list2):
    if len(list1)>len(list2):

        for elements in list2:
            if elements not in list1:
                return 'NO' 
        return 'YES' 

    elif list1==list2:
        return 'YES' 

    else:
        for elements in list1:
            if elements not in list2:
                return 'NO' 
        return 'YES'
       

#Test cases 
print(check_string('abc','def')) #NO

print(check_string('abc','ab')) #YES 

print(check_string('abcd','abc')) #YES 

print(check_string('dcba','abc')) #NO

print(check_string('pale','bale')) #YES 
