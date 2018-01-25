# Program to test if one string is one away of another
# Order matters 

def one_edit_replace(list1, list2):
    count=0
    for i in range(len(list1)):
        if list1[i]!=list2[i]:
            count=count+1
        if count>1:
            return 'NO'
    return 'YES' 

def one_insert(list1,list2):
    index1=0
    index2=0 

    while (index2<len(list1) and index1<len(list1)):
        if (list1[index1]!=list2[index2]):
            if index1 !=index2:
                return 'NO' 
            index2=index2+1
        else:
            index1=index1+1
            index2=index2+1
    return 'YES'

def test_all(list1, list2):
    if len(list1)==len(list2):
        return one_edit_replace(list1, list2)
    elif len(list1)>len(list2):
        return one_insert(list2, list1)
    else:
        return one_insert(list1, list2)

    
print(test_all(list('ab'),list('abd'))) # Test1 
print(test_all(list('ac'),list('abe'))) # Test1 
print(test_all(list('abc'),list('dbc'))) # Test1 
print(test_all(list('abc'),list('fac'))) # Test1 


    

    


