def kangaroo(x1, v1, x2, v2):
    if (v2 == v1):
        return "NO"
    elif (v1 > v2):
        if (x2 >= x1):
            if ((abs((x2-x1)/abs(v1-v2)) % 2 == 0) or (abs((x2-x1)/abs(v1-v2)) % 2 == 1)):
                return "YES"
            else:
                return "NO"
        else:
            return "NO"
    elif (v2 > v1):
        if (x1 >= x2):
            if ((abs((x2-x1)/abs(v2-v1)) % 2 == 0) or (abs((x2-x1)/abs(v2-v1)) % 2 == 1)):
                return "YES"
            else:
                return "NO"
        else:
            return "NO"

print(kangaroo(2564, 5393, 5121, 2836))