import math

def newton_raphson(a=0, x=.5, desired_percent_error=.01):
    percent_error = 1
    
    while (percent_error >= desired_percent_error):
        xnp1 = x - (compute_fx(x, a) / compute_dfx(x))
        percent_error = get_percent_error(xnp1, x)
        x = xnp1
    
    return x

def get_percent_error(xnp1, xn):
    return abs(((xnp1 - xn) / xnp1))

def compute_fx(x, a):
    return math.sin(x) - a

def compute_dfx(x):
    return math.cos(x)

if __name__ == '__main__':
    a = float(input('A: '))
    result = newton_raphson(a)
    print('arcsin({}) = {}'.format(a, result))
