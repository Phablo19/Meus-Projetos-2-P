def fibonacci(num):
    if num == 1 or num ==0:
        return 1
    else:
       return num * fibonacci(num - 1)
res = fibonacci(8)
print(res)