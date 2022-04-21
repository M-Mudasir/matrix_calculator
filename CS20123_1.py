print('''\t\t\t|MATRIC CALCULATOR|
      \t\t\t**************************''')
import time

# for interface :)
#******************
while True:

    try:        #for mistake in the input :)
        while True:
            print('''\t\t\tOPERATIONS MENU
                  \t\t\t------------------------
1. ADDITION
2. SUBTRACTION
3. MULTIPLICATION
4. TRANSPOSE
5. Exit''')
            print()
            operation = int(input("Enter the index of operation that you want to perform : "))

        # for termination :)
        #*******************                        #please use the exit sequence atleast once :') 
            if operation == 5:
                for i in "exiting in 3 2 1 . . " :
                    time.sleep(0.27)
                    print(i,end="")
                break

        # for index out of range :)
        #***************************
            elif operation >5:
                print("Input a valid index")
                continue

        # for input :)
        #*************
            rows = int(input("Enter the no. of rows/column for the square matrix: "))
            if operation!=4:
                for i in range(1, 3):

                    print("ENTER VALUE FOR MATRIX :", i)
                    matrix = []
                    flag = 1
                    while flag:

                        for items in range(1, rows + 1):
                            print("Enter values for row", items, "separated by commas: ", end="")
                            values = input()
                            lvalues = values.split(',')  # converts string into list :)
                            if len(lvalues) == rows:
                                matrix.append(lvalues)  # adds the new list into original :)
                            else:
                                print("enter same numbers of column as in rows")
                                matrix.clear()  # clears the previous list :)
                                break
                            if items == rows:
                                flag = 0

                    print()
                    if i  == 1:
                        a = matrix  # stores first value :)
                    if i == 2:
                        b = matrix  # stores second value :)

        # for the special condition of transpose , such that only one matrix is offered for input :)
        #********************************************************************************************

            else:
                print("ENTER VALUE FOR THE MATRIX :")
                matrix = []
                flag = 1
                while flag:

                    for items in range(1, rows + 1):
                        print("Enter values for row", items, "separated by commas: ", end="")
                        values = input()
                        lvalues = values.split(',')  # converts string into list :)
                        if len(lvalues) == rows:
                            matrix.append(lvalues)  # adds the new list into original :)
                        else:
                            print("enter same numbers of column as in rows")
                            matrix.clear()  # clears the previous list :)
                            break
                        if items == rows:
                            flag = 0
                print()
                c = matrix  # stores  value of the matrix :)

        # *********************************************************
            # for a null matrix of n order :)
            # makes a row x row null matrix :)

            result = []
            for i in range(1, rows + 1):
                f = []
                result.append(f)  # [[],[],[]] :)
                for j in range(1, rows + 1):
                    f.append(0)
            # [[0,0,0],..] :)
        # *********************************************************

        # for addition :)
        #****************
            if operation == 1:
                for i in range(len(a)):  # accesses the main components of the list :)
                    for j in range(len(a[0])):  # accesses the components of the main components :)
                        result[i][j] = int(a[i][j]) + int(b[i][j])
                print("YOUR ANSWER :")
                for i in result:
                    for k in i:
                        print("\t", k, end=" ")
                    print()
                print()         #skips a line to give the user a cool interface :)

        # for subtraction :)
        #*******************
            elif operation == 2:
               for i in range(len(a)):
                    for j in range(len(a[0])):
                        result[i][j] = int(a[i][j]) - int(b[i][j])
               print("YOUR ANSWER :")
               for i in result:
                   for k in i:
                       print("\t", k, end=" ")
                   print()
               print()

        # for multiplication :)
        #**********************
            elif operation == 3:
                for i in range(len(a)):     #accesses rows :)
                    for j in range(len(a[0])):      #accesses components of a row :)
                        for k in range(len(a[0])):      #accesses components of a row, for the second time , for multiplication :)
                            result[i][j]+=int(a[i][k])*int(b[k][j])
                print("YOUR ANSWER :")
                for i in result:
                    for k in i:
                        print("\t", k, end=" ")
                    print()
                print()

        # for transpose :)
        #*****************
            elif operation == 4:
                for i in range(len(c)):
                    for j in range(len(c[0])):
                        result[j][i] = int(c[i][j])     #assigns row elements into column :)
                print("YOUR ANSWER :")
                for i in result:
                    for k in i:
                        print("\t", k, end=" ")
                    print()
                print()
    except ValueError:          #just to look over a silly mistake made by the user in the input :)
        print("I think, You made a mistake in the input  :)")
        continue
    break
