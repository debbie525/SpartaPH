import numpy as np
import pandas as pd

# Get the number of students in the class
stuNum = input('Please enter the number of students in your class: ')  # added, debbie

names = []
# get the names of the students
for i in range(0, int(stuNum)):
    names.append(input("Enter the name of student " + str(i+1) + ": "))
    print(names)

    # Create Pandas data frame to store the scores for students (initially filled with zeros) to hold students’ test scores
    stuGradesFrame = pd.DataFrame(np.zeros((int(stuNum), 4)))  # change string to int , stuNum

    # Print the contents of the dataframe before entering the scores
print("The data frame contents BEFORE entering the scores")

print(stuGradesFrame)  # added

    # Write a nested loop to get the scores for each student and store them in the data frame
for i in range(0, int(stuNum)):  # you need to complete the code  #added
    for j in range(0, 4):  # you need to complete the code  #added
        grade = input(("Enter the " + str(j+1)  + "test of student " + str(names[i]) + ": "))  # you need to complete the code  #added
        stuGradesFrame.loc[i,j]=grade

    stuGradesFrame.loc[i]=pd.to_numeric(stuGradesFrame.loc[i])
    stuGradesFrame['mean']=stuGradesFrame.iloc[:,0:4].mean(axis=1)


print("The data frame contents AFTER entering the scores")
print(stuGradesFrame)

#Create a list for letter grades
letterGrades = []

#Create a loop to check the average of grades for each student

for i in range (0,int(stuNum)) :
    if (stuGradesFrame['mean'][i] >= 90):
        letterGrades.append('A')
    if (stuGradesFrame['mean'][i] >=80 and stuGradesFrame['mean'][i] <=89):
        letterGrades.append('B')
    if (stuGradesFrame['mean'][i] >=70 and stuGradesFrame['mean'][i] <=79):
        letterGrades.append('C')
    if (stuGradesFrame['mean'][i] >=60 and stuGradesFrame['mean'][i] <=69):
        letterGrades.append('D')
    if (stuGradesFrame['mean'][i] >= 0 and stuGradesFrame['mean'][i] <= 59):
        letterGrades.append('F')

    #print(letterGrades)
    print ('the grade letter for student' + str(i+1) + ' ' + names[i] + ' who has average ' + str(stuGradesFrame['mean'][i]) + ' is ' +  letterGrades[i])




