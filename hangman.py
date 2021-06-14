import random

GAME_NAME = 'H A N G M A N'
LIST_OF_WORDS = ('python', 'chloe', 'archie', 'airdrie')  # ('python', 'java', 'kotlin', 'javascript')
GUESS_LIMIT = 8


def get_menu_choice():
    menu_choice_ = str(input('Type "play" to play the game, "exit" to quit:'))
    return menu_choice_


def start_game():
    print(GAME_NAME)
    secret_word_ = random.choice(LIST_OF_WORDS)
    clue_ = '-' * len(secret_word_)
    return secret_word_, clue_  # False indicates game not over (started...


def get_guess(clue_):
    print()
    print(clue_)
    return str(input('Input a letter:'))


def is_repeat_letter(guess_, letters_guessed_, valid_guess_):
    if guess_ in letters_guessed_:
        # print(letters_guessed_)
        return True, letters_guessed_
    elif guess_ not in letters_guessed_ and valid_guess_:
        letters_guessed_ += guess_
        # print(letters_guessed_)
        return False, letters_guessed_
    else:
        return False, letters_guessed_


def is_valid_input(guess_):
    if len(guess_) == 1:
        valid_length = True
    else:
        print('You should input a single letter')
        valid_length = False

    if len(guess_) > 0 and guess_[0].islower() is True:
        valid_lowercase = True
    else:
        valid_lowercase = False

    if guess_.isalpha() is True:
        valid_alpha = True
    else:
        valid_alpha = False

    if False in [valid_lowercase, valid_alpha] and valid_length is True:
        print('Please enter a lowercase English letter')

    if False in [valid_alpha, valid_length, valid_lowercase]:
        return False
    else:
        return True


# ### ### Program Flow  ### ### #
# ### ### Program Flow  ### ### #
# ### ### Program Flow  ### ### #
menu_choice = 'need choice'

while menu_choice == 'need choice':
    menu_choice = get_menu_choice()
    if menu_choice == 'play':
        game_over = False
    elif menu_choice == 'exit':
        game_over = True
    else:
        game_over = True

    # Initialize the game
    secret_word, clue = start_game()
    game_won = False
    game_lost = False
    letters_guessed = []
    repeat_guess = False
    valid_guess = False
    wrong_letters = 0

    # play the game until over
    while game_over is not True:

        # get a new guess
        guess = get_guess(clue)
        # check if it's a valid guess & print line if it's not
        valid_guess = is_valid_input(guess)
        # check if it's a repeat guess and add to list of guesses if new letters.
        repeat_guess, letters_guessed = is_repeat_letter(guess, letters_guessed, valid_guess)

        # handle invalid guess
        if valid_guess is False:  # If guess (input) isn't valid
            pass

        # handle repeat guesses (valid but repeat)
        elif repeat_guess is True and guess in secret_word:  # repeat correct letter
            print("You've already guessed this letter")
        elif repeat_guess is True and guess not in secret_word:  # repeat wrong letter
            print("You've already guessed this letter")
            print("That letter doesn't appear in the word")

        # handle wrong guess that isn't a repeat guess (valid but wrong)
        elif guess not in secret_word:
            print("That letter doesn't appear in the word")
            wrong_letters += 1

        # handle correct guess (valid and not repeat)
        elif guess in secret_word and not repeat_guess:
            clue = ''
            for i in range(0, len(secret_word)):
                if secret_word[i] in letters_guessed:
                    clue += secret_word[i]
                else:
                    clue += '-'

        else:
            print('ERROR: UNEXPECTED CASE')

        # If wrong_letters count hits game limit, set to end game with loss
        if wrong_letters >= GUESS_LIMIT:
            game_lost = True
            game_over = True
            game_won = False

        # if game is won - secret word =- clue !!!, set to end game with win
        if secret_word == clue:
            game_lost = False
            game_over = True
            game_won = True

    # end the game
    if game_won is True:
        print(f'You guessed the word {secret_word}!')
        print('You survived!')
        menu_choice = 'need choice'
    if game_lost is True:
        print('You lost!')
        menu_choice = 'need choice'

    # get menu choice or exit
    if menu_choice == 'exit':
        exit()
    else:
        menu_choice = 'need choice'
