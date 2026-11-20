
# Exercise 3 - Student Manager
# This program allows users to view and manage student records.
# Prompt I used: Guide me to develop a Tkinter Student Manager application based on the assessment requirements, with the help of our Python lectures and W3Schools for additional guidance.
# ChatGPT was used for coding assistance and explanations of parts I did not fully understand.
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# This one creates the main window.
root = Tk()
root.title("Student Manager")
root.geometry("1199x674")
root.resizable(0, 0)

# This one sets the window icon, I used Keroppi also to match my background.
root.iconbitmap(r"C:\Users\Ken\OneDrive\Desktop\CodeLab ll Assessment 1\Exercise 3_Student_Manager\Pochacco.ico")

# This one loads the Pochacco background image.
bgImage = Image.open(r"C:\Users\Ken\OneDrive\Desktop\CodeLab ll Assessment 1\Exercise 3_Student_Manager\Pochacco.jpg")
bgImage = bgImage.resize((1199, 674))
bgPhoto = ImageTk.PhotoImage(bgImage)

# This one displays the background image.
bgLabel = Label(root, image=bgPhoto)
bgLabel.place(x=0, y=0)
bgLabel.lower()

# This one opens the student marks file and reads all the information inside it.
file = open(r"C:\Users\Ken\OneDrive\Desktop\CodeLab ll Assessment 1\Exercise 3_Student_Manager\studentMarks.txt", "r")
lines = file.readlines()
file.close()

# This gets the number of students from the first line of the file.
numberOfStudents = int(lines[0])

# This list stores all the student records.
students = []

# This goes through each student record in the file.
for line in lines[1:]:
    data = line.strip().split(",")

    # This stores each student's information in a list.
    student = [
        int(data[0]),
        data[1],
        int(data[2]),
        int(data[3]),
        int(data[4]),
        int(data[5])
    ]

    students.append(student)


# This function adds the three coursework marks together.
def courseworkTotal(student):
    return student[2] + student[3] + student[4]


# This function calculates the student's overall percentage.
def overallPercentage(student):
    total = courseworkTotal(student) + student[5]
    return (total / 160) * 100


# This function checks the percentage and gives the student a grade.
def studentGrade(percentage):
    if percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


# This function puts all the student's results together.
def displayStudent(student):
    coursework = courseworkTotal(student)
    percentage = overallPercentage(student)
    grade = studentGrade(percentage)

    result = (
        "Student Name: " + student[1] +
        "\nStudent Number: " + str(student[0]) +
        "\nCoursework Total: " + str(coursework) +
        "\nExam Mark: " + str(student[5]) +
        "\nOverall Percentage: " + format(percentage, ".2f") + "%" +
        "\nGrade: " + grade
    )

    return result


# This function displays all the student records.
def viewAllStudents():
    results = ""
    totalPercentage = 0

    # This goes through all the students and displays their results.
    for student in students:
        results = results + displayStudent(student) + "\n\n"
        totalPercentage = totalPercentage + overallPercentage(student)

    # This calculates the average percentage of the whole class.
    average = totalPercentage / numberOfStudents

    results = results + "Number of Students: " + str(numberOfStudents)
    results = results + "\nClass Average: " + format(average, ".2f") + "%"

    # This clears the previous results and displays the new ones.
    resultLabel.delete("1.0", END)
    resultLabel.insert(END, results)


# This function allows the user to search for a student using their student number.
def viewIndividualStudent():
    studentNumber = searchEntry.get()

    # This checks if the entered student number matches a record.
    for student in students:
        if str(student[0]) == studentNumber:
            resultLabel.delete("1.0", END)
            resultLabel.insert(END, displayStudent(student))
            return

    # This shows an error if the student number cannot be found.
    messagebox.showerror("Error", "Student not found.")


# This function finds the student with the highest overall percentage.
def highestStudent():
    highest = students[0]

    # This compares the percentages to find the highest one.
    for student in students:
        if overallPercentage(student) > overallPercentage(highest):
            highest = student

    resultLabel.delete("1.0", END)
    resultLabel.insert(END, displayStudent(highest))


# This function finds the student with the lowest overall percentage.
def lowestStudent():
    lowest = students[0]

    # This compares the percentages to find the lowest one.
    for student in students:
        if overallPercentage(student) < overallPercentage(lowest):
            lowest = student

    resultLabel.delete("1.0", END)
    resultLabel.insert(END, displayStudent(lowest))


# This one creates the heading of the program.
heading = Label(root, text="Student Manager",
                font=("Cute Dino", 24),
                bg="#9FC0D7",
                fg="#344F68")
heading.pack(pady=10)

# This button displays all the student records.
allButton = Button(root, text="1. View All Student Records",
                   command=viewAllStudents,
                   font=("Cute Dino", 13),
                   bg="#DCEAF4",
                   fg="#344F68",
                   activebackground="#759DBB",
                   activeforeground="#FFFFFF",
                   relief="flat",
                   cursor="hand2")
allButton.pack(pady=3)

# This label tells the user to enter a student number.
searchLabel = Label(root, text="Enter Student Number:",
                    font=("Cute Dino", 13),
                    bg="#9FC0D7",
                    fg="#344F68")
searchLabel.pack(pady=3)

# This is where the user types a student number.
searchEntry = Entry(root,
                    font=("Arial", 11),
                    bg="#FFFFFF",
                    fg="#344F68",
                    insertbackground="#344F68",
                    relief="flat")
searchEntry.pack(pady=3)

# This button displays the selected student's record.
individualButton = Button(root, text="2. View Individual Student Record",
                          command=viewIndividualStudent,
                          font=("Cute Dino", 13),
                          bg="#DCEAF4",
                          fg="#344F68",
                          activebackground="#759DBB",
                          activeforeground="#FFFFFF",
                          relief="flat",
                          cursor="hand2")
individualButton.pack(pady=3)

# This button displays the student with the highest score.
highestButton = Button(root, text="3. Show Highest Total Score",
                       command=highestStudent,
                       font=("Cute Dino", 13),
                       bg="#DCEAF4",
                       fg="#344F68",
                       activebackground="#759DBB",
                       activeforeground="#FFFFFF",
                       relief="flat",
                       cursor="hand2")
highestButton.pack(pady=3)

# This button displays the student with the lowest score.
lowestButton = Button(root, text="4. Show Lowest Total Score",
                      command=lowestStudent,
                      font=("Cute Dino", 13),
                      bg="#DCEAF4",
                      fg="#344F68",
                      activebackground="#759DBB",
                      activeforeground="#FFFFFF",
                      relief="flat",
                      cursor="hand2")
lowestButton.pack(pady=3)

# This one creates the text area where the student results are displayed.
resultLabel = Text(root, height=12, width=75,
                   font=("Arial", 11),
                   bg="#FFFFFF",
                   fg="#344F68",
                   insertbackground="#344F68",
                   wrap=WORD,
                   relief="flat")
resultLabel.pack(pady=10)

# This displays the starting message when the program opens.
resultLabel.insert(END, "Choose an option above.")

# This keeps the window running.
root.mainloop()
