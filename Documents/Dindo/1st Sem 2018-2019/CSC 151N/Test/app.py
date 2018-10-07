import csv
import fileinput
#with open('students.csv') as csvfile:
 #   student = csv.reader(csvfile)
  #  for row in student:
   #     print', '.join(row)

def menu():
    print("What to do: ")
    print("(1) Display - Display Students")
    print("(2) Add - Add Students")
    print("(3) Delete - Delete Students by ID")
    print("(4) Update - Update List")
    
def display():
    print("Current Students")
    with open('students.csv') as csvfile:
        student = csv.reader(csvfile)
        for row in student:
            print', '.join(row)
    csvfile.close() 
    
def add():
    choice= "yes"
    while(choice == "yes"):
        print("Input the Student's Information: ID Number, First Name, Last Name, Course, Year, Gender")
        with open('students.csv', 'a') as csvfile:
            studentwriter = csv.writer(csvfile)
            id_num = raw_input("ID Number: ")
            first_name = raw_input("First Name: ")
            last_name = raw_input("Last Name: ")
            course = raw_input("Course: ")
            year = raw_input("Year: ")
            gender = raw_input("Gender: ")
            studentwriter.writerow([id_num, first_name, last_name, course, year, gender])
        csvfile.close()
        choice = raw_input("Want to add more? [yes or no]: ")

def delete():
    choice = "yes"
    while(choice=="yes"):
        arr = []
        nput = raw_input("Input the ID Number: ")
        file = open('students.csv', 'r')
        for line in file:
            x = line.split(',')
            idnum = x[0]
            if idnum == nput:
                print "Deleted"
            else:
                arr.append(line)
                
                opt_del = open('students.csv', 'w')
                opt_del.writelines(arr)
                opt_del.close()
        choice = raw_input("Delete more? [yes or no]: ")

def update():
    select = "yes"
    while(select == "yes"):
        nput = raw_input("Enter ID no you want to update: ")
        file = open('students.csv','r')
        arr = []
        for line in file:
            x = line.split(',')
            idnum = x[0]
            if idnum == nput:
                print "result: "+line
                newinput = raw_input("What do you want to edit?: \n-idnumber, firstname, lastname, course, year, gender\n\n>>>")
                if newinput == "idnumber":
                    new_idnumber = raw_input("Enter changes: ")
                    arr.append(new_idnumber+','+x[1]+','+x[2]+','+x[3]+','+x[4]+','+x[5])
                elif newinput == "firstname":
                    new_fname = raw_input("Enter changes: ")
                    arr.append(x[0]+','+new_fname+','+x[2]+','+x[3]+','+x[4]+','+x[5])
                elif newinput == "lastname":
                    new_lname = raw_input("Enter changes: ")
                    arr.append(x[0]+','+x[1]+','+new_lname+','+x[3]+','+x[4]+','+x[5])
                elif newinput == "course":
                    new_course = raw_input("Enter changes: ")
                    arr.append(x[0]+','+x[1]+','+x[2]+','+new_course+','+x[4]+','+x[5])
                elif newinput == 'year':
                    new_year = raw_input("Enter changes: ")
                    arr.append(x[0]+','+x[1]+','+[2]+','+x[3]+','+new_year+','+x[5])
                elif newinput == 'gender':
                    new_gender = raw_input("Enter changes: ")
                    arr.append(x[0]+','+x[1]+','+x[2]+','+x[3]+','+x[4]+','+new_gender)
                    
            else:
                
                arr.append(line)
        file.close()
        opt_del = open('students.csv', 'w')
        opt_del.writelines(arr)
        opt_del.close()
    
        select = raw_input("Want to update another ID Number? [yes or no]: ")
            
    
menu()

while True:
    try:
        answer = int(raw_input("Type the number: "))
    except ValueError:
        print "Sorry that's not a number!"
        menu()
        continue

    else:
        if answer in range(1,5):
            if (answer == 1):
                display()
                menu()
            elif (answer == 2):
                add()
                menu()
            elif (answer == 3):
                delete()
                menu()
            elif (answer == 4):
                update()
                menu()
            elif (answer == 5):
                break
        else:
            print "Out of range! Make sure to type the correct number!"
            menu()
