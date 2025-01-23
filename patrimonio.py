from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys

class CadastroPatrimonio(QWidget):
    def __init__(self):
        super().__init__()
        # vamos definir a posição e o tamanho da tela
        self.setGeometry(500, 200, 550, 300)
        # agora o título da janela
        self.setWindowTitle("Cadastrar Patrimônio")

        # Gerenciador de layout vertical
        self.layout_v = QVBoxLayout()

        # Labels e LineEdits para os dados do patrimônio
        self.label_id = QLabel("ID do Patrimônio:")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_id = QLineEdit()

        self.label_num_serie = QLabel("Número de Série:")
        self.label_num_serie.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_num_serie = QLineEdit()

        self.label_nome = QLabel("Nome do Patrimônio:")
        self.label_nome.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_nome = QLineEdit()

        self.label_tipo = QLabel("Tipo do Patrimônio:")
        self.label_tipo.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_tipo = QLineEdit()

        self.label_descricao = QLabel("Descrição do Patrimônio:")
        self.label_descricao.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_descricao = QLineEdit()

        self.label_localizacao = QLabel("Localização do Patrimônio:")
        self.label_localizacao.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_localizacao = QLineEdit()

        self.label_data_fabricacao = QLabel("Data de Fabricação:")
        self.label_data_fabricacao.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_data_fabricacao = QLineEdit()

        self.label_data_aquisicao = QLabel("Data de Aquisição:")
        self.label_data_aquisicao.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_data_aquisicao = QLineEdit()

        # Adicionar as widgets ao layout
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)
        self.layout_v.addWidget(self.label_num_serie)
        self.layout_v.addWidget(self.edit_num_serie)
        self.layout_v.addWidget(self.label_nome)
        self.layout_v.addWidget(self.edit_nome)
        self.layout_v.addWidget(self.label_tipo)
        self.layout_v.addWidget(self.edit_tipo)
        self.layout_v.addWidget(self.label_descricao)
        self.layout_v.addWidget(self.edit_descricao)
        self.layout_v.addWidget(self.label_localizacao)
        self.layout_v.addWidget(self.edit_localizacao)
        self.layout_v.addWidget(self.label_data_fabricacao)
        self.layout_v.addWidget(self.edit_data_fabricacao)
        self.layout_v.addWidget(self.label_data_aquisicao)
        self.layout_v.addWidget(self.edit_data_aquisicao)

        # Botão de cadastro
        self.button = QPushButton("Cadastrar")
        self.button.clicked.connect(self.cadastrar)
        self.button.setStyleSheet("QPushButton{background-color:deepskyblue;color:white;font-size:12pt;font-weight:bold}")
        self.layout_v.addWidget(self.button)

        # Definir o layout da janela
        self.setLayout(self.layout_v)

    def cadastrar(self):
        # Vamos criar uma variável que fará referência ao arquivo de texto
        arquivo = open("patrimonio.txt", "a", encoding="utf-8")
        arquivo.write(f"ID: {self.edit_id.text()}\n")
        arquivo.write(f"Número de Série: {self.edit_num_serie.text()}\n")
        arquivo.write(f"Nome do Patrimônio: {self.edit_nome.text()}\n")
        arquivo.write(f"Tipo: {self.edit_tipo.text()}\n")
        arquivo.write(f"Descrição: {self.edit_descricao.text()}\n")
        arquivo.write(f"Localização: {self.edit_localizacao.text()}\n")
        arquivo.write(f"Data de Fabricação: {self.edit_data_fabricacao.text()}\n")
        arquivo.write(f"Data de Aquisição: {self.edit_data_aquisicao.text()}\n")
        arquivo.write("------------------------------------------\n")
        arquivo.close()

app = QApplication(sys.argv)
# Instância da classe Cadastro Patrimônio
# para iniciar a janela
tela = CadastroPatrimonio()
# Exibir a tela durante a execução
tela.show()
# Ao clicar no botão, fechar a tela
# deve fechar e sair da memória
app.exec()
