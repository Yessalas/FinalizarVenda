from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,QMessageBox, QComboBox
import sys 

class CaixaMercado(QWidget):
    def __init__(self):
        super().__init__()

        # Vamos configurar a geometria da tela. Setandos valores de posição X e Y,
        # além de largura e altura
        self.setGeometry(500,100,700,800)

        # Texto para a barra de título
        self.setWindowTitle("Caixa")

        #Layout vertical da tela inteira
        self.layout_v_total = QVBoxLayout()

        #Label titulo
        self.label_titulo = QLabel("Finalizar Venda")
        self.label_titulo.setStyleSheet("QLabel{background-color:White ; font-size:13pt}")
        self.label_titulo.setFixedSize(700,50)
        # adicionar a label de titulo ao layout
        self.layout_v_total.addWidget(self.label_titulo)







        #Label dados
        self.label_dados = QLabel()

        # Criar e adicionar um layout horizontal para 
        # os dados da compra
        self.layout_h_dados = QHBoxLayout()

        #================================================================================
        # criar label da esquerda ######################################
        self.label_esquerda = QLabel()
        # Criar um layout vertical
        self.layout_v_esquerda = QVBoxLayout()
        # label para guardar o texto Total de venda
        # e a caixa total de venda, ou seja, irá
        # a guardar uma nova label e uma lineEdit
       
    #    ===================Total Venda==============================
       
        self.label_total_venda = QLabel()

        # Criar o layout horizontal para a label total_venda e a 
        # Line Edit
        self.layout_h_total_venda = QHBoxLayout()

        # Criar a label que terá o texto Total de vendas
        self.label_venda = QLabel("Total de Venda")
        # Criar a LineEdit que recebe o total de venda
        self.edit_venda = QLineEdit("R$ 0,00")
        # adicionar a label_venda e a edit_venda ao layout horizontal venda
        self.layout_h_total_venda.addWidget(self.label_venda)
        self.layout_h_total_venda.addWidget(self.edit_venda)

        # Adiconar o layout_h_total_venda a label _total_venda
        self.label_total_venda.setLayout(self.layout_h_total_venda)

        # adicionar a label_total_venda ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_total_venda)

# ================== Fim do total venda ======================================


# =================== Inicio do Desconto ====================================

        self.label_desconto = QLabel()

        # Criar o layout horizontal para a label desconto e a 
        # Line Edit
        self.layout_h_desconto = QHBoxLayout()

        # Criar a label que terá o texto Desconto
        self.label_desc = QLabel("Desconto")
        # Criar a LineEdit que recebe o total de desc
        self.edit_desc = QLineEdit("R$ 0,00")
        # adicionar a label_desc e a edit_desc ao layout horizontal desc
        self.layout_h_desconto.addWidget(self.label_desc)
        self.layout_h_desconto.addWidget(self.edit_desc)

        # Adiconar o layout_h_desconto a label _desconto
        self.label_desconto.setLayout(self.layout_h_desconto)

        # adicionar a label_desconto ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_desconto)

# =================== Fim do Desconto =========================================

# =================================== Acréscimo ===========================

        # Adicionar o layout vertical da esquerda
        # na coluna da esquerda
        self.label_esquerda.setLayout(self.layout_v_esquerda)

        self.label_esquerda.setStyleSheet("QLabel{background-color:blue}")
        self.label_esquerda.setFixedSize(200,320)
        # adicionar a label da esquerda no layout 
        # horizontal
        self.layout_h_dados.addWidget(self.label_esquerda)
        #=============================================================

 #    ===================Acréscimo==============================
       
        self.label_acrescimo = QLabel()

        # Criar o layout horizontal para a label total_venda e a 
        # Line Edit
        self.layout_h_acrescimo = QHBoxLayout()

        # Criar a label que terá o texto Total de vendas
        self.label_acre = QLabel("Total de Acréscimo")
        # Criar a LineEdit que recebe o total de venda
        self.edit_acre = QLineEdit("R$ 0,00")
        # adicionar a label_venda e a edit_venda ao layout horizontal venda
        self.layout_h_acrescimo.addWidget(self.label_acre)
        self.layout_h_acrescimo.addWidget(self.edit_acre)

        # Adiconar o layout_h_total_venda a label _total_venda
        self.label_acrescimo.setLayout(self.layout_h_acrescimo)

        # adicionar a label_total_venda ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_acrescimo)

# ================== Fim do Acréscimo ======================================

 #    ===================Inicio Total Líquido==============================
       
        self.label_total_liquido = QLabel()

        # Criar o layout horizontal para a label total_venda e a 
        # Line Edit
        self.layout_h_total_liquido = QHBoxLayout()

        # Criar a label que terá o texto Total de vendas
        self.label_total_liqui = QLabel("Total de Líquido")
        # Criar a LineEdit que recebe o total de venda
        self.edit_total_liqui = QLineEdit("R$ 0,00")
        # adicionar a label_venda e a edit_venda ao layout horizontal venda
        self.layout_h_total_liquido.addWidget(self.label_total_liqui)
        self.layout_h_total_liquido.addWidget(self.edit_total_liqui)

        # Adiconar o layout_h_total_venda a label _total_venda
        self.label_total_liquido.setLayout(self.layout_h_total_liquido)

        # adicionar a label_total_venda ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_total_liquido)

# ================== Fim do Total Líquido ======================================

 #    ===================Total de Troco==============================
       
        self.label_troco= QLabel()

        # Criar o layout horizontal para a label total_venda e a 
        # Line Edit
        self.layout_h_troco = QHBoxLayout()

        # Criar a label que terá o texto Total de vendas
        self.label_troc= QLabel("Total do Troco")
        # Criar a LineEdit que recebe o total de venda
        self.edit_troc = QLineEdit("R$ 0,00")
        # adicionar a label_venda e a edit_venda ao layout horizontal venda
        self.layout_h_troco.addWidget(self.label_troc)
        self.layout_h_troco.addWidget(self.edit_troc)

        # Adiconar o layout_h_total_venda a label _total_venda
        self.label_troco.setLayout(self.layout_h_troco)

        # adicionar a label_total_venda ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_troco)

# ================== Fim do Troco ======================================

        # criar label da direita
        self.label_direita = QLabel()
        self.layout_v_direita = QVBoxLayout()
        self.label_direita.setStyleSheet("QLabel{background-color:yellow}")

        # =================== CLIENTE ==============================
        self.label_cliente = QLabel()

        self.layout_h_cliente = QVBoxLayout()

        self.label_clien = QLabel("Cliente")
        self.edit_clien = QLineEdit("1 - consumidor")

        self.layout_v_direita.addWidget(self.label_clien)
        self.layout_v_direita.addWidget(self.edit_clien)

        self.label_cliente.setLayout(self.layout_h_cliente)

        self.layout_v_direita.addWidget(self.label_cliente)






        
        # adicionar a label da direita no layout
         
        # horizontal
        self.layout_h_dados.addWidget(self.label_direita)
        


        self.label_dados.setLayout(self.layout_h_dados)
        self.label_dados.setStyleSheet("QLabel{background-color:red}")
        self.layout_v_total.addWidget(self.label_dados)
        
        









        #Label rodape
        self.label_rodape = QLabel()
        self.label_rodape.setStyleSheet("QLabel{background-color:green}")
        self.layout_v_total.addWidget(self.label_rodape)

        # adicionar o layout vertical a tela
        self.setLayout(self.layout_v_total)

app = QApplication(sys.argv)
tela = CaixaMercado()
tela.show()
app.exec()