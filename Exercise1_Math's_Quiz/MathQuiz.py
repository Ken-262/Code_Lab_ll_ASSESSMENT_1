# Exercise 1 - Maths Quiz
# Code structure based on the Python GUI lecture.
# I used ChatGPT for coding guidance and explanations, but not all of it is AI-Generated. I only used it for explanations and guidance.
# I got the codes from the Python GUI Lecture and the W3schools website. I also used ChatGPT to help me understand the codes and how they work.
# This is the link of where I got some of the codes: https://www.w3schools.com/python/default.asp (Its the homepage of the Python Section, I just navigated it to the sides on where I needed to get the codes.)
# Prompt I used: Help me develop a Tkinter Maths Quiz based on the assessment requirements, with the help of our lecture and the online source I used.
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# This one creates the main window
root = tk.Tk()
root.title("Maths Quiz")
root.geometry("600x450")
root.resizable(0, 0)

# This one changes the Tkinter window icon. I changed it to Gudetama to match the quiz's theme.
root.iconbitmap(r"C:\Users\Ken\OneDrive\Desktop\CodeLab ll Assessment 1\Exercise1_Math's_Quiz\Gudetama frame.ico")

# This frame holds the different screens.
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# This one loads the Gudetama background image that I imported to my laptop.
img = Image.open(r"C:\Users\Ken\OneDrive\Desktop\CodeLab ll Assessment 1\Exercise1_Math's_Quiz\Gudetama BG.jpg")

# This one resizes the image to fit the window and to not make the background or frame look stretched.
resized_img = img.resize((600, 450))

# This one converts the image so Tkinter can recognize it and then display it.
bg_image = ImageTk.PhotoImage(resized_img)

