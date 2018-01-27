# A program to rotate matrix 

def rotate_matrix(matrix):
    N=len(matrix)

    for layer in range(int(N/2)):
            first=layer
            last=N-1-layer 
            for i in range(first, last):
            	offset=i-first
            	top=matrix[first][i]
            	matrix[first][i]=matrix[last-offset][first]

            	matrix[last][last-offset]=matrix[i][last]

            	matrix[i][last]=top
    return matrix


            
print(rotate_matrix([[1,2],[2,3]]))

print(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))


