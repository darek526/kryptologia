#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget  # podstawowe klasy interfejsu graficznego
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton
from PyQt5.QtWidgets import QMessageBox

import prog_szyfr

L1, P1 = 0, 0


# clasa definiująca wygląd okna
class Siec_Feistela(QWidget):
    # zwrócenie klasy rodzica i wywoałnie jego kostruktora
    def __init__(self, parent=None):
        super().__init__(parent)

        # 1-liniowe pola edycyjne
        self.tekst_jawny2Edt = QLineEdit()
        self.klucz2Edt = QLineEdit()
        self.szyfrogram2Edt = QLineEdit()
        self.szyfrogramEdt = QLineEdit()
        self.kluczEdt = QLineEdit()
        self.tekst_jawnyEdt = QLineEdit()
        self.interfejs()

    # definicja metody odpowiedzialnej za wygląd interfejsu okna
    def interfejs(self):
        tekst = "Aplikacja do szyfrowania 16-bit wartości binarnych metodą Feistel'a"
        # etykiety
        tekst_wiad = QLabel(tekst, self)
        etykieta1 = QLabel("Wartość Jawana:", self)
        etykieta2 = QLabel("Wartość klucza:", self)
        etykieta3 = QLabel("Szyfrogram:", self)
        etykieta4 = QLabel("Szyfrogram:", self)
        etykieta5 = QLabel("Wartość klucza:", self)
        etykieta6 = QLabel("Wartość Jawna:", self)

        # przypisanie widgetów do układu tabelarycznego
        uklad_t = QGridLayout()
        uklad_t.addWidget(tekst_wiad, 0, 1)
        uklad_t.addWidget(etykieta1, 1, 0)
        uklad_t.addWidget(etykieta2, 2, 0)
        uklad_t.addWidget(etykieta3, 3, 0)
        uklad_t.addWidget(etykieta4, 5, 0)
        uklad_t.addWidget(etykieta5, 6, 0)
        uklad_t.addWidget(etykieta6, 7, 0)

        # pola wynikowe zablokowane do edycji, wyświetlanie podpowiedzi
        self.szyfrogramEdt.readonly = True
        self.tekst_jawny2Edt.readonly = True
        self.tekst_jawnyEdt.setToolTip('Wprowadź <b>binarą Wartość<b>')
        self.kluczEdt.setToolTip('Wprowadź <b>binarną wartośc Klucza</b>')

        uklad_t.addWidget(self.tekst_jawnyEdt, 1, 1)
        uklad_t.addWidget(self.kluczEdt, 2, 1)
        uklad_t.addWidget(self.szyfrogramEdt, 3, 1)
        uklad_t.addWidget(self.szyfrogram2Edt, 5, 1)
        uklad_t.addWidget(self.klucz2Edt, 6, 1)
        uklad_t.addWidget(self.tekst_jawny2Edt, 7, 1)

        # przyciski
        kod_btn = QPushButton("&Szyfrowanie", self)
        dekod_btn = QPushButton("&Deszyfrowanie", self)
        koniec_btn = QPushButton("&Koniec", self)
        koniec_btn.resize(koniec_btn.sizeHint())

        uklad_t.addWidget(kod_btn, 4, 1)
        uklad_t.addWidget(dekod_btn, 8, 1)
        uklad_t.addWidget(koniec_btn, 9, 1)

        # przypisanie utworzonego układu do okna
        self.setLayout(uklad_t)

        koniec_btn.clicked.connect(self.koniec)
        kod_btn.clicked.connect(self.dzialanie)
        dekod_btn.clicked.connect(self.dzialanie)

        self.tekst_jawnyEdt.setFocus()
        self.setGeometry(20, 20, 400, 200)
        self.setWindowIcon(QIcon('szyfr.png'))
        self.setWindowTitle("Sieć Feistel'a")
        self.show()

    def koniec(self):
        self.close()

    def closeEvent(self, event):

        odp = QMessageBox.question(
            self, 'Komunikat',
            "Czy na pewno koniec?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def dzialanie(self):
        nadawca = self.sender()

        try:
            tekst_jawny = (self.tekst_jawnyEdt.text())
            klucz = (self.kluczEdt.text())
            szyfrogram = ""
            szyfrogram2 = (self.szyfrogram2Edt.text())
            klucz2 = (self.klucz2Edt.text())
            tekst_jawny2 = ""

            if nadawca.text() == "&Szyfrowanie":
                try:
                    if len(tekst_jawny) == 16 and int(tekst_jawny, 2) <= (2 ** 16):
                        if len(klucz) == 8 and int(klucz, 2) <= (2 ** 8):
                            szyfrogram = prog_szyfr.szyfrowanie(tekst_jawny, klucz, szyfrogram)
                        else:
                            QMessageBox.warning(self, "Błąd", "Błędny Klucz", QMessageBox.Ok)
                            return
                    else:
                        QMessageBox.warning(self, "Błąd", "Błędna Wartość Jawana", QMessageBox.Ok)
                        return
                except ValueError:
                    QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)
                self.szyfrogramEdt.setText(str(szyfrogram))

            elif nadawca.text() == "&Deszyfrowanie":
                try:
                    if len(szyfrogram2) == 16 and int(szyfrogram2, 2) <= (2 ** 16):
                        if len(klucz2) == 8 and int(klucz2, 2) <= (2 ** 8):
                            tekst_jawny2 = prog_szyfr.deszyfrowanie(szyfrogram2, klucz2, tekst_jawny2)
                        else:
                            QMessageBox.warning(self, "Błąd", "Błędny Klucz", QMessageBox.Ok)
                            return
                    else:
                        QMessageBox.warning(self, "Błąd", "Błędna wartość Szyfrogramu", QMessageBox.Ok)
                        return
                except ValueError:
                    QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)
                self.tekst_jawny2Edt.setText(str(tekst_jawny2))
            else:
                QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)
                return
        except ValueError:
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)


if __name__ == '__main__':
    import sys

    # Obeikt reprezentujacy aplikację oraz okno aplikacji
    app = QApplication(sys.argv)
    okno = Siec_Feistela()
    # uruchomienie petli do obsługi zdarzeń
    sys.exit(app.exec_())
