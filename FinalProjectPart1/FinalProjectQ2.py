# Hamra Hussain 
# 2096123

# Importing required Libraries
import pandas as pd

# importing all the csv files as pandas dataframes 
students_major = pd.read_csv("StudentsMajorsList.csv", names = ['Student ID', 'First Name', 'Last Name', 'Major', 'Disciplinary Action'])

students_gpa = pd.read_csv("GPAList.csv", names = ['Student ID', 'GPA'])

students_dog = pd.read_csv("GraduationDatesList.csv", names = ['Student ID','Date Of Graduation'])

# merging all the datframes to a single roster dataframe on the basis of the Student ID coloumn which is unique to each record
roaster_df = pd.merge(students_major, students_gpa, on="Student ID")

roaster_df =  pd.merge(roaster_df, students_dog, on="Student ID")

# rearranging the coloumns of the dataframe to match the output order
roaster_df.insert(1, 'Major', roaster_df.pop('Major'))
roaster_df.insert(6, 'Disciplinary Action', roaster_df.pop('Disciplinary Action'))

# sort the records based on the Last Name in ascending order. inplace = True means that the changes are made in the original dataframe.
roaster_df.sort_values(by = 'Last Name', inplace=True)

# getting the unique majors available in the dataframe. list() converts the series into a simple python list to iterate on
majors_list = list(roaster_df['Major'].unique())
print(majors_list)

# saving a csv for each major in the majors_list
for i in majors_list:
    # creating a new dataframe for each major in the majors_list
    sub_df = roaster_df[roaster_df['Major']==i]

    # dropping the not required columns, here axis=1 means that the columns are dropped and inplace=True means that the columns are dropped in the original dataframe
    sub_df.drop(['Major', 'GPA'], axis = 1, inplace=True)

    # sort the records based on the Student ID in ascending order. inplace = True means that the changes are made in the original dataframe.
    sub_df.sort_values(by = 'Student ID', inplace=True)

    # rearranging the coloumns of the dataframe to match the output order
    sub_df.insert(1, 'Last Name', sub_df.pop('Last Name'))

    # creating the name of the csv file dynamically using the name of the major.
    path = "./output/"+i.replace(" ", "")+"Students.csv"

    # saving the dataframe by the specified name in an output folder. index= False means that the index is not included in the output file.
    sub_df.to_csv(path, index=False)