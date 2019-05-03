'''
Gabriel Patron
2014-89015
CS 131 THU

Michael Pio Mayol
2014-32780
CS 131 THU
'''

def create_square_matrix(N):
    '''
    input: integer N
    output: NxN matrix

    generates an empty square matrix of size N
    '''
    matrix = []
    for x in range(N):
        row = []
        for y in range(N):
            row.append(0)
        matrix.append(row)
    return matrix

def print_matrix(M):
    '''
    input: matrix M
    output: none

    prints the matrix M in a pretty manner 
    '''
    for row in M:
        print(row)
    print()

def divided_difference(x, y):
    '''
    input: vector x, matrix y
    output: matrix y

    fills the divided difference table for y
    '''
    n = len(x)
    
    for i in range (1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) / (x[j] - x[i + j]))
    
    return y

def find_constants(x, y, N, k):
    '''
    input: vector x, vector y, integer N, integer k
    output: vector A

    finds the values of A using Newton's divided differencce formula
    and expanding to get the form of s(k) = a0 + a1 * x + a2 * x^2 + a3 * x^3
    where the a0, a1, a2, and a3 are the values of A
    '''
    points = range(k-1, k+2+1)
    if (k == 0):
        points = range(0, 3+1)
    if (k == N-2):
        points = range(N-4, N-1+1)
    
    actual_x = [x[p] for p in points]
    actual_y = [y[p] for p in points]

    y_table = create_square_matrix(4)
    for i in range(4):
        y_table[i][0] = actual_y[i]
    
    # divided diff!!!
    div_diff = divided_difference(actual_x, y_table)

    # print_matrix(div_diff)

    # declare variables
    b1 = div_diff[0][0]
    b2 = div_diff[0][1]
    b3 = div_diff[0][2]
    b4 = div_diff[0][3]

    x1 = actual_x[0]
    x2 = actual_x[1]
    x3 = actual_x[2]
    x4 = actual_x[3]

    # compute constants
    a0 = b1 - (b2 * x1) + (b3 * x1 * x2) - (b4 * x1 * x2 * x3)
    a1 = b2 - (b3 * x1) - (b3 * x2) + (b4 * x1 * x2) + (b4 * x1 * x3) + (b4 * x2 * x3)
    a2 = b3 - (b4 * x1) - (b4 * x2) - (b4 * x3)
    a3 = b4
    
    return [a0, a1, a2, a3]

def do_the_thing(x, y):
    '''
    input: vector x, vector y
    output: none

    drives the whole program and prints the resulting matrix M
    which has the values of A for each iteration
    '''
    N = len(x)
    M = create_square_matrix(N-1)

    for k in range(N-1):
        M[k] = find_constants(x, y, N, k)
    
    print_matrix(M)

if __name__ == '__main__':
    X = [1, 4, 7, 10, 15, 22, 30]
    Y = [1, 3, 6, 13, 21, 32, 45]
    
    test_X = [1, 2, 3, 4, 5, 6, 7]
    test_Y = [4, 5, 6, 7, 8, 9, 10]

    test2_X = [-2, -1, 0, 1]
    test2_Y = [-3, 1, -1, -3]
    
    do_the_thing(test2_X, test2_Y)