from PySide6.QtWidgets import *
from PySide6.QtCore import *
from __feature__ import snake_case, true_property
import sys
from styles import game_style, player1_style, player2_style, title_style

current_player = "X"
player1_moves = set()
player2_moves = set()

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
        self.size =QSize(450,500)

        self.frame_titulo = QFrame()
        self.frame_buttons = QFrame()

        self.root_layout = QVBoxLayout()
        self.root_layout.add_widget(self.frame_titulo,30)
        self.root_layout.add_widget(self.frame_buttons,70)

        self.widget = QWidget()
        self.widget.set_layout(self.root_layout)

        self.set_central_widget(self.widget)
        self.setup_header_frame()
        self.setup_buttons_frame()
        self.style_sheet = game_style
    
    #------------------------------------

    def add_button_to_layout(self,row,column):
        coordinates = f'{row},{column}'
        button = QPushButton()
        button.clicked.connect(lambda: self.record_move(coordinates, button))
        self.game_button_layout.add_widget(button,row,column)

    #------------------------------------

    def setup_header_frame(self):
        self.header_label = QLabel(":D", alignment = Qt.AlignCenter)
        self.header_label.style_sheet = title_style
        self.header_label.word_wrap = True
        
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

    def record_move(self, coordinate, button):
        global current_player
        if(current_player == "X"):
            button.text = current_player
            button.style_sheet = player1_style
            player1_moves.add(coordinate)
            current_player = "O"

        else:
            button.text = current_player
            button.style_sheet = player2_style
            player2_moves.add(coordinate)
            current_player = "X"

        button.enabled = False
        button.style_sheet = button.style_sheet
        
        self.header_changer(self.game_win_check())
    
    #------------------------------------
    
    def game_win_check(self): # 0: still playing, 1: player1 won, 2: player2 won, 3: draw
        global winning_combinations
        
        for combo in winning_combinations:
            if (len(combo & player1_moves) == 3):   #player 1 wins
                return 1
            if (len(combo & player2_moves) == 3):   #player 2 wins
                return 2

        if(len(player1_moves) + len(player2_moves) == 9): #draw case
            return 3
        return 0       #nothing case

    #------------------------------------
    #this changes the "header" seccion

    def header_changer(self,gameStatus):
        #Still in game
        if gameStatus == 0:
            if current_player == "X":
                self.header_label.text = "Turno de Jugador 1"
                self.frame_titulo.style_sheet = player1_style
            else:
                self.header_label.text = "Turno de Jugador 2"
                self.frame_titulo.style_sheet = player2_style
        
        #End of game
        elif gameStatus == 3:
            self.header_label.text = "Empate!\nAmbos pierden :)"
            self.frame_titulo.style_sheet = "background: orange"
            
        
        #Someone won
        else:
            if gameStatus == 1:
                self.header_label.text = "Jugador 1 ganó el juego"
                self.frame_titulo.style_sheet = player1_style
                self.frame_buttons.enabled = False
            else:
                self.header_label.text = "Jugador 2 ganó el juego"
                self.frame_titulo.style_sheet = player2_style
                self.frame_buttons.enabled = False


#------------------------------------

#ejecutar app
app = QApplication(sys.argv)

menu = GameWindow()
menu.setup_ui()
menu.show()

sys.exit(app.exec())