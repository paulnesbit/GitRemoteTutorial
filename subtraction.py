#---- This is a script that subtracts stuff through the magic of Python ----

def sub(a, b):
    '''Returns the remainder of b from a'''
    return a - b

# Define Variables
x = 10
y = 7
ans = sub(x,y)

# Prints the equation and result in an 'f' string
print(f'\n {x} - {y} = {ans}\n')
