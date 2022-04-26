from multiprocessing.sharedctypes import Value
import numpy as np


# print(np.shape(A)[1])



# def strassen_meth(A,B):

#     if np.shape(A)[1] == np.shape(B)[0]:
        
#         if len(A) == 1 and len(B) ==1:
#             print("Output =", A[0]*B[0])
            
#         else:
#             a, b, c, d = divide(A)                 
#             e, f, g, h = divide(B)                 

#             p1 = strassen_meth(a+d,e+h)
#             p2 = strassen_meth(d, g-e)
#             p3 = strassen_meth(a+b, h)
#             p4 = strassen_meth(b-d, g+h)
#             p5 = strassen_meth(a, f-h)
#             p6 = strassen_meth(c+d, e)
#             p7 = strassen_meth(a-c, e+f)

#             c11 = (p1 + p2) - (p3 + p4)
#             c12 = p5 + p3
#             c21 = p6 + p2
#             c22 = (p5 + p1) - (p6 - p7)

#             print([[c11, c12],[c21,c22]])
#             print("sakoon sird qabar me ha")


#     else:
#         print('The columns of matrix A is not equal to the rows of matrix B and hence matrix multiplication cannot be performed')

def divide(matrix):
    # R, C = np.shape(matrix)
    # R, C = matrix.shape
    R = len(matrix)
    C = len(matrix[0])
    print(R,C)
    r = R//2
    c = C//2
    print(r,c)
    # return matrix[:r, :c], matrix[:r, c:],matrix[r:, :c], matrix[r:,c:]
    return matrix[:r][:c], matrix[:r][c:],matrix[r:][:c],matrix[r:][c:]


def strassen_meth(A,B):

    if len(A) == 1 :
        print("Output =", A[0]*B[0])
        value = A[0]*B[0]
        return value
        
    else:
        a, b, c, d = divide(A)                 
        e, f, g, h = divide(B)                 

        p1 = strassen_meth(a+d,e+h)
        p2 = strassen_meth(d, g-e)
        p3 = strassen_meth(a+b, h)
        p4 = strassen_meth(b-d, g+h)
        p5 = strassen_meth(a, f-h)
        p6 = strassen_meth(c+d, e)
        p7 = strassen_meth(a-c, e+f)

        c11 = (p1 + p2) - (p3 + p4)
        c12 = p5 + p3
        c21 = p6 + p2
        c22 = (p5 + p1) - (p6 - p7)

        # a = [[c11, c12],[c21,c22]]
        # return a
        
        print("sakoon sird qabar me ha")
        c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
        c = np.reshape(c,(3,3))
        return c


# A =np.array([[9,1,7],
#             [1,2,3],
#             [2,4,5],
#             [2,5,6]])
#             # 4x3
# B =np.array([[1,1,1],
#             [1,2,3],
#             [2,4,5]])
#             # 3x3
# A =np.array([[1,2,3],
#             [2,4,5],
#             [2,5,6]])
# B =np.array([[1,1,1],
#             [1,2,3],
#             [2,4,5]])
A =([[9,1,7],
    [1,2,3],
    [2,4,5],
    [2,5,6]])
           
B =([[1,1,1],
    [1,2,3],
    [2,4,5]])

print(strassen_meth(A,B))