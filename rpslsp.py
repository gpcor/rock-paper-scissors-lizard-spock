import random
import sys

from time import sleep


class MyGame:

    throwOptions = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    def __init__(self):

        self.scoreboard = {'player': 0, 'computer': 0}
        self.matchScore = {'player': 0, 'computer': 0}
        self.playerThrow = ''
        self.computerThrow = ''
        self.new_game_answer = ''
        self.rulesChoice = ''

        print('''
                                                                        
        88888888ba   88888888ba    ad88888ba   88           ad88888ba   
        88      "8b  88      "8b  d8"     "8b  88          d8"     "8b  
        88      ,8P  88      ,8P  Y8,          88          Y8,          
        88aaaaaa8P'  88aaaaaa8P'  `Y8aaaaa,    88          `Y8aaaaa,    
        88""""88'    88""""""'      `"""""8b,  88            `"""""8b,  
        88    `8b    88                   `8b  88                  `8b  
        88     `8b   88           Y8a     a8P  88          Y8a     a8P  
        88      `8b  88            "Y88888P"   88888888888  "Y88888P"   
                                                                
                                                                
        
        ''')

    def game_start(self):

        print('Welcome to Rock-Paper-Scissors-Lizard-Spock')
        sleep(2)
        print('Basically Rock-Paper-Scissors but with more options')
        sleep(2)
        print('Need to know the (r)ules? Or are you ready to (s)tart? (use "r" and "s" to either see the rules or start the game)')
        self.rulesChoice = str.lower(input())

    def game_rules(self):

        game_rules = '''
            # Rock, Paper, Scissors, Lizard, Spock

            A game of chance based on the hit TV show Big Bang Theory.

            Applicable Throws:
            ==================
            Players can throw one of the following Signs:
            * Rock
            * Paper
            * Scissors
            * Lizard
            * Spock

            Winning Matches:
            ----------------
            * Rock: Smashes Scissors and Lizard
            * Paper: Covers Rock and Disproves Spock
            * Scissors: Cuts Paper and Decaptitates Lizard
            * Lizard: Eats Paper and Poisons Spock
            * Spock: Vaporizes Rock and Smashes Scissors

            Rules
            -----
            * All players will one make one throw per round
            * The game is Best 3 out of 5 with a maximum of five rounds per Match
            * The first to three points wins the Match
            '''

        if self.rulesChoice == 'r':
            print(game_rules)
        else:
            pass

    def make_throws(self):

        print('Make your throw.')
        self.playerThrow = str.lower(input())
        self.computerThrow = random.choice(self.throwOptions)

    def throw_matchup(self):

        if self.playerThrow == 'rock':

            if self.computerThrow == 'scissors' or self.computerThrow == 'lizard':
                print('{} trumps {}, you win the round!'.format(
                    self.playerThrow, self.computerThrow))
                self.scoreboard['player'] += 1
                print(self.scoreboard)

            elif self.computerThrow == self.playerThrow:
                print('The round is a tie!')

            else:
                print('{} is trumped by {}, you lose the round'.format(
                    self.playerThrow, self.computerThrow))
                self.scoreboard['computer'] += 1
                print(self.scoreboard)

        elif self.playerThrow == 'paper':

            if self.computerThrow == 'rock' or self.computerThrow == 'spock':
                print('{} trumps {}, you win the round!'.format(
                    self.playerThrow, self.computerThrow))
                self.scoreboard['player'] += 1
                print(self.scoreboard)

            elif self.computerThrow == self.playerThrow:
                print('The round is a tie!')

            else:
                print('{} is trumped by {}, you lose the round'.format(
                    self.playerThrow, self.computerThrow))
                self.scoreboard['computer'] += 1
                print(self.scoreboard)

        elif self.playerThrow == 'scissors':

            if self.computerThrow == 'paper' or self.computerThrow == 'lizard':
                print('{} trumps {}, you win the round!'.format(
                    self.playerThrow, self.computerThrow))
                self.scoreboard['player'] += 1
                print(self.scoreboard)

            elif self.computerThrow == self.playerThrow:
                print('The round is a tie!')

            else:
                print('{} is trumped by {}, you lose the round'.format(
                    self.playerThrow, self.computerThrow))
                self.scoreboard['computer'] += 1
                print(self.scoreboard)

        elif self.playerThrow == 'lizard':

            if self.computerThrow == 'paper' or self.computerThrow == 'spock':
                print('{} trumps {}, you win the round!'.format(
                    self.playerThrow, self.computerThrow))
                self.scoreboard['player'] += 1
                print(self.scoreboard)

            elif self.computerThrow == self.playerThrow:
                print('The round is a tie!')

            else:
                print('{} is trumped by {}, you lose the round'.format(
                    self.playerThrow, self.computerThrow))
                self.scoreboard['computer'] += 1
                print(self.scoreboard)

        elif self.playerThrow == 'spock':

            if self.computerThrow == 'rock' or self.computerThrow == 'scissors':
                print('{} trumps {}, you win the round!'.format(
                    self.playerThrow, self.computerThrow))
                self.scoreboard['player'] += 1
                print(self.scoreboard)

            elif self.computerThrow == self.playerThrow:
                print('The round is a tie!')

            else:
                print('{} is trumped by {}, you lose the round'.format(
                    self.playerThrow, self.computerThrow))
                self.scoreboard['computer'] += 1
                print(self.scoreboard)

        else:
            print('That is not an approve throw.')

    def new_game_question(self):

        print('Thanks for playing! Wanna go again? ')

        while True:

            self.new_game_answer = str.lower(input())
            if self.new_game_answer == 'yes':
                for i in iter(self.scoreboard):
                    self.scoreboard[i] = 0
                print('Let us begin...')
                break

            elif self.new_game_answer != 'yes' and self.new_game_answer != 'no':
                print('I prefer yes and no answers only, please and thank you...')

            else:
                break


def main():

    game = MyGame()
    game.game_start()
    game.game_rules()

    while True:

        game.make_throws()
        game.throw_matchup()
        if game.scoreboard['player'] == 3:

            print('You win!')
            game.matchScore['player'] += 1
            print('The current match score is {}'.format(game.matchScore))
            game.new_game_question()
            try:
                if game.new_game_answer == 'yes':
                    game.make_throws()
                    game.computer_player()
                    game.throw_matchup()

                else:
                    print('See you later')
                    sys.exit()
            except:
                if KeyboardInterrupt:
                    print('How abruptly rude...')
                    sys.exit()

        elif game.scoreboard['computer'] == 3:

            print('The computer won!')
            game.matchScore['computer'] += 1
            print('The current match score is {}'.format(game.matchScore))
            game.new_game_question()

            if game.new_game_answer == 'yes':

                game.make_throws()
                game.throw_matchup()

            else:
                break


if __name__ == '__main__':
    main()
