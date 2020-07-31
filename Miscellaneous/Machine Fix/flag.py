def flag(n):
    sum = 0
    while (n > 0):
        sum += n
        n //= 3
    return sum

print(flag(523693181734689806809285195318))