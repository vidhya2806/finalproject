# STUDENT DATALIST
Video Demo :< (https://youtu.be/aYJj39LSSAc) >
#### Discription
    This Python code takes two CSV files as input, college_student.csv and afterstudent.csv. It reads the data from college_student.csv, processes the data, and then writes it into the afterstudent.csv file. The processed data includes the first name, last name, topics, department, current year, and joining date of the student.

#### Explaining the Project
-Creates an instance of csv.DictReader(csvfile) which is used to iterate through each row in the reader.Each iteration splits "name" into first and last parts using
```python
    split_name = row["name"].split(",")
```
#### Screenshot of College_student.csv File

![college_student.csv file ](Screenshot%20of%20intput%20collegestudentfile.png)


-It iterates each row's by calling print()data. Then we open csv file and read the content then create an empty list calle data. Then it loops through each row in reader object and append to datalist.
```python
    data.append({"first" :split_name[1].lstrip(), "last": split_name[0], "topics": row["topics"],"joining": row["joining"]})
```
-Finally we get a output of {first, last, topics,joining}

-Then we declare a emptylist called output.Then it iterates through the data & uses a function to select department of each row.
-It selects the current year for each student in that row using another function.Finally, it appends all of this information into an empty list called output which is finally printed out on screen.

Inside a for loop we use two funtions:
```python
    select_department()
    select_currentyear()
```
-This fuction take parameters from "topics" and "joining".We then append these values into our list with a function called append().-Then we created a list of all the department in the university and their student currentyear.
-After that write a program or script to open a file for writing with fieldname of first, last, topics, department, currentyear and joining of the student datalist.
```python
    with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames =["first","last","topics","department","currentyear","joining"])
    writer.writerow({"first":"first","last":"last", "topics":"topics","department":"department", "currentyear":"currentyear","joining":"joining",})
```
## Usage of read , write and append
-‘r’ – Read Mode: Read mode is used only to read data from the file.
-‘w’ – Write Mode: This mode is used when you want to write data into the file or modify it. Remember write mode overwrites the data
       present in the file.
-‘a’ – Append Mode: Append mode is used to append data to the file. Remember data will be appended at the end of the file pointer.


-This will iterate through each row in the output file create new rows by adding values to the respective fields thats are already present into the DictWriter
-It print out all the rows from input into output . And also it create a new csv file with the first and last name , topic, department , currentyear and joining date of the student.

ex: first,last,topics,department,currentyear,joining

The function called select_department . if the char in list of topics then it returns the respective department
```python
    def select_department(char):
        if char in ["Web Development","Programming","App Development"]:
            return "IT "
```
The function called select_currentyear() which calculate the currentyear of student based on value from year and it return currentyear of the student.
```python
    def select_currentyear(batch):
        currentyear =int(batch)-2018
        return  "year" + str(currentyear)
```
-The function check_command_line_arg is checking to make sure that the user has not passed in an invalid file type.
-If they have, then it will exit with a message saying "Too few command-line arguments",The code is also checking to see if the first argument is ".csv" and the second argument is ".csv", If either of these are true, then it will exit with a message saying "Not a csv file.".The code will exit the program if there are less than or more than three command-line arguments
```python
   def check_command_line_arg():
        if len(sys.argv)<3:
            sys.exit("Too few command-line arguments")
        if len(sys.argv)>3:
            sys.exit("Too many command-line arguments")
        if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
            sys.exit("Not a csv file ")
```
#### Screenshot of afterdtudent.csv file

![afterdtudent.csv file](Screenshot%20afterstudent.png)


## Installation

Visual Studio Code.Ink

Python 3.9(64-bit)

## Contribution

As a beginner at this project. I was responsible for conducting research on the project topic, analyzing data, and creating a new file on representations of our findings. My research contributed to the development of a new approach to the problem we were addressing, which led to a reduce the time consumption and increase user satisfaction ratings. Additionally, my data analysis helped us to identify key trends that informed our decision-making throughout the project. I worked closely with my ideas to ensure that our findings were integrated into our project plan. Overall, my contribution was critical to the success of the project, and I am proud to have been a beginner who did this project successfully."



# About myself

 Name: Vidhya

 From: Bangalore, Karnataka, India

 Mail: vidhya.dillu28@gmail.com

 Github: vidhya2806