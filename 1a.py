'''
Gabriel Patron
2014-89015
CS 131 THU

Michael Pio Mayol
2014-32780
CS 131 THU
'''
def newton_raphson(a, m, n, x=1, desired_percent_error=.01):
    '''
    input: integer a, integer m, integer n, 
    optional inputs: integer x, float desired_percent_error

    output: integer x

    Applies the newton raphson method to get a^(m/n). Continully does this
    until percent_error is less than the desired_percent_error
    '''

    percent_error = 1
    while (percent_error >= desired_percent_error):
        xnp1 = x - (compute_fx(x, n, a, m) / compute_dfx(x, n, a, m))
        percent_error = get_percent_error(xnp1, x)
        x = xnp1
    return x

def get_percent_error(xnp1, xn):
    '''
    input: integer xnp1, xn
    output: float 

    Calculates the percentage error
    '''
    return abs(((xnp1 - xn) / xnp1))

def fake_exponent(base, exp):
    '''
    input: integer base, integer exp
    output: integer b

    Uses for loop to get the value of the exponent, base^exp
    '''
    b = 1 
    for i in range(exp):
        b *= base 
    return b

def compute_fx(x, n, a, m):
    '''
    input: integer x, integer n, integer a, integer m
    output: integer

    Computes f(x) = x^n - a^m
    '''
    return fake_exponent(x, n) - fake_exponent(a, m)

def compute_dfx(x, n, a, m):
     '''
    input: integer x, integer n, integer a, integer m
    output: integer

    Computes the derivative of f'(x) = n * (x)^(n-1)
    '''
    return (n)*(fake_exponent(x, n-1))

if __name__ == '__main__':
    a, m, n = input('A, M, N: ').split()
    a = int(a)
    m = int(m)
    n = int(n)
    result = newton_raphson(a, m, n)
    print('{}^({}/{}) = {}'.format(a, m, n, result))
