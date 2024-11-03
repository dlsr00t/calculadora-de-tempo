def timeCalc():
    print("\033[33mWARNING: if you dont specify the hours doing [m:s + m:s...]\nThe hours gon be set to 0\033[0m")

    numbers = input("Enter the the time u wanna calc in this model [hh:mm:ss + hh:mm:ss ...]: ")
    numbersOrganized = numbers.split("+")   

    for c in range(len(numbersOrganized)):
        numbersOrganized[c] = "".join(numbersOrganized[c].split())

    for c in range(len(numbersOrganized)):
        if numbersOrganized[c].count(":") == 0:
            return print("\n\n\n\033[1;31mERROR: YOU INSERTED VALUES IN A DIFFERENT EXPECTED MODEL1!!!\033[0m")
        elif numbersOrganized[c].count(":") == 1:
            numbersOrganized[c] = numbersOrganized[c].replace(numbersOrganized[c][0], "00:"+numbersOrganized[c][0], 1)
        #elif numbersOrganized[c].count(":") == 2 and numbersOrganized[c][1] == ":":
        #    numbersOrganized[c] = numbersOrganized[c].replace(numbersOrganized[c][0], "0"+numbersOrganized[c][0], 1)

    print(numbersOrganized)
    
    transformingIntoInt = []
    for c in range(len(numbersOrganized)):
        transformingIntoInt.append(numbersOrganized[c].split(":"))

    for c in range(len(transformingIntoInt)):
        for i in range(3):
            transformingIntoInt[c][i] = int(transformingIntoInt[c][i])

    for c in range(len(transformingIntoInt)):
            for i in range(len(transformingIntoInt[c])):
                if c!=0 and len(str(transformingIntoInt[c][i])) > 2:
                    print(str(transformingIntoInt[c]))
                    return print("\n\n\n\033[1;31mERROR: YOU INSERTED VALUES IN A DIFFERENT EXPECTED MODEL2!!!\033[0m")



    print(transformingIntoInt)
#   [[0, 3, 10], [0, 28, 12]]
     #0          #1
    result = [0,0,0]
    for c in range(len(transformingIntoInt)):
        for i in range(3):
            result[i] = result[i]+transformingIntoInt[c][i] 


    print(result)

timeCalc()









