import random

def hangman_animation(num):
    one = """
  7-------
  |       |
  |      
  |       
  |     
  |       
__|__    
    """
    two = """
  7-------
  |       |
  |      _n
  |       
  |     
  |       
__|__    
    """
    three = """
  7-------
  |       |
  |      _n
  |       0
  |     
  |       
__|__    
    """
    four = """
  7-------
  |       |
  |      _n
  |       0
  |       |
  |       
__|__    
    """
    five = """
  7-------
  |       |
  |      _n
  |       0
  |     --|
  |       
__|__    
    """
    six = """
  7-------
  |       |
  |      _n
  |       0
  |     --|--
  |       
__|__    
    """
    seven = """
  7-------
  |       |
  |      _n
  |       0
  |     --|--
  |       A
__|__    
    """
    eight = """
  7-------
  |       |
  |      _n
  |       0
  |     --|--
  |       A
__|__    /
    """
    nine = """
  7-------
  |       |
  |      _n
  |       0
  |     --|--
  |       A
__|__    / \\
    """
    total = [one, two, three, four, five, six, seven, eight, nine]
    return total[num]

def hangman_words():
    word_bank = ['tree', 'programming', 'computer', 'ducks', 'jazz', 'fitness', 'pizza', 'boring', \
             'shirt', 'coffee', 'glasses', 'python', 'table', 'skyscraper', 'chorizo', 'blanket', \
             'jacket', 'carpet', 'codeup', 'tequila', 'headphones', 'sleep', \
             'linux', 'regression', 'average', 'sailor', 'riverwalk', 'statistics', 'longboard', 'camero', \
                 'windows', 'apple', 'hadoop', 'bidoof', 'spark', 'tableau', 'terminal',\
                 'whisky', 'marker', 'airpods', 'edgy', 'hacker', 'javascript', 'chicken', \
                 'command']
    return random.choice(word_bank)



