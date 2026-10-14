def isPerfectNumber(n):
    sum = 0
    og = n
    for i in range(1,n):
        if (n % i == 0):
            sum = sum + i
    return sum == og   