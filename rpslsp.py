"""This program is for the  game Rock-paper-scissors-lizard-spock"""

import random
import sys

from time import sleep


class MyGame:
    """The Game class for the program"""

    throw_options = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    def __init__(self):

        self.scoreboard = {'player': 0, 'computer': 0}
        self.match_score = {'player': 0, 'computer': 0}
        self.player_throw = ''
        self.computer_throw = ''
        self.new_game_answer = ''
        self.rules_choice = ''

    def game_start(self):
        '''Determines the start of the game and if rules are displayed'''
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

        print('Welcome to Rock-Paper-Scissors-Lizard-Spock')
        sleep(2)
        print('Basically Rock-Paper-Scissors but with more options')
        sleep(2)
        print('Need to know the (r)ules? Or are you ready to (s)tart?')
        print('(Use "r" and "s" to either see the rules or start the game):')
        self.rules_choice = input()

    def game_rules(self):
        '''Only job here is to display the rules'''

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
            * The game is Best 3 out of 5 with a maximum of five rounds per
              Match
            * The first to three points wins the Match
            '''

        if self.rules_choice == str.lower('r'):
            print(game_rules)
        else:
            pass

    def make_throws(self):
        '''Player inputs their throw and the computer randomly selects its'''

        print('Make your throw.')
        self.player_throw = str.lower(input())
        self.computer_throw = random.choice(self.throw_options)

    def throw_match_up(self):
        '''compares throws made by player and pc to see who won the throw'''

        if self.player_throw == 'rock':

            if self.computer_throw == 'scissors' or 'lizard':
                print('{} trumps {}, you win the round!'.format(
                    self.player_throw, self.computer_throw))
                self.scoreboard['player'] += 1
                print(self.scoreboard)

            elif self.computer_throw == self.player_throw:
                print('The round is a tie!')

            else:
                print('{} is trumped by {}, you lose the round'.format(
                    self.player_throw, self.computer_throw))
                self.scoreboard['computer'] += 1
                print(self.scoreboard)

        elif self.player_throw == 'paper':

            if self.computer_throw == 'rock' or 'spock':
                print('{} trumps {}, you win the round!'.format(
                    self.player_throw, self.computer_throw))
                self.scoreboard['player'] += 1
                print(self.scoreboard)

            elif self.computer_throw == self.player_throw:
                print('The round is a tie!')

            else:
                print('{} is trumped by {}, you lose the round'.format(
                    self.player_throw, self.computer_throw))
                self.scoreboard['computer'] += 1
                print(self.scoreboard)

        elif self.player_throw == 'scissors':

            if self.computer_throw == 'paper' or 'lizard':
                print('{} trumps {}, you win the round!'.format(
                    self.player_throw, self.computer_throw))
                self.scoreboard['player'] += 1
                print(self.scoreboard)

            elif self.computer_throw == self.player_throw:
                print('The round is a tie!')

            else:
                print('{} is trumped by {}, you lose the round'.format(
                    self.player_throw, self.computer_throw))
                self.scoreboard['computer'] += 1
                print(self.scoreboard)

        elif self.player_throw == 'lizard':

            if self.computer_throw == 'paper' or 'spock':
                print('{} trumps {}, you win the round!'.format(
                    self.player_throw, self.computer_throw))
                self.scoreboard['player'] += 1
                print(self.scoreboard)

            elif self.computer_throw == self.player_throw:
                print('The round is a tie!')

            else:
                print('{} is trumped by {}, you lose the round'.format(
                    self.player_throw, self.computer_throw))
                self.scoreboard['computer'] += 1
                print(self.scoreboard)

        elif self.player_throw == 'spock':

            if self.computer_throw == 'rock' or 'scissors':
                print('{} trumps {}, you win the round!'.format(
                    self.player_throw, self.computer_throw))
                self.scoreboard['player'] += 1
                print(self.scoreboard)

            elif self.computer_throw == self.player_throw:
                print('The round is a tie!')

            else:
                print('{} is trumped by {}, you lose the round'.format(
                    self.player_throw, self.computer_throw))
                self.scoreboard['computer'] += 1
                print(self.scoreboard)

        else:
            print('That is not an approve throw.')

    def new_game_question(self):
        '''Determines if a new game will be played or not'''

        print('Thanks for playing! Wanna go again? ')

        while True:

            self.new_game_answer = str.lower(input())

            if self.new_game_answer != 'yes' or 'no':
                print('''I prefer yes and no answers only,
                please and thank you...''')

            elif self.new_game_answer == 'yes':

                for i in iter(self.scoreboard):
                    self.scoreboard[i] = 0
                print('Let us begin...')
                break

            else:
                break


def main():

    game = MyGame()
    game.game_start()
    game.game_rules()

    while True:

        game.make_throws()
        game.throw_match_up()
        if game.scoreboard['player'] == 3:

            print('You win!')
            game.match_score['player'] += 1
            print('The current match score is {}'.format(game.match_score))
            game.new_game_question()
            try:
                if game.new_game_answer == 'yes':
                    game.make_throws()
                    game.throw_match_up()

                else:
                    print('See you later')
                    sys.exit()
            except KeyboardInterrupt:
                if KeyboardInterrupt is True:
                    print('How abruptly rude...')
                    sys.exit()

        elif game.scoreboard['computer'] == 3:

            print('The computer won!')
            game.match_score['computer'] += 1
            print('The current match score is {}'.format(game.match_score))
            game.new_game_question()

            if game.new_game_answer == 'yes':

                game.make_throws()
                game.throw_match_up()

            else:
                break


if __name__ == '__main__':
    main()
