import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Jogo da Velha")
        self.setFixedSize(300, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)

        # Cria uma grade 3x3 de botões
        self.buttons = []
        for row in range(3):
            row_buttons = []
            for col in range(3):
                btn = QPushButton("")
                btn.setFixedSize(80, 80)
                grid_layout.addWidget(btn, row, col)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())