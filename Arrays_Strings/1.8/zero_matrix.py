# A program to set all the elements of matrix to zero if one element is 0 

def zero_matrix(matrix):
    N=len(matrix)
    M=len(matrix[0])

    for i in range(N):
        for j in range(M):
            if matrix[i][j]==0:
                return set_zero(matrix)

    return matrix 




def set_zero(matrix):
    N=len(matrix)
    M=len(matrix[0])

    for i in range(N):
        for j in range(M):
            matrix[i][j]=0 
    
    return matrix

print(zero_matrix([[1],[2],[3]]))

print(zero_matrix([[1,0],[2,3],[4,5]]))
