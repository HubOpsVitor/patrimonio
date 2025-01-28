from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sys

class CadastroLocalizacoes(QWidget):
    def __init__(self):
        super().__init__()
        # Vamos definir a posição e o tamanho da tela
        self.setGeometry(500, 200, 550, 300)
        # Agora o título da janela
        self.setWindowTitle("Cadastrar Localizações dos Patrimônios")

        # Gerenciador de layout vertical
        self.layout_v = QVBoxLayout()

        # Labels e LineEdits para os dados do patrimônio
        self.label_id = QLabel("ID do Patrimônio:")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_id = QLineEdit()

        self.label_num_empresa = QLabel("Empresa onde se encontra:")
        self.label_num_empresa.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_num_empresa = QLineEdit()

        self.label_logradouro = QLabel("Logradouro:")
        self.label_logradouro.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_logradouro = QLineEdit()

        self.label_numero = QLabel("Número:")
        self.label_numero.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_numero = QLineEdit()

        self.label_predio = QLabel("Prédio onde se encontra (se houver):")
        self.label_predio.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_predio = QLineEdit()

        self.label_andar = QLabel("Andar onde se encontra (se houver):")
        self.label_andar.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_andar = QLineEdit()

        self.label_data_sala = QLabel("Sala:")
        self.label_data_sala.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_data_sala = QLineEdit()

        # Adicionar as widgets ao layout
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)
        self.layout_v.addWidget(self.label_num_empresa)
        self.layout_v.addWidget(self.edit_num_empresa)
        self.layout_v.addWidget(self.label_logradouro)
        self.layout_v.addWidget(self.edit_logradouro)
        self.layout_v.addWidget(self.label_numero)
        self.layout_v.addWidget(self.edit_numero)
        self.layout_v.addWidget(self.label_predio)
        self.layout_v.addWidget(self.edit_predio)
        self.layout_v.addWidget(self.label_andar)
        self.layout_v.addWidget(self.edit_andar)
        self.layout_v.addWidget(self.label_data_sala)
        self.layout_v.addWidget(self.edit_data_sala)
        
        # Botão de cadastro
        self.button = QPushButton("Cadastrar")
        self.button.clicked.connect(self.cadastrar)
        self.button.setStyleSheet("QPushButton{background-color:navy;color:white;font-size:12pt;font-weight:bold}")
        self.layout_v.addWidget(self.button)

        # Definir o layout da janela
        self.setLayout(self.layout_v)

    def cadastrar(self):
        if(self.edit_id.text()=="" or 
        self.edit_num_empresa.text()=="" or 
        self.edit_logradouro.text()=="" or
        self.edit_numero.text()=="" or
        self.edit_predio.text()=="" or
        self.edit_andar.text()=="" or
        self.edit_predio.text()=="" or
        self.edit_data_sala.text()==""):
            QMessageBox.critical(self,"Erro","Você deve preencher todas as informações para fazer o cadastro!")
        
        else:
  
        # Vamos criar uma variável que fará referência ao arquivo de texto
            with open("localizacao.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"ID: {self.edit_id.text()}\n")
                arquivo.write(f"Empresa: {self.edit_num_empresa.text()}\n")
                arquivo.write(f"Logradouro: {self.edit_logradouro.text()}\n")
                arquivo.write(f"Número: {self.edit_numero.text()}\n")
                arquivo.write(f"Prédio: {self.edit_predio.text()}\n")
                arquivo.write(f"Andar: {self.edit_andar.text()}\n")
                arquivo.write(f"Sala: {self.edit_data_sala.text()}\n")
                arquivo.write("------------------------------------------\n")
                QMessageBox.information(self,"Salvo","Os dados da localização patrimônio foram salvos")


app = QApplication(sys.argv)
# Instância da classe Cadastro Localizações
# para iniciar a janela
tela = CadastroLocalizacoes()
# Exibir a tela durante a execução
tela.show()
# Ao clicar no botão, fechar a tela
# deve fechar e sair da memória
app.exec()