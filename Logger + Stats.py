#Health Management System Logger
#3 patients are required to log their food and physical exercises

def getdate():
    import datetime
    return datetime.datetime.now()

a = getdate()

print("Hey there! \n\tWelcome to Health Management System Logger\n\t  Instructions: Enter 1 for Harry, 2 for Rohan and 3 for Hammad in the input below.\n")
try:
    n= int(input("Input (1/2/3): "))
except ValueError:
    print("Enter either 1, 2 or 3!\n \t\t\t\t Please restart the program now!")
if n>3 or n<1:
        print("Enter only 1,2 or 3!")
else:
    print("\n\nSuccessfully Logged In! \n\nWhat do you want to do??\nPress 1 if you want to log, 2 for status.")

    try:
        q = int(input("\nInput (1/2): "))
    except ValueError:
        print("Enter either 1 or 2")
    if q<1 or q>2:
        print("Enter either 1 or 2")
    else:
        if q==1:
            print("\n\nEnter 1 to log diet, 2 for exercise.")
            try:
                l= int(input("\nInput (1/2): "))
            except ValueError:
                print("Enter either 1 or 2!\n \t\t\t\t Please restart the program now!")
            if n==1 and l==1:
                edit= input('Hi Harry! What did you eat?: ')
                op = open("Harry-Diet.txt","a")
                op.write(str(a) + "  :  " + edit + "\n")
                print("\nData Logged Successfully!!\n")
                op.close()
            elif n==1 and l==2:
                edit= input('Hi Harry! What exercise did you do?: ')
                op = open("Harry-Exercise.txt","a")
                op.write(str(a) + "  :  " + edit + "\n")
                print("\nData Logged Successfully!!\n")
                op.close()
            elif n == 2 and l == 1:
                edit = input('Hi Rohan! What did you eat?: ')
                op = open("Rohan-Diet.txt", "a")
                op.write(str(a) + "  :  " + edit + "\n")
                print("\nData Logged Successfully!!\n")
                op.close()
            elif n == 2 and l == 2:
                edit = input('Hi Rohan! What exercise did you do?: ')
                op = open("Rohan-Exercise.txt", "a")
                op.write(str(a) + "  :  " + edit + "\n")
                print("\nData Logged Successfully!!\n")
                op.close()
            elif n == 3 and l == 2:
                edit = input('Hi Hammad! What exercise did you do?: ')
                op = open("Hammad-Exercise.txt", "a")
                op.write(str(a) + "  :  " + edit + "\n")
                print("\nData Logged Successfully!!\n")
                op.close()
            elif n == 3 and l == 1:
                edit = input('Hi Hammad! What did you eat?: ')
                op = open("Hammad-Diet.txt", "a")
                op.write(str(a) + "  :  " + edit + "\n")
                print("\nData Logged Successfully!!\n")
                op.close()
            else:
                print("Some unexpected error occured! Please try again!")

        if q ==2:
            print("Input 1 for Diet Stats, 2 for Exercise.")
            try:
                st = int(input("Input (1/2): "))
            except ValueError:
                print("Enter either 1 or 2")
            if st < 1 or st > 2:
                print("Enter either 1 or 2")
            else:
                if n==1 and st ==1:
                    tr = open("Harry-Diet.txt","r")
                    print("Here are your current logs Harry- \n\n\t\t\t")
                    for j in tr.readlines():
                        print(j)
                    tr.close()
                elif n==2 and st ==1:
                    tr = open("Rohan-Diet.txt","r")
                    print("Here are your current logs Rohan- \n\n\t\t\t")
                    for j in tr.readlines():
                        print(j)
                    tr.close()
                elif n==3 and st ==1:
                    tr = open("Hammad-Diet.txt","r")
                    print("Here are your current logs Hammad- \n\n\t\t\t")
                    for j in tr.readlines():
                        print(j)
                    tr.close()
                elif n==1 and st ==2:
                    tr = open("Harry-Exercise.txt","r")
                    print("Here are your current logs Harry- \n\n\t\t\t")
                    for j in tr.readlines():
                        print(j)
                    tr.close()
                elif n==2 and st ==2:
                    tr = open("Rohan-Exercise.txt","r")
                    print("Here are your current logs Rohan- \n\n\t\t\t")
                    for j in tr.readlines():
                        print(j)
                    tr.close()
                elif n==3 and st ==2:
                    tr = open("Hammad-Exercise.txt","r")
                    print("Here are your current logs Hammad- \n\n\t\t\t")
                    for j in tr.readlines():
                        print(j)
                    tr.close()
                else:
                    print("Some unexpected error occured! Please retry!")
