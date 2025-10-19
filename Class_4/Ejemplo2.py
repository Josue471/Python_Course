print("Ejemplo 2. Nested if else")
print("Special funtion()")
x = -10
if x<=-1:
    fx=1/x
    print("fx = ", fx, ", x = ", x, " and behaves like 1/x")
else:
    if -1<x and x<=10:
        print("fx = ", x, ", x = ", x, " and behaves like x")
    else:
        fx=x*x
        print("fx = ", fx, ", x = ", x, " and behaves like x^2")