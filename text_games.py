import random
import pickle
import numpy as np
import re
import hangman_file as hf


def rps(*args):
    try:
        toggle = pickle.load(open('rps_data.p', 'rb'))
    except:
        pickle.dump(False, open('rps_data.p', 'wb'))
        toggle = False
    w_or_l = 0
    aa = []
    for a in args:
        aa.append(a)
    print('<<<<<<<<<<>>>>>>>>>>')
    choice = ['r', 'p', 's']
    words = ['ROCK', 'PAPER', 'SCISSORS']    
    if a[0] not in choice:
            print('first var needs to be r, p, or s')
            return        
    ai_choice = random.choice(choice)
    if a[0] == ai_choice:
        print('its a tie!')
        win_or_l = 3      
    if a[0] == 'r' and ai_choice == 's' or a[0] == 'p' and ai_choice == 'r' \
       or a[0] == 's' and ai_choice == 'p':
        print(words[choice.index(a[0])] + ' beats ' + words[choice.index(ai_choice)] + \
              ', PLAYER wins!')
        w_or_l = 1
    if a[0] == 'r' and ai_choice == 'p' or a[0] == 'p' and ai_choice == 's' or a[0] == 's' \
       and ai_choice == 'r':
        print(words[choice.index(ai_choice)] + ' beats ' + words[choice.index(a[0])] + \
              ', RPS_AI wins!')
        w_or_l = 2
    for a in args:
        if a == 'rscore':
            toggle = not toggle
            pickle.dump(toggle, open('rps_data.p', 'wb'))
            print('<<DATA SAVED>>')
        if a == 'score' or toggle == True:
            try:
                score = pickle.load(open('rps_score.p', 'rb'))
            except:
                print('<<<NO DATA FOUND, SCORE RESET>>>')
                score = [0, 0]
            if w_or_l == 1:
                score[0] += 1
            if w_or_l == 2:
                score[1] += 1
            print('_______________________________')
            print('PLAYER score: ' + str(score[0]))
            print('RPS_AI score: ' + str(score[1]))
            pickle.dump(score, open('rps_score.p', 'wb'))
        if a == 'reset':
            print('<<<SCORE_RESET>>>')
            pickle.dump([0, 0], open('rps_score.p', 'wb'))
            score = pickle.load(open('rps_score.p', 'rb'))
            print('_______________________________')
            print('PLAYER score: ' + str(score[0]))
            print('RPS_AI score: ' + str(score[1]))
    print('<<<<<<<<<<>>>>>>>>>>')

def hangman():
    ai_choice = hf.hangman_words()
    word = list(ai_choice)
    guessbox = []
    wrongword = []
    for w in word:
        guessbox.append('__')
    score = 0
    while True:
        try:
            animation = hf.hangman_animation(score)
        except:
            print('<<GAME OVER>>')
            print('WORD WAS >> ' + ai_choice)
            break
        print(animation)
        print('<<<<<<<<<<>>>>>>>>>>')
        print('Letters guessed: ' + str(wrongword))
        print('<<' + str(guessbox) + '>>')
        if (len(set(word)) == 1):
            print('<<PLAYER wins!>>')
            break
        inp = input('Enter guess >> ')
        inp = inp.lower()
        if inp == 'quit':
            break
        if inp not in word and inp not in wrongword:
            wrongword.append(inp)
            score += 1
        if inp in word and inp != '!':
            instances = [i for i, x in enumerate(word) if x == inp]
            for i in instances:
                intword = word.index(inp)
                guessbox.pop(word.index(inp))
                guessbox.insert(word.index(inp), inp)
                word.pop(intword)
                word.insert(intword, '!')
        print('<<<<<<<<<<>>>>>>>>>>')


def blackjack():
    card_list = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'king', 'queen']
    card_types = ['ace', 'jack', 'king' 'queen']
    deck = {'hearts' : ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'king', 'queen'], \
            'clubs' : ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'king', 'queen'],\
            'dimonds' : ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'king', 'queen'], \
            'spades' : ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'king', 'queen']}
    ai_deck = deck
    player_score = 0
    ai_score = 0
    l = False
    ace = False
    while True:
        print('<<<<<>>>>>')
        if player_score > 21:
            print('<<PLAYER went over! BLACKJACK_AI wins!>>')
            l = True
            break
        inp = input('[H]it or [S]tay? >> ')
        if inp == 'H':
            ai = random.choice(list(deck.keys()))
            player_choice = random.choice(deck[ai])
            print(str(player_choice) + ' of ' + ai)
            if deck[ai].index(player_choice) == 0:
                if (player_score + 11) <= 21:
                    player_score += 11
                    ace = True                   
            if deck[ai].index(player_choice) + 1 > 10:
                player_score += 10
            if deck[ai].index(player_choice) + 1 <= 10 and ace == False:
                player_score += deck[ai].index(player_choice) + 1
            print('Current Score >> ' + str(player_score))
            deck[ai].remove(player_choice)
        if inp == 'S':
            break
    while True:
        if l == True:
            break
        if ai_score > 21:
            print('<<<<<>>>>>')
            print('<<BLACKJACK_AI went over! PLAYER wins!>>')
            break
        if ai_score >= 16:
            break
        aii = random.choice(list(ai_deck.keys()))
        ai_choice = random.choice(ai_deck[aii])
        if ai_deck[aii].index(ai_choice) + 1 > 10:
            ai_score += 10
        if ai_deck[aii].index(ai_choice) + 1 <= 10:
            ai_score += ai_deck[aii].index(ai_choice) + 1
    print('BLACKJACK_AI score : {}'.format(ai_score))
    if ai_score > player_score and ai_score <= 21:
        print('<<BLACKJACK_AI wins!>>')
    if player_score > ai_score and player_score <= 21:
        print('<<PLAYER wins!>>')

        
        
    
