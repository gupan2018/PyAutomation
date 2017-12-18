list = []

for i in range(0, 4):
    value = input("请输入分值:")
    value = float(value)
    list.append(value)

for i in range(0, 4):
    if (list[i] >= 90) & (list[i] <= 100):
        print("A+")
    elif (list[i] >= 80) & (list[i] < 90):
        print("A")
    elif (list[i] >= 70) & (list[i] < 80):
        print("B+")
    elif (list[i] >= 60) & (list[i] < 70):
        print("B")
    elif (list[i] < 60) & (list[i] >= 0):
        print("C")
    else:
        print("Error")