import numpy as np
#Gauss_Seidel_Method alogritem
def Gauss_Seidel_Method(matrix, b):
    D = create_D(matrix)
    L = create_L(matrix)
    U = create_U(matrix)

    L_D = sum_mat(L, D)
    L_D_INVERSE = (L_D.I)
    L_D_U = np.matmul(L_D_INVERSE, U)
    L_D_b = np.matmul(L_D_INVERSE, b)
    L_D_U_1 = multi_scalar(L_D_U,-1)

    new_b = []
    for i in range(len(b)):
        new_b.append(1.0)

    L_D_b = L_D_b.getA()[0]

    printList = []
    r = iterative(L_D_U_1, new_b ,L_D_b, printList)
    P_List(printList, len(matrix[0]))

    return r
#all the func we will use
def create_D(matrix):
    result = []
    for i in range(len(matrix)):
        m = []
        for j in range(len(matrix)):
            if i == j:
                m.append(float(matrix.item(i, j)))
            else:
                m.append(0.0)
        result.append(m)
    D = np.matrix(result)
    return D
def create_L(matrix):
    result = []
    for i in range(len(matrix)):
        m = []
        for j in range(len(matrix)):
            if i > j:
                m.append(float(matrix.item(i, j)))
            else:
                m.append(0.0)
        result.append(m)
    L = np.matrix(result)
    return L
def create_U(matrix):
    result = []
    for i in range(len(matrix)):
        m = []
        for j in range(len(matrix)):
            if i < j:
                m.append(float(matrix.item(i, j)))
            else:
                m.append(0.0)
        result.append(m)
    U = np.matrix(result)
    return U
def iterative(matrix, b, c, printList):
    result = []
    sum = 0
    count = 0
    k = 0
    flag = 0
    flag2 = 0

    for i in range(len(matrix)):
        result.append(0)

    while(flag2 == 0 and count <= 50):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                sum = sum + (matrix.item(i, j)*result[j])
            sum = sum + c[i]
            if  b[i] > 0.001:
                sum = sum / b[i]
            if abs(sum - result[i]) > 0.0000001:
                flag = 1
            result[i] = sum
            sum = 0

        if flag == 0:
            flag2 = 1
        else:
            flag = 0
        count = count + 1
        printList.append(count)
        for j in result:
            printList.append(j)

    return result
def P_List(printList, num):
    for i in range(0 ,len(printList), num + 1):
        print("number iteration:", printList[i])
        for j in range(1 , num + 1):
            print("x", j, ": ", printList[i + j])
def sum_mat(mat1, mat2):
        result = []

        for i in range(len(mat1)):
            mylist = []
            for j in range(len(mat2)):
                mylist.append(0.0)
            result.append(mylist)

        mat = np.matrix(result)

        for i in range(len(mat1)):
            for j in range(len(mat2)):
                mat.itemset((i, j), (mat1.item(i, j) + mat2.item(i, j)))

        new_mat = np.matrix(mat)
        return new_mat
def multi_scalar(mat, num):
    result = []

    for i in range(len(mat)):
        mylist = []
        for j in range(len(mat)):
            mylist.append(mat.item(i, j) * num)
        result.append(mylist)

    new_mat = np.matrix(result)
    return new_mat



# a tryout for the progrenm for NxN matrix AND vector b
# initialize the matrix
a = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0., 3., -1., 8.]])
# initialize the RHS vector
b = np.array([6.0, 25.0, -11.0, 15.0])
print( "Solution:", Gauss_Seidel_Method(a, b))
