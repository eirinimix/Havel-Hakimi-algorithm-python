import numpy as np

stringInput = input('Give number array ex 2,1,4,5,6\n')
intArray = []
stringInput = stringInput.split(',')
gradeSum = 0;

for item in stringInput:
    tempVal = int(item)
    if tempVal < 0:
        print('This is not a graphic array.')
        break;
    gradeSum = gradeSum + tempVal
    intArray.append(tempVal)
if gradeSum % 2:
    print('This is not a graphic array.')
else:
    intArray = np.array(intArray)
    intArray.sort()
    for grade in intArray:
        if len(intArray) > 1:
            intArray = intArray[0: len(intArray) - 1]
            if len(intArray) >= grade:
                for i in range(grade):
                    intArray[len(intArray) - i - 1] = intArray[len(intArray) - i - 1] - 1
                    print(intArray, gradeSum)
        else:
            if intArray[0] == 0:
                print('I can create the graph')
            else:
                print('I can\'t create the graph')


print(intArray, gradeSum)
