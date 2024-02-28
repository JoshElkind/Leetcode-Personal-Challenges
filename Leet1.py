listinput = [2, 15, 11, 7]
check = False
targetinput = 9
list1 = []
output = []
for x in listinput:
    for y in list1:
        if y + x == targetinput:
            '''print("The two numbers are " + str(y) + " and " + str(x))'''
            check = True
            break
        else:
            pass
    if check == False:
        list1.append(x)
    else:
        break

ycount = 0
xcount = 0


count = -1
for z in listinput:
    count += 1
    if z == y and ycount == 0:
        '''print(str(y) + "'s index is " + str(count) + ".")'''
        ycount = 1
        ysum = count
    elif z == x and xcount == 0:
        '''print(str(x) + "'s index is " + str(count) + ".")'''
        xcount = 1
        xsum = count
        
    else:
        pass

    if xcount + ycount == 2:
        break

    else:
        pass


output.append(ysum)
output.append(xsum)
print(output)


'''

class Solution(object):
    def twoSum(nums,target):
        listinput = nums
        check = False
        targetinput = target
        list1 = []
        output = []
        for x in listinput:
            for y in list1:
                if y + x == targetinput:
                    '''print("The two numbers are " + str(y) + " and " + str(x))'''
                    check = True
                    break
                else:
                    pass
            if check == False:
                list1.append(x)
            else:
                break

        ycount = 0
        xcount = 0


        count = -1
        for z in listinput:
            count += 1
            if z == y and ycount == 0:
                '''print(str(y) + "'s index is " + str(count) + ".")'''
                ycount = 1
                ysum = count
            elif z == x and xcount == 0:
                '''print(str(x) + "'s index is " + str(count) + ".")'''
                xcount = 1
                xsum = count

            else:
                pass

            if xcount + ycount == 2:
                break

            else:
                pass


        output.append(ysum)
        output.append(xsum)
        print(output)

'''