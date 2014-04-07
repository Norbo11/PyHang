class Player:
    def __init__(self, game, name=""):
        self.game = game
        self.name = name
        self.score = 0
        
    def __str__(self):
        return self.name
    
    def turn(self, word):
        print(str(self) + ", type either your guess or a letter (" + str(self.game.guesses) + " guesses left): ")
        guess = input()
        
        #Reveals a given letter of a word or checks for win if a word was typed
        if (len(guess) == 1):
            word.reveal(guess)
            if (word.is_fully_revealed()):
                self.win()
        elif (word.word == guess):
            self.win()
            
        self.game.guesses -= 1
        
    def win(self):
        print(str(self) + " has guessed the word, +1 point!")
        self.game.guessed = True
        self.score += 1