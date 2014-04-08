from player import Player
from util import get_choice, format_points
from word import Word

MAX_GUESSES = 9

class Game:
    def __init__(self):
        self.players = []
        self.guessed = False
        self.num_players = 0
        self.current_word = Word()
        self.guesses = 0
    
    def end_game(self):
        #Creates a list of winners (players with the highest score)
        winners = [self.players[0]]
        for player in self.players:
            for winner in winners:
                if player != winner and player.score > winner.score:
                    winners = [player]
                    break
                elif player != winner and player.score == winner.score:
                    winners.append(player)
                    break
                
        if (len(winners) == 1): print(str(winners[0]) + " wins the game with " + format_points(winners[0].score) + "!")
        else:
            print("Tied winners!")
            to_print = ""
            for winner in winners: to_print += str(winner) + " - " + format_points(winner.score) + "\n"
            print(to_print)
            
        print("Thanks for playing PyHang by Norbo11!")
            
    def shift_leader(self):
        #Assigns the first player to be the leader if the new index exceeds the allowable range, otherwise it just assings the a player with the new index
        new_index = self.players.index(self.current_leader) + 1
        self.current_leader = self.players[0] if new_index > len(self.players) - 1 else self.players[new_index]
    
    def clear_vars(self):
        self.guessed = False
        self.eliminated = []
        self.shift_leader()
    
    def welcome(self):
        print("Welcome to Norbo11's PyHang!")
        while (self.num_players > 5 or self.num_players < 2):
            print("Enter number of players (2-5): ")
            self.num_players = int(input())
        
        for i in range(1, self.num_players + 1):
            print("Enter Player " + str(i) + " name:") 
            self.players.append(Player(self, input()))
    
        self.current_leader = self.players[0]
        
    def loop(self):
        #Main loop
        while (True):
            print(str(self.current_leader) + ", pick a word!")
            self.current_word = Word(input())
            self.guesses = MAX_GUESSES
            print("\n"*20)
            
            while (True):
                #Loop through players which are non-leaders
                for player in [player for player in self.players if player != self.current_leader]:
                    if (self.guesses > 0):
                        self.current_word.print_word()
                        player.turn(self.current_word)
                    else:
                        print("No guesses left, " + str(self.current_leader) + " +3 points!")
                        self.current_leader.score += 3
                        break
                    if (self.guessed): 
                        break
                else:
                    continue; #Executed if the loop finished without breaking
                break #This never gets called until the above "continue" isn't called (which happens when break is called within the inner loop)
            
            print("Keep playing? y/n")
            
            choice = get_choice(("y","n"))
            if (choice == "n"):
                self.end_game()
                break
            elif (choice == "y"):
                self.clear_vars()
                continue