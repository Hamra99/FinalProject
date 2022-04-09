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

# creating a new dataframe by creating a copy of teh roaster_df by reordering the coloumn orders. Here copy() is used to copy the roaster_df dataframe. 
disciplined_df = roaster_df[['Student ID', 'Last Name', 'First Name', 'Date Of Graduation', 'Disciplinary Action']].copy()

# converting the values of the Date Of Graduation column to datetime format
disciplined_df['Date Of Graduation']  = pd.to_datetime(disciplined_df['Date Of Graduation'], format="%d/%m/%Y")

# dropping the students who does not have a disciplinary record
disciplined_df.drop(disciplined_df.index[disciplined_df['Disciplinary Action'] != 'Y'], inplace=True)

# dropping the not required columns, here axis=1 means that the columns are dropped and inplace=True means that the columns are dropped in the original dataframe
disciplined_df.drop(['Disciplinary Action'], axis = 1, inplace=True)

# sort the records based on the Date of Graduation in ascending order. inplace = True means that the changes are made in the original dataframe.
disciplined_df.sort_values(by = 'Date Of Graduation', inplace=True)

# saving the dataframe by the specified name in an output folder. index= False means that the index is not included in the output file.
disciplined_df.to_csv('./output/DisciplinedStudents.csv', index=False)