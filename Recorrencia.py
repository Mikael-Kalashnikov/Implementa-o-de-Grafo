import math

def getRoots(a,p,q):
    if(a > 1):
        p = p/a
        q = q/a
        a = a/a

    delta = (p**2-4*1*q)
    if(delta > 0):
        r1 = (int) ((-p+math.sqrt(delta))/2*a)
        r2 = (int) ((-p-math.sqrt(delta))/2*a)
        result = "Xn = C1("+(str)(r1)+")^n + C2("+(str)(r2)+")^n"
        return result
    elif(delta == 0):
        r = (int) ((-p+delta)/2)
        result = "Xn = C1*"+(str)(r)+"^n + C2*n*"+(str)(r)+"^n"
        return result
    elif(delta < 0):
        p = str(-1*p)
        a = str(2*a)
        result = "Xn = C1 * (("+p+" + i√"+str(delta)+")/"+a+") + C2 * (("+p+" - i√"+str(delta)+")/"+a+")"
        return result

print(getRoots(1,1,1))