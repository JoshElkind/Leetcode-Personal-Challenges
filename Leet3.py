def solveLSWRC():
    input1 = input()
    list2 = ["null"]
    y = 1
    inc = 0
    length1 = ""
    check = False
    while y == 1:
        for z in list2:
            if input1[inc] == z:
                check = True
        if check == False:
            list2.append(input1[inc])
        inc += 1
        check = False
        if inc == len(input1):
            y = 0

    length1 = len(list2) - 1
    print(length1)

solveLSWRC()