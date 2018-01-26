# Program to help the string compression 

def compress_string(string):
    mylist=list(string)
    i=0
    final_str=''
    current=mylist[0]
    count=0

    for i in range(len(mylist)):
        if mylist[i]!=current:
            final_str=final_str+str(current)+str(count) 
            current=mylist[i]
            count=1
        else:
            count=count+1
            if i==(len(mylist)-1):
                final_str=final_str+str(current)+str(count)

    return final_str 

def return_compression (string):
    if len(string)<len(compress_string(string)):
        return string 
    else:
        return compress_string(string)

print(return_compression('aaaaabbcccdeee'))
print(return_compression('abc'))
print(return_compression('aaibc'))
print(return_compression('aaaaaaaaaaaaaaaaaaabcdd'))
