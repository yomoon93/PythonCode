def doSomeMath(n):
    return (n+2) * 3 - 7

print([x+1 for x in range(1,10)])
print([el * 2 + 4 for el in range(1,20,2)])
print([doSomeMath(n) for n in range(1,10)])
print([n for n in range(1,20) if n < 9])