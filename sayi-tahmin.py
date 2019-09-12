#Credit: @sumedhaj9 https://github.com/sumedhaj9
import random

try:
    # python 2
    from Tkinter import *
except ImportError:
    # user is running python 3
    from tkinter import *

# Guessing Numbers (Lower & upper limit)
MAX = 10
MIN = 1



class Application(Frame):
    """The GUI application (Guess My Number)."""

    def __init__(self, master):
        """Initialize Frame."""
        Frame.__init__(self, master)
        #master.minsize(width=400, height=200)
        master.maxsize(width=400, height=200)
        self.grid()

        self.create_widgets()

        # Random number to be guessed by player.
        self.number = random.randrange(MIN, MAX + 1)

        self.tries = 0


    def create_widgets(self):
        """Program all the widgets to be used."""
        Label(self,
              text="I'm thinking of a number between " + str(MIN) +
                   " and " + str(MAX)
              ).grid(row=0, column=0, columnspan=2, sticky=W)

        Label(self,
              text="Try to guess the number"
              ).grid(row=1, column=0, columnspan=2, sticky=W)

        

        Label(self,
              text="Guess"
              ).grid(row=2, column=0, sticky=W)


        # Entry widget to allow guessing
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row=2, column=1, sticky=W)

        # Submit button to obtain guess
        Button(self,
               text="Enter",
               command=self.get_guess
               ).grid(row=2, column=2, columnspan=4, sticky=W)
        Button(self,
               text="Reset",
               command=self.reset
               ).grid(row=1, column=2, columnspan=1, sticky=W)

        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=3, column=0, columnspan=3)

    def get_guess(self):
        """Obtain the player's guess and verify it."""
        try:
            guess = int(self.guess_ent.get())
        except(ValueError):
            self.display_message("Invalid entry. Try again.")
        else:
            self.tries += 1
            Label(self,
                  text="     Number Of Tries: " + str(self.tries)
                  ).grid(row=0, column=2, columnspan=1, sticky=W)
            self.check_guess(guess)

    def check_guess(self, guess):
        """
        Verify if the player's guess is correct.
        Keyword argument:
        guess - the int value to be verified
        """
        if guess < MIN or guess > MAX:
            self.display_message("Invalid Input, Guess Out Side Of Range.")
            self.tries -= 1  # This try doesn't count
            return

        # If guess equals the number, end current game.
        if guess == self.number:
            self.resetgame()
            return

        # Otherwise, see if guess is higher or lower than the chosen number.
        if guess < self.number:
            self.display_message("Guess Higher...")
            return
        elif guess > self.number:
            self.display_message("Guess Lower...")
            return




    def display_message(self, message):
        """
        Display a message on the text box.
        Keyword argument:
        message -- the message to be displayed
        """
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)

    def reset(self):
        """Prepare for a new game."""
        self.number = random.randrange(MIN, MAX + 1)
        self.display_message("Game Reset. Please enter another number to play again.")
        self.tries = 0
        Label(self,
              text="Number Of Tries: " + str(self.tries)
              ).grid(row=0, column=2, columnspan=1, sticky=W)
    def resetgame(self):
        self.display_message("Congrats! You guessed correctly! The number was " + \
                             str(self.number) + ". It only took you " + \
                             str(self.tries) + " tries!" + " Click The Reset Button To Play Again" )


def main():
    """Kickstart Guess My Number."""
    root = Tk()
    root.title("Guess My Number")
    app = Application(root)
    root.mainloop()



# start Guess My Number
main()