x = 2

N = 7 #number of iterations
a = 1 # initial 
c = 2/3
d = 3

def cuberoot(x):
    if x < 0:
        x = abs(x)
        cube_root = x**(1/3)*(-1)
    else:
        cube_root = x**(1/3)
    return cube_root

for i in range(N):
    anext = (c*a)+(x/(d*a^2))
    a = anext
    print("Step {}, our approximation: {}, error:{}".format(i, numerical_approx(anext), numerical_approx(anext - cuberoot(x))))
    
print("\nThe correct value of cube root of 2 is " + str(numerical_approx(cuberoot(2))
