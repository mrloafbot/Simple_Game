import os

### this is a simple game for trying new ideas 

class user():
    def __init__(self):
        self.score = 0
        self.userName = raw_input("Whats your name?")
        self.round = 0
        
        
class question():
    def __init__(self):
        pass
    
    def getQuestion(self):
        ### eventually read an xml file here ###
        self.question = "What is your favorite color?"
        self.anwser = "Blue"
        
    def askQuestion(self):
        print self.question
        self.userAnwser = raw_input ("your anwser:")
        if self.userAnwser == self.anwser:
            return 1
        else:
            return 0
            
    def checkQuestion(self):
        print self.userAnwser, self.anwser
        if self.userAnwser == self.anwser:
            return 1
        else:
            return 0
    
    
class game():
    def __init__(self):
        print "Welcome to my stupid game"
        self.maxScore = 2
        self.player = user()
        self.quest = question()
        
    def update(self):
        """  create working game loop here """
        # gather users
        # gather questions
        
    def play(self):
        while self.player.score < self.maxScore:
            self.quest.getQuestion()
            checkAnwser = self.quest.askQuestion()
            if checkAnwser == 1:
                self.player.score += 1
                print "Correct!, your score is:", self.player.score
            elif checkAnwser == 0:
                print "Incorrect! Try again"
        if self.player.score == self.maxScore:
            print self.player.userName, "has won!"


def main():
    newGame = game()
    newGame.play()
    
if __name__=="__main__":
    main()
