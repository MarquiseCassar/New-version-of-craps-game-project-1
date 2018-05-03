_author_ = "Marquise Cassar"
#!/usr/bin/env python

from sys import path
from die import *
import sys
import crapsResources_rc
from time import sleep
from logging import basicConfig, getLogger, DEBUG, INFO, CRITICAL
from pickle import dump, load
from os import path
from PyQt5.QtCore import pyqtSlot, QSettings, Qt, Qtimer, QCoreApplication
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox

startingBankDefault = 100
maxiumumBetDefault = 100
minimumBetDefault = 10
logFilename = 'craps.log'
pickleFilenameDefault = "crapsSavedObjects.pl"

class Craps(QMainWindow) :
    """A game of Craps."""
    die1 = die2 = None

    def __init__( self, parent=None ):
        """Build a game with two dice."""

        super().__init__(parent)

        self.logger = getLogger("Marquise.craps")
        self.appSetting = QSettings()
        self.quitCounter = 0; # used in a workaround for a QT5 bug

        .c. loadUi("Craps.ui", self)


        self.bidSpinBox.setRange ( 10, 100 )
        self.bidSpinBox.setSingleStep ( 5 )

        self.die1 = Die()
        self.die2 = Die()

        self.buttonText = "Roll"

             #          0  1  2  3  4    5    6    7    8    9    10   11   12
        self.payouts = [0, 0, 0, 0, 2.0, 1.5, 1.2, 1.0, 1.2, 1.5, 2.0, 1.0, 0]

        self.rollButton.clicked.connect(self.rollButtonClickedHandler)

    def __str__( self ):
        """String representation for Dice.
        """

        return "Die1: %s\nDie2: %s" % ( str(self.die1),  str(self.die2) )

    def updateUI ( self ):
        print("Die1: %i, Die2: %i" % (self.die1.getValue(),  self.die2.getValue()))
        self.die1View.setPixmap(QtGui.QPixmap( ":/" + str( self.die1.getValue() ) ) )
        self.die2View.setPixmap(QtGui.QPixmap( ":/" + str( self.die2.getValue() ) ) )
        # Add your code here to update the GUI view so it matches the game state.

        from random import randint

        def do_roll():
            return randint(1, 6) + randint(1, 6)

        def craps():
            first = do_roll()
            if first in {2, 3, 12}:
                return 0
            # Player asked for another roll of the dice.
    def rollButtonClickedHandler ( self ):
        self.currentBet = self.bidSpinBox.value()

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


