from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from _42db2ui import Ui_MainWindow
import sys
import random



deck=["maca1","maca2","maca3","maca4","maca5","maca6","maca7","maca8","maca9","maca10","macak","macaq","macaj",
"sinek1","sinek2","sinek3","sinek4","sinek5","sinek6","sinek7","sinek8","sinek9","sinek10","sinekk","sinekj","sinekq",
"kupa1","kupa2","kupa3","kupa4","kupa5","kupa6","kupa7","kupa8","kupa9","kupa10","kupak","kupaj","kupaq",
"karo1","karo2","karo3","karo4","karo5","karo6","karo7","karo8","karo9","karo10","karok","karoj","karoq"]

def createDeck(deck):
    deckrange=random.randint(10,12)
    deck*=deckrange

    random.shuffle(deck)
    return deck[:int(len(deck)/2)]

class App(QMainWindow):

    def __init__(self):
        super(App,self).__init__()
        self.ui=Ui_MainWindow()
        self.pcScore=0
        self.playerScore=0
        self.hitcount=1
        self.playerAcount=0
        self.pcAcount=0
        self.ui.setupUi(self)
        self.ui.stand.clicked.connect(self.stand)
        self.ui.hitbtn.clicked.connect(self.hit)
        self.ui.restartbtn.clicked.connect(self.restart)

    def startGame(self,playableDeck):
        self.ui.restartbtn.setVisible(False)
        self.ui.pcCard1.setPixmap(QPixmap("deck-images/"+str(self.hitCard(playableDeck,"0"))+".jpg"))
        self.ui.pcCard2.setPixmap(QPixmap("deck-images/arka.jpg"))
        self.ui.playerCard1.setPixmap(QPixmap("deck-images/"+str(self.hitCard(playableDeck,"1"))+".jpg"))
        self.ui.playerCard2.setPixmap(QPixmap("deck-images/"+str(self.hitCard(playableDeck,"1"))+".jpg"))
        if self.playerScore==21:
            self.gameOver()
    
    def restart(self):
        self.pcScore=0
        self.playerScore=0
        self.hitcount=1
        self.playerAcount=0
        self.pcAcount=0
        
        self.ui.pcCard1.setPixmap(QPixmap("deck-images/arka.jpg"))
        self.ui.pcCard2.setPixmap(QPixmap("deck-images/arka.jpg"))
        self.ui.pcCard3.setPixmap(QPixmap("null.jpg"))
        self.ui.pcCard4.setPixmap(QPixmap("null.jpg"))
        self.ui.pcCard5.setPixmap(QPixmap("null.jpg"))
        self.ui.pcCard6.setPixmap(QPixmap("null.jpg"))
        self.ui.pcCard7.setPixmap(QPixmap("null.jpg"))

        self.ui.playerCard1.setPixmap(QPixmap("deck-images/arka.jpg"))
        self.ui.playerCard2.setPixmap(QPixmap("deck-images/arka.jpg"))
        self.ui.playerCard3.setPixmap(QPixmap("null.jpg"))
        self.ui.playerCard4.setPixmap(QPixmap("null.jpg"))
        self.ui.playerCard5.setPixmap(QPixmap("null.jpg"))
        self.ui.playerCard6.setPixmap(QPixmap("null.jpg"))
        self.ui.playerCard7.setPixmap(QPixmap("null.jpg"))

        self.ui.hitbtn.setVisible(True)
        self.ui.stand.setVisible(True)
        self.ui.restartbtn.setVisible(False)

        self.ui.sonuc.setText("")
        self.startGame(playableDeck)



    def stand(self):
        pcCards=[self.ui.pcCard2,self.ui.pcCard3,self.ui.pcCard4,self.ui.pcCard5,self.ui.pcCard6,self.ui.pcCard7]

        for i in pcCards:
            i.setPixmap(QPixmap("deck-images/"+str(self.hitCard(playableDeck,"0"))+".jpg"))
            if self.pcScore>=17:
                break
        
        self.gameOver()
        
    def hit(self):
        playerCards=[self.ui.playerCard3,self.ui.playerCard4,self.ui.playerCard5,self.ui.playerCard6,self.ui.playerCard7]

        playerCards[self.hitcount-1].setPixmap(QPixmap("deck-images/"+str(self.hitCard(playableDeck,"1"))+".jpg"))
        if self.playerScore>=21:
            self.gameOver()
        self.hitcount+=1



    def gameOver(self):
        self.ui.hitbtn.setVisible(False)
        self.ui.stand.setVisible(False)
        self.ui.restartbtn.setVisible(True)


        if self.playerScore> self.pcScore and self.playerScore<=21:
            self.ui.sonuc.setText("you win!")
        elif self.playerScore < self.pcScore and self.pcScore<=21:
            self.ui.sonuc.setText("you lose!")
        elif self.playerScore>21:
            self.ui.sonuc.setText("you lose!")
        elif self.pcScore>21:
            self.ui.sonuc.setText("you win!")
        elif self.playerScore == self.pcScore:
            self.ui.sonuc.setText("draw!")

        



    def hitCard(self,playableDeck,hittedBy):
        
        self.currentCard = playableDeck.pop()

        if self.currentCard[-1]=="k" or self.currentCard[-1]=="j" or self.currentCard[-1]=="q" or self.currentCard[-1]=="0":
            self.numberToAdd=10

        elif self.currentCard[-1]=="1":
            self.numberToAdd=11
            if hittedBy=="1":
                self.playerAcount+=1
            else:
                self.pcAcount+=1


        else:
            self.numberToAdd=int(self.currentCard[-1])
            

        if hittedBy=="1":
            self.playerScore+=self.numberToAdd
            if self.playerScore>21 and self.playerAcount>0:
                self.playerScore-=10
                self.playerAcount-=1
        else:
            self.pcScore+=self.numberToAdd
            if self.pcScore>21 and self.pcAcount>0:
                self.pcScore-=10
                self.pcAcount-=1

        self.ui.playertxt.setText("you "+str(self.playerScore))
        self.ui.kasatxt.setText("dealer "+str(self.pcScore))
        self.ui.kalankarttxt.setText(str(len(playableDeck))+" cards left")
        return self.currentCard
        


app=QApplication(sys.argv)
win=App()
win.show()


playableDeck=createDeck(deck)
win.startGame(playableDeck)

sys.exit(app.exec_())





