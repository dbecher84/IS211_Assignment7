#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""______doc string_________"""

import random
import sys

random.seed(0)


class Player(object):
    """defines a player for the game"""
    def __init__(self, player_num):
        """player constructor"""
        self.player_id = player_num
        self.roll = True
        self.total_score = 0

    def hold_roll(self):
        """is player rolling or holding"""
        try:
            choice = raw_input('Are you going to hold (h) or roll (r)? ')
            if choice not in ('h', 'r'):
                raise ValueError
            if choice.lower() == 'h':
                self.roll = False
                print 'Turn ended.'
            if choice.lower() == 'r':
                self.roll = True
                print 'Rolling again.'
        except ValueError:
            print 'Not a valid option. Must be h or r.'
            self.hold_roll()


class Dice(object):
    """defines the dice for the game"""
    def __init__(self):
        """dice constructor"""
        self.rolled_value = None

    def roll(self):
        """random number from 1-6 for dice value"""
        self.rolled_value = random.randint(1, 6)
        return self.rolled_value


class Continue(object):
    """Continue or end game class"""
    def __init__(self):
        """Conintue constructor"""
        self.go_on = False

    def replay_game(self):
        """function to continue or end game"""
        try:
            play_more = raw_input('Would you like to play again? y/n ')
            if play_more.lower() not in ('y', 'n'):
                raise ValueError
            if play_more.lower() == 'y':
                self.go_on = True
            if play_more.lower() == 'n':
                self.go_on = False
        except ValueError:
            print 'Not a valid option. Must be y or n.'
            self.replay_game()


class Game(object):
    """sets up the game"""
    def __init__(self, list_players):
        """constructor for Game"""
        self.player_list = list_players
        self.win_score = 100
        #determines starting player. proceeds in order after that.
        self.starting_player = random.randint(1, (len(self.player_list) - 1))
        self.next_player = None
        self.dice = Dice()
        self.more_play = Continue()

        self.current_player = self.player_list[self.starting_player]
        print 'Player {} will go first'.format(self.current_player.player_id)

        self.start_turn(self.current_player)


    def turn_change(self, player):
        """changes the current player"""
        if player.total_score >= self.win_score:
            print 'Player {} has won!'.format(player.player_id)
            self.more_play.replay_game()
            if self.more_play.go_on is True:
                start_game()
            if self.more_play.go_on is False:
                sys.exit

        else:
            if player.player_id == len(self.player_list):
                self.starting_player = 0
                self.current_player = self.player_list[0]
                self.start_turn(self.current_player)
            else:
                self.starting_player += 1
                self.current_player = self.player_list[self.starting_player]
                self.start_turn(self.current_player)


    def start_turn(self, player):
        """turn for player"""
        turn_score = 0
        count = len(self.player_list) - 1
        print "The current score are."
        while count >= 0:
            print "Player {}'s total score is {}.".format(self.player_list[count].player_id,
                                                        self.player_list[count].total_score)
            count -= 1#prints all current total scores
        print "It is player {}'s turn.".format(player.player_id)

        player.roll = True
        while player.roll:

            die_num = self.dice.roll()

            if die_num == 1:
                print 'You rolled 1 no points gained this time.'
                player.roll = False
                turn_score = 0

            else:
                turn_score = turn_score + die_num
                print 'You rolled {}'.format(self.dice.rolled_value)
                print 'Your score this round is {}'.format(turn_score)
                print 'Your score for the game is {}'.format(player.total_score)
                player.hold_roll()

        player.total_score += turn_score
        print 'Your total score is now {}.'.format(player.total_score)

        self.turn_change(player)#switch to next player


def start_game():
    """starts a game"""
    try:
        number_of_players = int(raw_input('Enter the number of players for the game. '))
    except ValueError:
        print 'Input must be a number.'
        start_game()
    player_list = []
    for num in range(number_of_players):
        player_list.append(Player(num + 1))

    Game(player_list)


if __name__ == '__main__':
    start_game()
