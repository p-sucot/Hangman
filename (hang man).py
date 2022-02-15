# Table of Contents:
# Basic variables -> Line 6
# The functions(10) -> Line 49
# Moves of the game(5) -> Line 261

# The 5 basic variables:
MAX_TRIES = 6
num_of_tries = 0
secret_word = ""
old_letters_guessed = []
HANGMAN_PHOTOS = {1: """    x-------x""", 2: """    x-------x
    |
    |
    |
    |
    |
""", 3: """    x-------x
    |       |
    |       0
    |
    |
    |
""", 4: """    x-------x
    |       |
    |       0
    |       |
    |
    |
""", 5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""", 6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
""", 7: """     x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}


# The functions of the game:
# Function number 1:
def opening_screen():
    """
    A function that prints the game's opening screen,
     and the number of possible failed attempts
    """
    print("Welcome to the game Hangman")
    print("""      _    _
     | |  | |
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |
                         |___/""")
    print(MAX_TRIES)


# Function number 2:
def choose_word(file_path, index):
    """
    The function receives from the player the file path (file of words),
    and receives from the player the word number,
    the function returns the same word from the file.
    :param:The file path, of the word file for the game
    :param:The number of words from the words in the file
    :type:file
    :type:int
    :return:Returns the secret word,
    and the number of different words that exist in the file
    :rtype:str
    """
    with open(file_path, "r") as file_object:
        word_list = file_object.read().split()
        index = index - 1
        if index >= len(word_list):
            index = index % len(word_list)
        global secret_word
        secret_word = word_list[index].lower()
        new_word_list = []
        for i in word_list:
            if i not in new_word_list:
                new_word_list.append(i)
        numbers_Words = len(new_word_list)
    print("You have to guess the secret word from ",
                numbers_Words, " Words that exist in the word file")
    return (secret_word)


# Function number 3(Includes function 2):
def Arguments_for_choose_word():
    """
    The function receives from the player the file path of the word file,
    and receives the word number from the file,
    and embeys the number 2 function on them
    :param:The file path, of the word file for the game
    :param:The number of words from the words in the file
    :type:file
    :type:int
    :return:Returns the secret word,
    and the number of different words that exist in the file
    :rtype:str
    """
    file_path = input("Type here the file path of the word file:")
    index = input("Type here the word number you choose:")
    index = (int(index))
    choose_word(file_path, index)


# Function number 4:
def print_hangman(num_of_tries):
    """
    The function shows the player the condition of the dependent man,
    according to the number of his failed attempts.
    :param:Number of failed attempts
    :type:int
    :return:Prints the man depending on his situation
    :rtype:str
    """
    print (HANGMAN_PHOTOS.get((num_of_tries) + 1))


# Function number 5:
def show_hidden_word(secret_word, old_letters_guessed):
    """
    The function returns to the player
    the correct letters he has already guessed,
    and bottom lines within the secret word, to letters he has not yet guessed
    :param:string of the secret word
    :param:list of the characters the player has already guessed
    :type:str
    :type:list
    :return:The secret word, when the letters he has already guessed appear,
    and the letters he has not yet guessed appear in their place Underlines
    :rtype:str
    """
    hidden_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            hidden_word = hidden_word + letter + " "
        else:
            hidden_word = hidden_word + "_ "
    hidden_word = hidden_word[:-1]
    return hidden_word


# Function number 6:
def check_valid_input(letter_guessed, old_letters_guessed):
    """
    The function checks whether the character
    that the player types is correct or not
    :param:A character that the player will type
    :param:A list of all the normal characters the player tried to guess
    :type:str
    :type:list
    :return:Is the character correct or not
    :rtype:Boolean
    """
    if len(letter_guessed) != 1 or not letter_guessed.isalpha()\
            or letter_guessed.lower() in old_letters_guessed:
        return False
    else:
        return True


# Function number 7:
def type_letter_guessed():
    """
    The function receives a character from the player
    :param:The player types a character
    :type:str
    :return:Returns the character as a small letter
    :rtype:str
    """
    letter_guessed = input("Guess one letter and type it here:")
    letter_guessed = letter_guessed.lower()
    return letter_guessed


# Function number 8:
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    The function that puts the typed character
    in the guessing list if the character is correct,
    and if it is not correct it will return a lie
    :param:String of a selected character
    :param:A list of the characters the player has already guessed
    :type:str
    :type:list
    :return:If the character is correct she will add me to the list Print true,
    if it is invalid she will print X and print the list and print a lie
    :rtype:Boolean
    :rtype:str
    :rtype:list
    """
    if check_valid_input(letter_guessed, old_letters_guessed) is True:
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print ("X")
        new_old_letters_guessed = sorted(old_letters_guessed)
        print (" -> ".join(new_old_letters_guessed).lower())
        return False


# Function number 9(Includes functions 6, 7, 8):
def letter_guessed_loop():
    """
    The function receives the character from the game,
    it repeatedly requests it until it is OK
    :param:Letter or character
    :type:str
    :return:Returns a lie if the attempt to guess failed
    :rtype:Boolean
    """
    while True:
        letter_guessed = type_letter_guessed()
        check_valid_input(letter_guessed, old_letters_guessed)
        if try_update_letter_guessed \
                (letter_guessed, old_letters_guessed) is True:
            break
    if letter_guessed not in secret_word:
        return False


# Function number 10(Includes function 9):
def The_game_process():
    """
    The function asks the player to type letters again and again,
    until the game is over
    :param:Function number 9
    :type:Function
    :return:WIN if the player wins, or LOSE if the player fails
    :rtype:str
    """
    while True:
        if letter_guessed_loop() is False:
            global num_of_tries
            num_of_tries = num_of_tries + 1
            print_hangman(num_of_tries)
        print(show_hidden_word(secret_word, old_letters_guessed))
        Matching_guesses = \
            all([Letter in old_letters_guessed for Letter in secret_word])
        if num_of_tries == 6 or Matching_guesses is True:
            break
    if num_of_tries == 6:
        print("LOSE")
    if Matching_guesses is True:
        print("WIN")


# The game process:
def main():
    # Call to function number 1:
    opening_screen()

    # Call to function number 3:
    Arguments_for_choose_word()

    # Call to function number 4:
    print_hangman(num_of_tries)

    # Call to function number 5:
    print(show_hidden_word(secret_word, old_letters_guessed))

    # Call to function number 10:
    The_game_process()

if __name__ == "__main__":
    main()
