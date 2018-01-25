# Program to help the string compression 

def compress_string(string):
    mylist=list(string)
    i=0

    final_str=""

    while (i<len(string)-1):
        count=1
        if mylist[i]==mylist[i+1]:
            i=i+1 
            count=count+1

        final_str=final_str+str(mylist[i]+str(count))

        i=i+1 

    return final_str 

print(compress_string('abcde'))
print(compress_string('aabbcccdeee'))
