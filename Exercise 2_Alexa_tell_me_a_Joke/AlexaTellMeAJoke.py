# Exercise 2 - Alexa Tell Me a Joke
# I used W3school for the codes, though the lecture did tackle it especially the tkinter and the file handling but I used W3Schools for extra guidance throughout the code.
# ChatGPT is used also for assistance and slight explanation on what i kind of not understand.
# Prompt used: Guide me to develop a TKinter GUI Application named, Alexa Tell Me A Joke based on the assessments requirements with the guide of our Python Lectures and the online resource that I used which is the W3Schools.
import tkinter as tk
from PIL import ImageTk, Image
import random


# This one creates the main window
root = tk.Tk()
root.title("Alexa Tell Me a Joke")
root.geometry("735x418")
root.resizable(0, 0)

# This one sets the window icon, I used Keroppi also to match my background.
root.iconbitmap(r"C:\Users\Ken\OneDrive\Desktop\CodeLab ll Assessment 1\Exercise 2_Alexa_tell_me_a_Joke\Keroppi frame.ico")

# This one loads the background image which is a Keroppi-themed window.
bgImage = Image.open(r"C:\Users\Ken\OneDrive\Desktop\CodeLab ll Assessment 1\Exercise 2_Alexa_tell_me_a_Joke\Keroppi.jpg")
bgImage = bgImage.resize((735, 418))

bgPhoto = ImageTk.PhotoImage(bgImage)

# This one displays the background image I used.
bgLabel = tk.Label(root, image=bgPhoto)
bgLabel.place(x=0, y=0)
bgLabel.lower()

# This one opens the file that is in the GitHub resources, which is the Random Jokes file. I transferred the file inside Exercise 2's file so the studio extension can recognize it.
file = open(r"C:\Users\Ken\OneDrive\Desktop\CodeLab ll Assessment 1\Exercise 2_Alexa_tell_me_a_Joke\randomJokes.txt", "r")
jokes = file.readlines()
file.close()

# This one stores the current joke displayed on the screen.
currentJoke = ["", ""]

# This one selects a single random joke out of 37 jokes given on the text file.
def tellJoke():
    joke = random.choice(jokes)

    # This one separates the setup and punchline.
    parts = joke.strip().split("?", 1)

    currentJoke[0] = parts[0] + "?"
    currentJoke[1] = parts[1]

    # This one displays the setup
    setupLabel.config(text=currentJoke[0])

    # This one defers the punchline until it is clicked by the user.
    punchlineLabel.config(text="")

# This is where the punchline gets functioned or displayed on the screen.
def showPunchline():
    punchlineLabel.config(text=currentJoke[1])

# This one allows the user to choose another random joke, just in case it repeated the same one, and want to hear another joke.
def nextJoke():
    tellJoke()

# This one is on how the joke is labeled and setup. I used a customized font and matched its color to the theme im going.
setupLabel = tk.Label(root, text="Click the button to hear a joke!",
                      wraplength=450,
                      font=("Cute Dino", 20),
                      bg="#F5F0DF",
                      fg="#526B45")
setupLabel.pack(pady=30)

# This one is on how the punchline is labeled and setup. I also used a customized font here and its colors.
punchlineLabel = tk.Label(root, text="",
                          wraplength=450,
                          font=("Cute Dino", 16),
                          bg="#F5F0DF",
                          fg="#75664F")
punchlineLabel.pack(pady=15)

# This button selects a random joke from the 37 given jokes inside the text file. Same fonts and theme to match.
jokeButton = tk.Button(root, text="Alexa tell me a Joke",
                       command=tellJoke,
                       bg="#A8B99A",
                       fg="#40543A",
                       font=("Cute Dino", 14),
                       activebackground="#8FA581",
                       activeforeground="#FFFFFF",
                       relief="flat",
                       cursor="hand2")
jokeButton.pack(pady=5)

# This one reveals the jokes' punchline. The punchline remains hidden until it is clicked or prompted by this one. Same fonts and theme to match.
punchlineButton = tk.Button(root, text="Show Punchline",
                            command=showPunchline,
                            bg="#A8B99A",
                            fg="#40543A",
                            font=("Cute Dino", 14),
                            activebackground="#8FA581",
                            activeforeground="#FFFFFF",
                            relief="flat",
                            cursor="hand2")
punchlineButton.pack(pady=5)

# This one is where the user can click next and if they want to hear another joke. Same fonts and theme to match.
nextButton = tk.Button(root, text="Next Joke",
                       command=nextJoke,
                       bg="#A8B99A",
                       fg="#40543A",
                       font=("Cute Dino", 14),
                       activebackground="#8FA581",
                       activeforeground="#FFFFFF",
                       relief="flat",
                       cursor="hand2")
nextButton.pack(pady=5)

# This one is a Quit Button on where users can click Quit, once clicked, the program stops. Same fonts and theme to match.
# # Destroy is used to close the Tkinter window and stop the program when the user clicks the Quit button.
quitButton = tk.Button(root, text="Quit",
                       command=root.destroy,
                       bg="#A8B99A",
                       fg="#40543A",
                       font=("Cute Dino", 14),
                       activebackground="#8FA581",
                       activeforeground="#FFFFFF",
                       relief="flat",
                       cursor="hand2")
quitButton.pack(pady=5)

# Keeps the window running
root.mainloop()
