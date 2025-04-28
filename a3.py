def CalcFactorial(n):
    print("the factorial of", n, "is")
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

y=input("enter the number tpo calculate factorial ")
z=int(y)
ans = CalcFactorial(z)
print(ans)
