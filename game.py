from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QIcon

from __feature__ import snake_case, true_property
import sys
from styles import game_style, player1_style, player2_style, title_style, game_header_style

#from main import players_names
players_names = ["Jose","Pablo"]

class Player:
    def __init__(self, name, char,pstyle):
        self.letter = char
        self.name = name
        self.moves = set()
        self.style = pstyle

player1 = Player(players_names[0],"X",player1_style)
player2 = Player(players_names[1],"O",player2_style)

current_player = player1.letter

player1_moves = set()
player2_moves = set()
playable_buttons = set()

winning_combinations = [
    {'0,0', '0,1', '0,2'},
    {'1,0', '1,1', '1,2'},
    {'2,0', '2,1', '2,2'},
    {'0,0', '1,0', '2,0'},
    {'0,1', '1,1', '2,1'},
    {'0,2', '1,2', '2,2'},
    {'0,0', '1,1', '2,2'},
    {'0,2', '1,1', '2,0'},
]

class GameWindow(QMainWindow):

    def setup_ui(self):
        self.size =QSize(450,600)

        self.frame_titulo = QFrame()
        self.frame_buttons = QFrame()
        self.frame_options = QFrame()

        self.root_layout = QVBoxLayout()
        self.root_layout.add_widget(self.frame_titulo,24)
        self.root_layout.add_widget(self.frame_buttons,70)
        self.root_layout.add_widget(self.frame_options,6)

        self.widget = QWidget()
        self.widget.set_layout(self.root_layout)

        self.set_central_widget(self.widget)
        self.setup_header_frame()
        self.setup_buttons_frame()
        self.setup_options_frame()
        self.style_sheet = game_style
    
    #------------------------------------

    def add_button_to_layout(self,row,column):
        coordinates = f'{row},{column}'
        button = QPushButton()
        button.clicked.connect(lambda: self.record_move(coordinates, button))
        self.game_button_layout.add_widget(button,row,column)
        playable_buttons.add(button)

    #------------------------------------

    def setup_header_frame(self):
        self.header_label = QLabel(":D", alignment = Qt.AlignCenter)
        self.header_label.style_sheet = title_style
        
        
        self.header_layout = QVBoxLayout()
        self.header_layout.add_widget(self.header_label)

        self.frame_titulo.set_layout(self.header_layout)


    #------------------------------------

    def setup_buttons_frame(self):

        self.game_button_layout = QGridLayout()
        
        for i in range(3):
            for j in range(3):
                self.add_button_to_layout(i,j)
        
        self.frame_buttons.set_layout(self.game_button_layout)
        

    #------------------------------------

    def setup_options_frame(self):
        self.options_layout = QHBoxLayout()

        self.home_button = QPushButton()
        self.switch_roles_button = QPushButton()
        self.restart_button = QPushButton()

        for button in (self.home_button, self.switch_roles_button, self.restart_button):
            button.style_sheet = "height: 60%;"

        self.home_button.icon = QIcon("home-icon.png")
        self.home_button.icon_size = QSize(30, 30)
        self.switch_roles_button.icon = QIcon("switch-icon.png")
        self.switch_roles_button.icon_size = QSize(30, 30)
        self.restart_button.icon = QIcon("return-icon.png")
        self.restart_button.icon_size = QSize(30, 30)

        self.restart_button.clicked.connect(self.restart_logic)
        #self.switch_roles_button.clicked.connect(self.switch_roles)

        self.options_layout.add_widget(self.home_button)
        self.options_layout.add_widget(self.switch_roles_button)
        self.options_layout.add_widget(self.restart_button)

        self.frame_options.set_layout(self.options_layout)

    #------------------------------------

    def record_move(self, coordinate, button):
        global current_player
        if(current_player == player1.letter):
            button.text = current_player
            button.style_sheet = player1.style
            player1.moves.add(coordinate)
            current_player = player2.letter

        else:
            button.text = current_player
            button.style_sheet = player2.style
            player2.moves.add(coordinate)
            current_player = player1.letter

        button.enabled = False
        button.style_sheet = button.style_sheet
        
        self.header_changer(self.game_win_check())
    
    #------------------------------------
    
    def game_win_check(self): # 0: still playing, 1: player1 won, 2: player2 won, 3: draw
        global winning_combinations
        
        for combo in winning_combinations:
            if (len(combo & player1.moves) == 3):   #player 1 wins
                return 1
            if (len(combo & player2.moves) == 3):   #player 2 wins
                return 2

        if(len(player1.moves) + len(player2.moves) == 9): #draw case
            return 3
        return 0       #nothing case

    #------------------------------------
    #this changes the "header" seccion

    def header_changer(self,gameStatus):
        #Still in game
        if gameStatus == 0:
            if current_player == "X":
                self.header_label.text = f"Turno de {player1.name}"
                self.frame_titulo.style_sheet = player1.style
            else:
                self.header_label.text = f"Turno de {player2.name}"
                self.frame_titulo.style_sheet = player2.style
        
        #End of game
        elif gameStatus == 3:
            self.header_label.text = "Empate!\nAmbos pierden :)"
            self.frame_titulo.style_sheet = "background: orange"
            
        
        #Someone won
        else:
            if gameStatus == 1:
                self.header_label.text = f"{player1.name} ganó el juego"
                self.frame_titulo.style_sheet = player1.style
                self.frame_buttons.enabled = False
            else:
                self.header_label.text = f"{player2.name} ganó el juego"
                self.frame_titulo.style_sheet = player2.style
                self.frame_buttons.enabled = False
    
    #------------------------------------

    def restart_logic (self):
        global playable_buttons
        self.frame_buttons.enabled = True
        for button in playable_buttons:
            button.enabled = True
            button.style_sheet=game_style
            button.text = ""

        global player1
        global player2

        player1.moves = set()
        player2.moves = set()

        self.frame_titulo.style_sheet = game_header_style
        self.header_label.text = ":D"

    # def switch_roles(self):
    #         temporal = player1.letter

    #         player1.letter = player2.letter
    #         player2.letter = temporal

    #         temporal = player1.style
    #         player1.style = player2.style
    #         player2.style = temporal


#------------------------------------

#ejecutar app
app = QApplication(sys.argv)

menu = GameWindow()
menu.setup_ui()
menu.show()

sys.exit(app.exec())