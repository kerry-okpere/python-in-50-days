word_list = (
    "ant badger bat bear beaver camel cat clam cobra cougar "
    "crow dog donkey duck eagle fox frog goat "
    "hawk lion lizard mole monkey mouse mule newt "
    "owl parrot pigeon python ram rat raven "
    "rhino salmon seal shark sheep skunk sloth snake spider "
    "stork swan tiger toad trout turkey weasel whale wolf "
    "wombat zebra "
).split()

HANGMANPICS = [
    r'''
  +---+
  |   |
      |
      |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
]