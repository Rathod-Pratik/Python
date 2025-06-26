def f(a):
    less = []
    equal = []
    grater = []

    if len(a) > 1:
        p = a[0]
        for x in a:
            if x < p:
                less.append(x)
            elif x == p:
                equal.append(x)
            else:
                grater.append(x)
        return f(less) + equal + f(grater)
    else:
        return a

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
print(f(arr))