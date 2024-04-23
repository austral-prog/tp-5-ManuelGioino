def max_of_two(x,y):
    if x > y: 
        return x
    elif x < y:
        return y
    if  x == y:
        return x
        
        
def max_of_three(x, y, z):   
    if (z > x) and (z > y): 
        return z
    elif (x > z) and (x > y):
        return x
    elif (y > x) and (y > z):
        return y
    if z == x == y :
        return x
