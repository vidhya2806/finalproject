""" STUDENT DATALIST
Name: Vidhya
From: Bangalore, Karnataka, India"""
import sys
import csv

def main():
    check_command_line_arg()
# OPENING A CSV FILE AND READ THE CSV FILE
    data =[]
    try:
        with open(sys.argv[1],"r")as csvfile:
            reader=csv.DictReader(csvfile)
            for row in reader:
                split_name = row["name"].split(",")
                data.append({"first" :split_name[1].lstrip(), "last": split_name[0], "topics": row["topics"],"joining": row["joining"]})
                #print(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    #print(data)
# USING SELECT_DEPARTMENT FUNCTION INCLUDE A DEPARTMENT AND CURRENTYEAR OF STUDENT IN CSV FILE
    output=[]
    for row in data:
        department = select_department(row["topics"])
        currentyear =select_currentyear(row["joining"])
        #output.append(department)
        #output.append(currentyear)
        output.append({"first":row["first"], "last":row["last"],"topics":row["topics"],"department":department,"currentyear":currentyear,"joining":row["joining"]})
        #print(row)
    #print(output)

# WRITE A NEW AFTERSTUDENT.CSV FILE WITH FIRST , LAST NAME, TOPIC , DEPARTMENT, CURRENTYEAR, JOINING DATE OF STUDENT
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames =["first","last","topics","department","currentyear","joining"])
        writer.writerow({"first":"first","last":"last", "topics":"topics","department":"department", "currentyear":"currentyear","joining":"joining",})
        for row in output:
            writer.writerow({"first":row["first"], "last":row["last"],"topics":row["topics"],"department":row["department"],"currentyear":row["currentyear"],"joining":row["joining"]})
            #print(row)

# WRITE A FUNCTION TO SELECT A DEPARTMENT BASED ON THE CHAR IN THE LIST

def select_department(char):
    if char in ["Web Development","Programming","App Development"]:
        return "IT "
    elif char in ["Mobile Computing","Cloud Computing","Data Mining"]:
        return "CSE "
    elif char in ["Home Automation","Robotic"]:
        return "EEE "
    elif char in ["Integrated Circuit","Network Simulation","Image Processing"]:
        return "ECE "
    elif char in ["Electronic Power Steering","Automatic Gear Changer"]:
        return "ME "
    else:
        return "Other Department"

# WRITE A FUCTION TO CALCULATE CURRENT YEAR OF THE STUDENT

def select_currentyear(batch):
    currentyear =int(batch)-2018
    return  "year" + str(currentyear)

# WRITE A FUCTION TO CHECK NUMBER OF ARGUMENTS IN TERMINAL
# python project.py college_student.csv afterstudent.csv

def check_command_line_arg():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a csv file ")


if __name__=="__main__":
    main()
