#!/Users/neevekadosh/anaconda3/bin/python3

class HangMan:
    def __init__(self):
        self.win = False
        self.done = False
        self.usedChars = []
        self.attempts = 0
        self.maxAttempts = 6 # stick figure amount
        self.correctGuesses = []
        self.display = ""
        self.saveDisplay = ""
        self.wordDict = {}

    def Run(self, word):
        
        wordList = list(word)
        word = set(word)

        print("Welcome to Hang Man!")
        print("  ________\n |       |\n |       |\n |\n |\n |\n |\n |\n________________\n")
        empty = ""
        for idx in range(len(wordList)):
            self.wordDict[idx] = " "
            empty += "_ "
        print("\n" + empty)
        
        while not self.done:
            char = input("Make a guess\n> ")
            # VerifyValid(char)
            if char not in self.usedChars:
                self.usedChars.append(char)
                print("Used characters: ", self.usedChars)
            else:
                self.attempts -= 1
                
            if char in word:
                word.remove(char)
                
                for idx, letter in enumerate(wordList):
                    if char == letter:
                        self.wordDict[idx] = char
                    else:
                        self.display += "  "
                self.display += ""
                text = ""
                for idx, key in enumerate(sorted(self.wordDict.keys())):
                    if idx == key:
                        text += self.wordDict[key] + " "
                    else:
                        text += "  "
                print("  ________\n |       |\n |       |\n |\n |\n |\n |\n |\n________________\n")
                print(text, "\n" + empty)

            self.GameOver(word)
            
    def Status(self):
        if self.win:
            print("Victory!")
        else:
            print("You lose :(")
    
    def GameOver(self, word):
        if len(word) == 0:
                self.win = True
                self.done = True
        if self.attempts >= self.maxAttempts:
            self.done = True
        else:
            self.attempts += 1

if __name__=="__main__":
    hangMan = HangMan()
    hangMan.Run("pal")
    hangMan.Status()
