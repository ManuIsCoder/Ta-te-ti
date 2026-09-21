from PySide6.QtWidgets import *
from PySide6.QtCore import *
from __feature__ import snake_case, true_property
import sys
from styles import game_style

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
    
    def setup_buttons_frame(self):

        self.ButtonA1 = QPushButton()
        self.ButtonA2 = QPushButton()
        self.ButtonA3 = QPushButton()

        self.ButtonB1 = QPushButton()               
        self.ButtonB2 = QPushButton()
        self.ButtonB3 = QPushButton()

        self.ButtonC1 = QPushButton()
        self.ButtonC2 = QPushButton()
        self.ButtonC3 = QPushButton()

        self.game_button_layout = QGridLayout()

        buttons_list = [[self.ButtonA1, self.ButtonA2, self.ButtonA3],
                        [self.ButtonB1, self.ButtonB2, self.ButtonB3],
                        [self.ButtonC1, self.ButtonC2, self.ButtonC3]]
        
        
        for i in range(3):
            for j in range(3):
                self.game_button_layout.add_widget(buttons_list[i][j],i,j)
        
        self.frame_buttons.set_layout(self.game_button_layout)

#------------------------------------

#ejecutar app
app = QApplication(sys.argv)

menu = GameWindow()
menu.setup_ui()
menu.show()

sys.exit(app.exec())