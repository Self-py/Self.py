HANGMAN_PHOTOS = {'1': """    x-------x""", '2': """
    x-------x
    |
    |
    |
    |
    |""", '3':"""
    x-------x
    |       |
    |       0
    |
    |
    |""", '4': """
    x-------x
    |       |
    |       0
    |       |
    |
    |""", '5': """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", '6': """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""", '7': """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}
def print_hangman(num_of_tries):
    """Prints hangman state, according to input nunmer.
    :param: num_of_tries: define the state to be displayed
    :type: int
    """
    print(HANGMAN_PHOTOS[str(num_of_tries)])