# Hamra Hussain 
# 2096123

# importing libraries
import datetime

# creating the roster dictionary that takes all the details from the csv files and combines them into one dictionary
def create_roster():
    # initialize the dictionary
    roster_dict = {}

    # open the majors csv file and read the data
    with open("StudentsMajorsList(1).csv","r") as f:
        for line in f:
            if (line[:-2] == "Y"):
                roster_dict[line.split(",")[0]] = line[0:-2]+"Y"
            elif (line[:-2] != "Y"):
                roster_dict[line.split(",")[0]] = line[0:-1]+"N"

    # open the grades csv file and read the data and add it to the dictionary
    with open("GPAList(1).csv","r") as f:
        for line in f:
            k = line.split(",")[0]
            roster_dict[k] += "," + line[7:-1]

    # open the attendance csv file and read the data and add it to the dictionary
    with open("GraduationDatesList(1).csv","r") as f:
        for line in f:
            k = line.split(",")[0]
            roster_dict[k] += "," + line[7:-1]

    # return the dictionary
    return roster_dict

# functions to get majors available in the csv files
def get_majors():
    majors = []
    with open("StudentsMajorsList(1).csv","r") as f:
        for line in f:
            majors.append(line.split(",")[3])
    return list(set(majors))

# a helper function to check if a number is float or not
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# a helper function to check if a date is greater or smaller than curent date
def checkDate(date):
    date_check = datetime.datetime.strptime(date, '%m/%d/%Y')
    if (date_check > datetime.datetime.now()):
        return True
    else:
        return False

# main function starts
if __name__ == "__main__":

    # create the roster dictionary and getting the majors
    k = create_roster()
    # print(k)
    majors = get_majors()
    # print(majors)

    # getting the input from the user for infinite times
    while True:

        print()
        # print the menu and getting input form the user
        query = input("Enter your Query or type 'q' to quit: ")
        
        # if the user enters q then quit the program
        if query == "q":
            break

        # splitting the query to check which words and numbers and which are not needed
        q = query.split()

        # getting all the words avialable in the majors
        words = " ".join(majors).split()  
        # print(words)  
        

        # checking if a word is a major or a float or not, if not remove it from the query
        for i in q:
            if (i not in words and isfloat(i) == False):
                q.remove(i)

        # removing all the redundant words if any 
        q1 = []
        flag_gpa = False
        for i in range(len(q)):
            if (q[i] in words):
                q1.append(q[i])
            if (isfloat(q[i]) == True):
                if flag_gpa == False:
                    q1.append(q[i])
                    flag_gpa = True
            
        # print(words)
        # print(q)
        # print(q1)

        # further refining all the redundant floats if any and removing them from the query
        gpa = 0.0
        for i in q1:
            if (isfloat(i)):
                gpa = float(i)
                q1.remove(i)

        q1 = " ".join(q1)
        # print(gpa)
        # print(q1)      

        # checking if the major exists or not, if not agin ask for the query after saying so such student
        if (q1 not in majors):
            print("No such student")
            continue

        stu_avialable = False

        students_done = []

        # checking if the student is available or not who is not having a disciplinary action not have passed till now and has the major in the query. Also here we check for student having the gpa within 0.1 of the query gpa
        print("Your student(s):")
        for i in k.values():
            j = i.split(",")
            if (j[3] == q1 and j[4] == "N" and checkDate(j[6])):
                if (float(j[5])> gpa-(0.1*gpa) and float(j[5])< gpa+(0.1*gpa)):
                    stu_avialable = True
                    students_done.append(j[0])
                    print(f"SID: {j[0]}, First Name: {j[1]}, Last Name: {j[2]}, GPA: {j[5]}")
        print()

        # checking if the student is available or not who is not having a disciplinary action not have passed till now and has the major in the query. Also here we check for student having the gpa within 0.1 of the query gpa
        print("You may, also, consider:")
        for i in k.values():
            j = i.split(",")
            if (j[3] == q1 and j[4] == "N" and checkDate(j[6]) and j[0] not in students_done):
                if (float(j[5])> gpa-(0.25*gpa) and float(j[5])< gpa+(0.25*gpa)):
                    stu_avialable = True
                    print(f"SID: {j[0]}, First Name: {j[1]}, Last Name: {j[2]}, GPA: {j[5]}")
        print()

        # if no student is avialable within 0.1 of the gpa and 0.25 of the gpa then print the student with the nearest gpa 
        if (stu_avialable == False):
            print("Student with closest GPA:")
            student = []
            gpa_diffs = []
            for i in k.values():
                j = i.split(",")
                if (j[3] == q1 and j[4] == "N" and checkDate(j[6])):
                    student.append([j[0], j[1], j[2], j[5]])
                    gpa_diffs.append(abs(float(j[5])-gpa))
            idx = gpa_diffs.index(min(gpa_diffs))
            print(f"SID: {student[idx][0]}, First Name: {student[idx][1]}, Last Name: {student[idx][2]}, GPA: {student[idx][3]}")        



