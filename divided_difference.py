def compute_x_prod(point, x, i):
    x_prod = 1

    for _i in range(i):
        x_prod *= point - x[_i]
    
    return x_prod

def interpolate(point, x, y):
    n = len(y)
    total = y[0][0]
    x_prod = 0 

    for i in range(1, n):
        x_prod = compute_x_prod(point, x, i)
        total += (y[0][i] * x_prod)

    return total

def print_divided_difference(y):
    n = len(y)

    for i in range(n):
        for j in range(n - i):
            print(y[i][j], "\t", end = " ");
        print("")

def divided_difference(x, y):
    n = len(x)
    
    for i in range (1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) / (x[j] - x[i + j]))
    
    return y


if __name__ == '__main__':
    x = [ -5, -1, 0, 2 ]
    y = [[0 for i in range(len(x))] for j in range(len(x))]

    y[0][0] = -2
    y[1][0] = 6
    y[2][0] = 1
    y[3][0] = 3
    
    y = divided_difference(x, y)
    print_divided_difference(y)
    val = interpolate(7, x, y)
    print(val)