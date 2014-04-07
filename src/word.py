class Word:
    def __init__(self, word=""):
        self.word = word
        self.revealed = []
        
    #Reveals a letter by adding it to the revealed list
    def reveal(self, letter):
        self.revealed.append(letter)
        
    #Returns a string representing the word according to the revealed letters
    def get_word_string(self):
        word_string = ""
        for c in self.word:
            if (c in self.revealed):
                word_string += c
            elif (c == " "):
                word_string += " "
            else:
                word_string += "_"
        return word_string
        
    def print_word(self):
        print(self.get_word_string())
        
    def is_fully_revealed(self):
        return self.get_word_string() == self.word