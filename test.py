



def array_diff(a, b):
    #your code here
    outside = []
    for i in a:
        if i == b[0]:
            continue
        outside.append(i)

    return outside

name = array_diff([3, -3, -13, -19, 10, 8, -2, 3, 18], [-14, 20, -19, 7, -12, 5])
print(name)









