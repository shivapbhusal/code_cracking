# Program to help the string compression 

def compress_string(string):
    mylist=list(string)
    i=0
    final_str=''
    current=mylist[0]

    count=0
    while (i<len(string)-1):
        if mylist[i]!=current:
            final_str=final_str+str(current)+str(count) 
            current=mylist[i]
            count=0
            i=i+1
        else:
            count=count+1
            i=i+1

    return final_str 

print(compress_string('aaaaabbcccdeee'))
