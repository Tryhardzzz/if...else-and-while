#Name: Sariyah Motoda
#File name: while.py
#Description: Filter through names and GPA
last_name = "default"
while last_name != 'ZZZ':
    last_name = input("Enter the student's last name: ")
    if last_name == 'ZZZ':
        break
    first_name = input("Enter the student's first name: ")
    GPA = float(input("Enter the student's GPA: "))
    if GPA >= 3.5:
        print(first_name + " " + last_name + " has made the Dean's List")
    if GPA >= 3.25:
        print(first_name + " " + last_name + " has made the Honor Roll")
    