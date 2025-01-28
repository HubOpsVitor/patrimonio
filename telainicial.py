from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys
from patrimonio import CadastroPatrimonio
from localizacoes import CadastroLocalizacoes

class TelaInicial(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciar")
        self.setGeometry(300, 200, 200, 150)
        self.layout_v = QVBoxLayout()

        self.label_titulo = QLabel("Clique para abrir a janela")
        self.button_patrimonio = QPushButton("Abrir Patrimônio")
        self.button_localizacoes = QPushButton("Abrir Localizações de Patrimônio")

        self.layout_v.addWidget(self.label_titulo)
        self.layout_v.addWidget(self.button_localizacoes)
        self.layout_v.addWidget(self.button_patrimonio)

        self.button_patrimonio.clicked.connect(self.abrir_cadastro) 
        self.button_localizacoes.clicked.connect(self.abrir_localizacoes)

        self.setLayout(self.layout_v)

    def abrir_cadastro(self):
        self.pat = CadastroPatrimonio() 
        self.pat.show()
    
    def abrir_localizacoes(self):
        self.loc = CadastroLocalizacoes()
        self.loc.show()

app = QApplication(sys.argv)
tela = TelaInicial()
tela.show()
app.exec_()
