def f1(n):
    if n > 0:
        f1(n-1)
    print(n)

def f(a,b):
    assert (a != 0) & (b != 0), 'a ou b est un entier naturel nul'
    if b == 1:
        return a
    return a + f(a,b-1)

def f1iter(n):
    for i in range(n+1):
        print(i)

def puissance(x, n):
    p = 1
    for i in range(n):
        p = p * x
    return p

def f2():
    print("Hello")
    f2()    

def f3(n):
    if n <= 0:
        return 0
    else:
        print(n)
    return f3(n-1) 

def f4(n,m):
    if n == 0:
        return 0
    return m + f4(n-1,m)

def f5(n):
    if n == 0 or n == 1:
        return 1
    else:
        return f5(n-1) + f5(n-2)
    
def mult(n,m):
    if n == 0:
        return 0
    return m + mult(n-1,m)

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

def iterafact(n):
    if n == 0:
        return 1
    else:
        f = 1
        for k in range(2, n+1):
            f = f * k
        return f

def Fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)

def pgcd(a,b):
    while b != 0:
        reste = a % b 
        a = b
        b = reste
    return a

def pgcdrecur(n,m):
    assert (n != 0) and (m != 0), 'n ou m est un entier naturel nul'
    if n % m == 0:
        return m
    else:
        return pgcdrecur(m , n%m)

def pair(n:int):
    if n == 0:
        return True
    return impair(n-1)

def impair(n:int):
    if n == 0:
        return False
    return  pair(n - 1)


if __name__ == "__main__":
    print(impair(5))






    #f1(10)
    #f1iter(3)
    #f2()
    #print(f3(3))
    #print(f4(3,1))
    #print(fact(10))
    #print(Fibonacci(5))
    #print(pgcdrecur(12,8)) 
    
