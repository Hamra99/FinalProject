# Hamra Hussain 
# 2096123

# Importing required Libraries
import pandas as pd
import datetime

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

# creating a new dataframe which copies the roaster_df
scholarship_df = roaster_df

# converting the values of the Date Of Graduation column to datetime format
scholarship_df['Date Of Graduation']  = pd.to_datetime(roaster_df['Date Of Graduation'], format="%d/%m/%Y")

# drop the students who are having disciplinary actions in the scholarship dataframe
scholarship_df.drop(scholarship_df.index[scholarship_df['Disciplinary Action'] == 'Y'], inplace=True)

# drop the students who are have already graduated in the scholarship dataframe
scholarship_df.drop(scholarship_df.index[scholarship_df['Date Of Graduation'] > datetime.datetime.now()], inplace=True)

# drop the students who are have less than 3.8 GPA in the scholarship dataframe
scholarship_df.drop(scholarship_df.index[scholarship_df['GPA'] < 3.8], inplace=True)

# dropping the not required columns, here axis=1 means that the columns are dropped and inplace=True means that the columns are dropped in the original dataframe
scholarship_df.drop(['Date Of Graduation', 'Disciplinary Action'], axis = 1, inplace=True)

# rearranging the coloumns of the dataframe to match the output order
scholarship_df.insert(2, 'Last Name', scholarship_df.pop('Last Name'))
scholarship_df.insert(3, 'Major', scholarship_df.pop('Major'))

# saving the dataframe by the specified name in an output folder. index= False means that the index is not included in the output file.
scholarship_df.to_csv('./output/ScholarshipCandidates.csv', index=False)