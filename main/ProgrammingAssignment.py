import math

def RootTwo():
    x0 = 1.5
    tol = 0.000001

    iter = 0
    diff = x0
    x = x0

    print(str(iter) + ' : ' + str(x))

    while (diff >= tol):
        iter += 1
        y = x

        x = (x/2.0)+(1.0/x)
        print(str(iter) + ' : ' + str(x))

        diff = abs(x-y)
    
    print("Convergence after " + str(iter) + " iterations.")


def BisectionMethod():
    x0 = 1.5
    tol = 1e-6

    iter = 0
    diff = x0
    x = x0
    print(str(iter) + ": " + str(x))
    while (diff >= tol):
        iter += 1
        y=x
        x = (x/2) + (1/x)
        print(str(iter) + ": " + str(x))
        diff = abs(x-y)
    print("Convergence after " + str(iter) + " iterations")

def FixedPointIteration():
    p0 = 1.5
    result = "Failure"
    tol = 1e-6
    N0 = 50

    i = 1
    p = 0

    while (i<=N0):
        # # a
        # p = p0 - p0*p0*p0 - 4*p0*p0 + 10

        # b
        p = math.sqrt(10-p0*p0*p0) / 2
        
        if math.isnan(p):
            print("Result diverges")
            break

        print(str(i) + ": " + str(p))

        if (abs(p-p0) < tol):
            result = "Success"
            break
        i+=1
        p0=p
    print(result + " after " + str(i) + " iterations")

def NewtonMethod():
    # #a
    # f = lambda x: -x*x*x-4*x*x+10
    # df = lambda x: -3 *x*x - 8*x
    
    #b
    f = lambda x: (math.sqrt(10 - x*x*x) / 2)-x
    df = lambda x: (-(3 * x*x) / (4 * math.sqrt(10-x*x*x))) -1
    found = False

    p_prev = math.pi/4
    tol = 1e-6
    N_0 = 1000

    i = 1
    while (i <= N_0):
        if (df(p_prev) != 0):
            p_next = p_prev - (f(p_prev) / df(p_prev))
            print(str(i) + ": " + str(p_next))
            if (abs(p_next-p_prev) < tol):
                print("Success after " + str(i) + " iterations")
                found = True
                break
            i += 1
            p_prev = p_next
        else:
            print("FAILED")
            print("DERIVATIVE IS ZERO")
            found = True
            break
    if not found:
        print("FAILED")
        print("MAX ITERATIONS PERFORMED")
    

if __name__=='__main__':
    print("Approximation Algorithm")
    RootTwo()
    print()
    print()
    print("The Bisection Algorithm")
    BisectionMethod()
    print()
    print()
    print("Fixed Point Algorithm")
    FixedPointIteration()
    print()
    print()
    print("Newton Raphson Method")
    NewtonMethod()