# This one creates a label to display the background image.
bg_label = tk.Label(main_frame, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# This one keeps the background behind the other widgets.
bg_label.lower()


def deletePages():
    # This one removes the widgets from the current screen in order to proceed to the next one.
    for widget in main_frame.winfo_children():

        # This one keeps the background image when changing screens.
        if widget != bg_label:
            widget.destroy()


# This one generates numbers depending on the difficulty.
def randomInt(difficulty):
    if difficulty == "Easy":
        return random.randint(1, 9)
    elif difficulty == "Moderate":
        return random.randint(10, 99)
    else:
        return random.randint(1000, 9999)


# This one randomly chooses addition or subtraction.
def decideOperation():
    return random.choice(["+", "-"])


# This one displays the section of difficulty menu where players can choose the difficulty of their Math Quiz.
def displayMenu():
    global score, question_number, attempts

    score = 0
    question_number = 0
    attempts = 0

    deletePages()

    title = tk.Label(
        main_frame,
        text="Maths Quiz",
        font=("Cute Dino", 28),
        bg="#FFFDF2",
        fg="#795C36",
        bd=3,
        relief="solid",
        padx=15,
        pady=5
)
    title.pack(pady=25)

    instruction = tk.Label(
        main_frame,
        text="Choose your difficulty:",
        font=("Cute Dino", 16),
        bg="#FFFDF2",
        fg="#795C36",
        bd=2,
        relief="solid",
        padx=10,
        pady=5
)
    instruction.pack(pady=10)

        # This one creates the Easy difficulty button.
    tk.Button(
        main_frame,
        text="Easy",
        font=("Cute Dino", 18),
        bd=3,
        relief="raised",
        bg="#F6D76B",
        fg="#795C36",
        activebackground="#EAC653",
        command=startEasy
    ).pack(pady=5)

    # This one creates the Moderate difficulty button.
    tk.Button(
        main_frame,
        text="Moderate",
        font=("Cute Dino", 18),
        bd=3,
        relief="raised",
        bg="#F6D76B",
        fg="#795C36",
        activebackground="#EAC653",
        command=startModerate
    ).pack(pady=5)

    # This one creates the Advanced difficulty button.
    tk.Button(
        main_frame,
        text="Advanced",
        font=("Cute Dino", 18),
        bd=3,
        relief="raised",
        bg="#F6D76B",
        fg="#795C36",
        activebackground="#EAC653",
        command=startAdvanced
    ).pack(pady=5)


# These functions work on how difficult the quiz is gonne be.
def startEasy():
    startQuiz("Easy")


def startModerate():
    startQuiz("Moderate")


def startAdvanced():
    startQuiz("Advanced")


# This starts the quiz once a player chose their desired difficulty. Global is used to ensure that the variables applied can be used in other functions.
def startQuiz(difficulty):
    global current_difficulty
    global score, question_number
    global question_label, answer_entry

    current_difficulty = difficulty
    score = 0
    question_number = 0

    deletePages()

    question_label = tk.Label(
        main_frame,
        text="",
        font=("Cute Dino", 22),
        bg="#FFFDF2",
        fg="#795C36",
        bd=3,
        relief="solid",
        padx=20,
        pady=10
)
    question_label.pack(pady=30)

    # This is where the player types their answer. Entry is used to create a message box where the player's can put their answer on a question.

    answer_entry = tk.Entry(
    main_frame,
    font=("Cute Dino", 18),
    justify="center",
    bd=3,
    relief="solid",
    bg="#FFFDF2",
    fg="#795C36"
    )
    answer_entry.pack(pady=10)

    tk.Button(
        main_frame,
        text="Submit Answer",
        font=("Cute Dino", 18),
        bd=3,
        relief="raised",
        bg="#F6D76B",
        fg="#795C36",
        activebackground="#EAC653",
        activeforeground="#795C36",
        command=checkAnswer
    ).pack(pady=15)

    displayProblem()


# This one is used to create the equations and display them on the player's screen. It also shows the correct answer and the points.
def displayProblem():
    global num1, num2, operation
    global correct_answer, attempts

    if question_number >= 10:
        displayResults()
        return

    attempts = 0

    num1 = randomInt(current_difficulty)
    num2 = randomInt(current_difficulty)

    operation = decideOperation()

    # This one makes sure subtraction does not give a negative answer
    if operation == "-" and num1 < num2:
        num1, num2 = num2, num1

    # This one calculates the correct answer
    if operation == "+":
        correct_answer = num1 + num2
    else:
        correct_answer = num1 - num2

    question_label.config(
        text="Question " + str(question_number + 1) +
        " of 10\n\n" + str(num1) + " " +
        operation + " " + str(num2) + " = ?"
    )

    # This one clears the previous answer and makes sure that the player can input another answer.
    answer_entry.delete(0, tk.END)


# This one checks IF player's the answer is correct
def isCorrect(user_answer):
    return user_answer == correct_answer


# This one checks the player's answer
def checkAnswer():
    global score, attempts, question_number

    answer = answer_entry.get()

    # Change the entered answer into a number
    user_answer = int(answer)

    if isCorrect(user_answer):

        # This one gives 10 points for the first correct attempt.
        if attempts == 0:
            score = score + 10
            messagebox.showinfo(
                "Correct!",
                "Correct answer! You earned 10 points."
            )

        # This one gives 5 points for the second correct attempt.
        else:
            score = score + 5
            messagebox.showinfo(
                "Correct!",
                "Correct answer! You earned 5 points."
            )

        question_number = question_number + 1
        displayProblem()

    else:

        # This one gives the player another chance if they fail.
        if attempts == 0:
            attempts = 1
            messagebox.showinfo(
                "Try Again",
                "That answer is incorrect. You have one more attempt."
            )
            answer_entry.delete(0, tk.END)

        # This one moves to the next question if the second attempt is wrong.
        else:
            messagebox.showinfo(
                "Incorrect",
                "The correct answer was " + str(correct_answer) + "."
            )

            question_number = question_number + 1
            displayProblem()


# This one displays the final score and grade that the player accumulated.
def displayResults():
    deletePages()

    title = tk.Label(
        main_frame,
        text="Quiz Results",
        font=("Cute Dino", 28),
        bg="#FFFDF2",
        fg="#795C36",
        bd=3,
        relief="solid",
        padx=15,
        pady=5
    )
    title.pack(pady=25)

    # This is the criteria that decides the grade based on the player's score.
    if score > 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    result_label = tk.Label(
        main_frame,
        text="Your score: " + str(score) + "/100\n\nGrade: " + grade,
        font=("Cute Dino", 22),
        bg="#FFFDF2",
        fg="#795C36",
        bd=2,
        relief="solid",
        padx=15,
        pady=10
    )
    result_label.pack(pady=20)

    # This one asks the player if they want to play again.
    play_again = messagebox.askyesno(
        "Play Again",
        "Do you want to play another quiz?"
    )

    if play_again:
        displayMenu()
    else:
        root.destroy()


# This one displays the menu once the program runs.
displayMenu()

root.mainloop()