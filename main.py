from PySide6.QtWidgets import *
from PySide6.QtCore import *
from __feature__ import snake_case, true_property
import sys
from styles import menu_style, title_style

class Menu(QMainWindow):
    def setup_ui(self):
        self.size = QSize(450,500)
        self.root_layout = QVBoxLayout()

        self.frame_titulo = QFrame()
        self.frame_titulo.style_sheet = menu_style
        self.frame_input = QFrame()
        self.frame_input.style_sheet = menu_style


        self.root_layout.add_widget(self.frame_titulo,30)
        self.root_layout.add_widget(self.frame_input,70)

        self.widget = QWidget()
        self.widget.set_layout(self.root_layout)

        self.set_central_widget(self.widget)
        self.setup_inputs_frame()
        self.setup_title_frame()

    #------------------------------------


    def setup_inputs_frame(self):
        self.titulo_inputs = QLabel("Ingrese el nombre de los jugadores", alignment = Qt.AlignCenter)
        self.player1 = QLineEdit(alignment = Qt.AlignCenter,placeholder_text="Jugador 1")
        self.player2 = QLineEdit(alignment = Qt.AlignCenter,placeholder_text="Jugador 2")
        self.start_button = QPushButton("Iniciar")

        self.start_button.clicked.connect(self.get_player_names)

        self.titulo_inputs.style_sheet= menu_style

        self.start_button.style_sheet = menu_style

        self.player1.style_sheet = menu_style
        self.player2.style_sheet = menu_style

        self.inputs_layout = QVBoxLayout()

        widgets = [self.titulo_inputs,self.player1,self.player2,self.start_button]

        for wd in widgets:
            self.inputs_layout.add_widget(wd)
            self.inputs_layout.add_spacing(10)
        self.inputs_layout.add_stretch()

        self.frame_input.set_layout(self.inputs_layout)
    
    #------------------------------------

    def setup_title_frame (self):
        self.title_title = QLabel("TA-TE-TI", alignment = Qt.AlignCenter)
        
        self.title_title.style_sheet = "color: black;font-size: 50px;font-weight: bold;"

        self.title_layout = QVBoxLayout()
        self.title_layout.add_widget(self.title_title)
        #self.title_layout.add_stretch()


        self.frame_titulo.set_layout(self.title_layout)
    
    #------------------------------------
    #Verifica si los jugadores tienen nombre

    def get_player_names (self):
        if (self.player1.text and self.player2.text != ""):
            print(f"Jugador1: {self.player1.text}\nJugador 2: {self.player2.text}")
        else:
            print("No name input")


#------------------------------------

#ejecutar app
app = QApplication(sys.argv)

menu = Menu()
menu.setup_ui()
menu.show()

sys.exit(app.exec())