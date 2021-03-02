def operation(a,b,op):
    count = 0
    if op == "add":
        count = add(a,b)
    print(count)


def add(a,b):
    return a + b

operation(4,5,"add")
