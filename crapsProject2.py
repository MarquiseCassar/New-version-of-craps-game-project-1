#!/usr/bin/env python

from die import *
import sys
import crapsResources_rc
from time import sleep
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import  QMainWindow, QApplication

startingBankDefault = 100
maxinumBetDefault = 100
logFilenameDefault = "craps.log"

class Craps(QMainWindow) :
    """A game of Craps."""
    die1 = die2 = None

    def __init__( self, parent=None ):
        """Build a game with two dice."""

        super().__init__(parent)
        uic.loadUi("Craps.ui", self)

        self.bidSpinBox.setRange ( 10, 100 )
        self.bidSpinBox.setSingleStep ( 5 )

        self.die1 = Die()
        self.die2 = Die()

        self.buttonText = "Roll"

             #          0  1  2  3  4    5    6    7    8    9    10   11   12
        self.payouts = [0, 0, 0, 0, 2.0, 1.5, 1.2, 1.0, 1.2, 1.5, 2.0, 1.0, 0]

        self.restoreSettings()

        self.restartGame()

        self.rollButton.clicked.connect(self.rollButtonClickedHandler)
        self.preferenceSelectButton.clicked.connect(self.preferencesSelectButtonClickedHandler)

    def __str__( self ):
        """String representation for Dice.
        """

        return "Die1: %s\nDie2: %s" % ( str(self.die1),  str(self.die2) )

    def updateUI ( self ):
        print("Die1: %i, Die2: %i" % (self.die1.getValue(),  self.die2.getValue()))
        self.bidSpinBox.setRange(self.minimunBet, self.maxiimunBet)
        self.die1View.setPixmap(QtGui.QPixmap( ":/" + str( self.die1.getValue() ) ) )
        self.die2View.setPixmap(QtGui.QPixmap( ":/" + str( self.die2.getValue() ) ) )
        if self.firstRoll == True:
            self.rollingForLabel.setText("")
        else:
            self.rollingForLabel.setText(str("%i" % self.newWinner))
        #if self.results is not "":
            #self.resultsLabel.setText(self.results;
            #sleep(4)
            #self.results = ""
        self.resultsLabel.setText(self.results)
        self.rollButton.SetText(self.buttonText)
        self.winsLabel.setText(str("%i" % self.losses))
        self.bankValue.setText(str("%i" % self.currentBank))

    def restoreSettings(self):
        # Restore settings values, write defaults to any that don't already exist.
        if self.appSettings.contains('logFile'):
            self.logFilename = self.appSettings.value('logFile', type=str)
        else:
            self.logFilename = 'pythonGraderLog.txt'
            self.appSetting = self.appSetting.value('pickleFilename', type=str)

        if self.appSettings.contains('pickleFilename'):
            self.pickleFilename = self.appSetting.value('pickleFilename', type=str)
        else:
            self.pickleFilename = ".crapsSavedObjects.pl"
            self.appSetting.setValue('pickleFilename', self.pickleFilename)

        # Add your code here to update the GUI view so it matches the game state.

        from random import randint

        def do_roll():
            return randint(1, 6) + randint(1, 6)

        def craps():
            first = do_roll()
            if first in {2, 3, 12}:
                return 0

    def restoreSetting(self):
        # Restore settings values, write defaults to any that don't alreay exist.
        if self.appSetting.contains('startingBank'):
            self.startingBank = self.appSetting.value('startingBank', type=int)
        else:
            self.startingBank = startingBankDefault
            self.appSetting.setValue('startingBank', self.startingBank )

        if self.appSetting.contains('maxinumBet'):
            self.maximumBet = self.appSetting.value('maximumBet', type=int)
        else:
            self.maximumBet = maxinumBetDefault
            self.appSetting.setValue('maximumBet', self.maximumBet )

        if self.appSetting.contains('createLogFile'):
            self.createLogFile = self.appSetting.value('createLogFile', typ=bool)
        else:
            self.createLogFile = logFilenameDefault
            self.appSetting.setValue('createLogFile', self.createLogFile)

    @pyqtSlot()        # Player asked for another roll of the dice.
    def rollButtonClickedHandler ( self ):
        self.currentBet = self.bidSpinBox.value()
        # play the first roll
        self.results = ""
        if self.firstRoll:
            self.die1.roll()
            self.die2.roll()
            if (self.die1.getValue() + self.die2.getValue()) == 7 or (self.die1.getValue() + self.die2.getValue()) == 11:
                self.results = "Craps, You win!"
                self.wins += 1
                self.firstRoll = True
            elif self.die1.getvalue() + self.die2.getValue() == 2 or self.die1getValue() + self
               or self.die1.getValue() + self.die2.getValue() == 12:
            self,results = "You lose!"
            self.losses += 1
            self.firstRoll = True
            self.currentBank -= self.currentBet
        else:
            self.firsrRollValue = self.die1.getValue() + self.die2getValue()
            self.firstRoll = False
            self.buttonText = "Roll Again"
        else:
        self.firstRollValue = self.die1.getValue() + self.die2.getValue()
        self.firstRoll = False
        self.buttonText = "Roll Again"
        else:
            # Play the following rolls
            self.die1.roll()

        def craps():
            first = 'do_roll'()
            if first in {2, 3, 12}:
                return 0

        # Play the first roll
        pass            # Replace this line with your roll event handler
        self.updateUI()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    diceApp = Craps()
    diceApp.updateUI()
    diceApp.show()
    sys.exit(app.exec_())


