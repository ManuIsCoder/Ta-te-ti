from PySide6.QtWidgets import *
from PySide6.QtCore import *
from __feature__ import snake_case, true_property
import sys
from styles import game_style

current_player = "X"

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
        self.setup_buttons_frame()
        self.style_sheet = game_style
    
    #------------------------------------

    def add_button_to_layout(self,row,column):
        coordinates = f'{row},{column}'
        button = QPushButton()
        button.clicked.connect(lambda: self.record_move(coordinates, button))
        self.game_button_layout.add_widget(button,row,column)

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
        if(current_player == "X" and button.text==""):
            button.text = current_player
            button.style_sheet = "background: green"
            current_player = "O"
        elif(current_player == "O" and button.text==""):
            button.text = current_player
            button.style_sheet = "background: blue"
            current_player = "X"
        else:
            print("No se puede jugar en esa posicion")
        print("Click",coordinate)

#------------------------------------

#ejecutar app
app = QApplication(sys.argv)

menu = GameWindow()
menu.setup_ui()
menu.show()

sys.exit(app.exec())