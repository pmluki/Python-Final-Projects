import random
from tkinter import *
from tkinter import messagebox

class GUI():
    def __init__(self, window):
        # ------------------------
        # --- SET UP FOR WORDS ---
        # ------------------------
        self.game = True
        self.window = window

        self.word_generate()
        self.num_guesses = 6
        self.update = None

        # --------------------------------
        # --- GUESSES AND TOWER SET UP ---
        # --------------------------------

        self.tower = Label(self.window, text="", font=('Ariel', 30))
        self.tower.place(x=150, y=150)

        self.tower_progress()

        # --------------------
        # --- USER PROMPTS ---
        # --------------------

        self.label_title = Label(self.window, text='Hangman', font=('Ariel', 30)).pack()
        self.label_game_explain = Label(self.window, text='Can you guess the word? Enter one letter at a time to try!\n'
                                        'Each word you guess incorrectly will add to the hangman. '
                                        'Try to guess the word in 6 tries, correct ones\nwon\'t impact your attempts left, good luck!', font=('Ariel', 12))
        self.label_game_explain.pack()

        self.guess_text = Label(self.window, text='Type in a letter to guess the word!')
        self.guess_text.place(x=450, y=150)

        self.letters_used_label = Label(self.window, text=(f'Letters Used:'), font=('Ariel', 10))
        self.letters_used_label.place(x=450, y=350)

        self.letters_used_below = Label(self.window, text='', font=('Ariel', 10))
        self.letters_used_below.place(x=450, y=370) #TODO: Change the y later

        # ---------------------
        # --- COUNT GUESSES ---
        # ---------------------

        self.count_guesses = Label(self.window, text=(f'Guesses left: {self.num_guesses}'), font=('Ariel', 10))
        self.count_guesses.place(x=450, y=420)

        # ------------------------------
        # --- PLAYER GUESS ENTRY BOX ---
        # ------------------------------

        self.guess_strVar = StringVar()
        self.player_guess = Entry(self.window, text='', textvariable=self.guess_strVar, justify='right', width=29)
        self.player_guess.place(x=455, y=175)

        # ---------------------
        # --- SUBMIT BUTTON ---
        # ---------------------

        self.button_submit = Button(self.window, text='Submit', command=self.guess_check)
        self.button_submit.place(x=550, y=200, height=30, width=80)

        # -----------------------
        # --- New Game Button ---
        # -----------------------

        self.button_new_game = Button(self.window, text='New Game', command=self.new_game)
        self.button_new_game.place(x=225, y=475, height=50, width=80)

        # -------------------
        # --- Exit Button ---
        # -------------------

        self.button_exit = Button(self.window, text='Exit', command=window.destroy)
        self.button_exit.place(x=525, y=475, height=50, width=80)

    def new_game(self):
        '''
        This creates a new game with a new word, resets the guesses and tower, and places the
        default label at the top of the game.
        :return: Settings back to start
        '''
        self.hidden_word_label.config(text='')
        self.word_generate()
        self.num_guesses = 6
        self.count_guesses.config(text=(f'Guesses left: {self.num_guesses}'))
        self.tower_progress()
        self.label_game_explain.config(text="Can you guess the word? Enter one letter at a time to try!\nEach word you guess incorrectly will add to the hangman. Try to guess the word in 6 tries, correct ones\nwon\'t impact your attempts left, good luck!'")
        self.guess_strVar.set('')
        self.letters_used_below.config(text='')
        self.update = ''
        self.game = True

    def guess_check(self):
        '''
        This method goes through and checks if the letter they have entered is correct.
        FIRST: Checks to see if the input is a letter (A-Z)
        SECOND: Checks to see if it is only ONE character
        THIRD: Lowercases the letter and checks to see if it is correct. It will display
               a correct message if it is. If it is not, it will lower their guesses left
               and then let them know it was incorrect.
        :return: Updates the tower, checks the answer, and clears the text box
        '''
        global player_guess
        player_guess = self.guess_strVar.get()
        if not player_guess.isalpha(): # Fine
            self.label_game_explain.configure(text='Looks like that\'s not a valid character! Pick a letter A-Z and try again!')
            self.label_game_explain.pack()
        elif len(player_guess) != 1: # Fine
            self.label_game_explain.config(text='Only enter one letter at a time! Try again!')
        else:
            player_guess.islower()
            if self.game == True:
                if self.letter_check() == True:
                    self.used_letters(player_guess)
                    self.label_game_explain.config(text='Good job, that was correct! Try to guess the next letter.')
                elif self.letter_check() == False:
                    self.used_letters(player_guess)
                    self.count_guess()
                    self.label_game_explain.config(text="Looks like that letter is not in the word! Try again!")

            self.guess_counter() # Counts the guesses and updates the tower
        self.ans_check()
        self.guess_strVar.set('')

    def count_guess(self):
        '''
        This counts the guesses the player has left.
        :return: Returns an update to the label notifying the player of their guesses left.
        '''
        self.num_guesses -= 1
        self.count_guesses.config(text=(f'Guesses left: {self.num_guesses}'))

    def ans_check(self):
        '''
        This checks to see if the game is active or not. It disables the user from continuing to
        play after they have beat the game.
        :return: Returns game as False once they win.
        '''
        ans = self.chosen_word
        if self.starred == ans:
            self.label_game_explain.config(text='Congrats! You win! If you would like to play again, click new game.')
            self.button_submit.config(command=None)
            self.game = False


    def tower_progress(self):
        '''
        This method builds the tower based on the amount of guesses left.
        :return: Returns the tower to the application
        '''
        if self.num_guesses == 6:
            self.tower.config(text="      --------\n"
                                             "       |      |\n"
                                             "|\n"
                                             "|\n"
                                             "|\n"
                                             "|\n"
                                             "----", font=('Ariel', 30))
        elif self.num_guesses == 5:
            self.tower.config(text="      --------\n"
                                             "       |      |\n"
                                             "        |     O\n"
                                             "|\n"
                                             "|\n"
                                             "|\n"
                                             "----", font=('Ariel', 30))
        elif self.num_guesses == 4:
            self.tower.config(text="      --------\n"
                                             "       |      |\n"
                                             "        |     O\n"
                                             "       |      |\n"
                                             "|\n"
                                             "|\n"
                                             "----", font=('Ariel', 30))
        elif self.num_guesses == 3:
            self.tower.config(text="      --------\n"
                                             "       |      |\n"
                                             "        |     O\n"
                                             "       |     /|\n"
                                             "|\n"
                                             "|\n"
                                             "----", font=('Ariel', 30))
        elif self.num_guesses == 2:
            self.tower.config(text="      --------\n"
                                             "       |      |\n"
                                             "        |     O\n"
                                             "        |     /|\\\n"
                                             "|\n"
                                             "|\n"
                                             "----", font=('Ariel', 30))
        elif self.num_guesses == 1:
            self.tower.config(text="      --------\n"
                                             "       |      |\n"
                                             "        |     O\n"
                                             "        |     /|\\\n"
                                             "      |     /\n"
                                             "|\n"
                                             "----", font=('Ariel', 30))
        elif self.num_guesses == 0:
            self.tower.config(text="      --------\n"
                                             "       |      |\n"
                                             "        |     O\n"
                                             "        |     /|\\\n"
                                             "        |     / \\\n"
                                             "|\n"
                                             "----", font=('Ariel', 30))


    def used_letters(self, guess):
        '''
        This function goes through and adds letters to the user's guessed letters.
        :param guess: This takes in the player_guess
        :return: This updates the used letter bank
        '''
        if self.update == None:
            self.update = player_guess
        else: #FIXME: FIrst letter returning True 
            self.update = f'{self.update} {player_guess}'
        self.letters_used_below.config(text=f'{self.update} ')

    def word_generate(self):
        '''
        This method chooses a random word from the word bank and allows the player to
        begin the game. It then stars out the length of the word so the user will know
        how many letters are left once they start guessing.
        :return: Returns the word as a hidden one for the game to start.
        '''
        self.word_bank = ['dog', 'cat', 'python', 'snake', 'cobra', 'frog', 'monkey', 'lizard',
                          'horse', 'tiger', 'wolf', 'bear', 'narwhal', 'dragon', 'dinosaur',
                          'camel', 'bat', 'fly']
        self.chosen_word = random.choice(self.word_bank)
        self.starred = '*' * len(self.chosen_word)

        self.hidden_word_label = Label(self.window, text=self.starred, font=('Ariel', 30))
        self.hidden_word_label.place(x=450, y=250)

    def letter_check(self):
        '''
        This method lowers the player_guess to ensure the character matches.
        FOR LOOP: The for loop goes through each letter of the player guess and adds the letter
                  to the correct position of the word. Once it finds the correct place, it
                  breaks out and adds it to the starred word.
        :return: Returns the correct letter to the correct position
        '''
        player_guess.islower()
        for i in range(0, len(self.chosen_word)):
            if self.chosen_word[i] == player_guess:
                pos = i
                new_starred = self.starred[:pos] + player_guess + self.starred[pos + 1:]
                self.starred = new_starred
                self.hidden_word_label.config(text=self.starred)
                ans = True
                break
            elif self.chosen_word[i] != player_guess:
                ans = False
        return ans

    def guess_counter(self):
        '''
        This method goes through and updates the game tower for the amount of guesses left.
        When you reach 0, it will deny you from inputting more letters and say the game is
        over.
        :return: Calls Tower Progress to match the amount of guesses
        '''
        if self.num_guesses == 0:
            self.tower_progress()
            self.button_submit.config(command=None)
            self.label_game_explain.config(text=f'Game over! The word was {self.chosen_word}. Thanks for playing! Feel free to try again with the new game button.')
            self.game = False
        elif self.num_guesses == 1:
            self.tower_progress()
        elif self.num_guesses == 2:
            self.tower_progress()
        elif self.num_guesses == 3:
            self.tower_progress()
        elif self.num_guesses == 4:
            self.tower_progress()
        elif self.num_guesses == 5:
            self.tower_progress()
