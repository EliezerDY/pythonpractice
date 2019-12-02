def baseChange(n, b):
    if n < b:
        return str(n)
    return baseChange(n // b, b) + str(n % b)

print(baseChange(156,5))
print(baseChange(23,2))
