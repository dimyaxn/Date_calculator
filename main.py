
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLineEdit
from PySide6.QtGui import QFontDatabase
from design import Ui_MainWindow
from date_calc import days_calc, result_date_calc

class DateCalc(QMainWindow):
    def __init__(self):
        super(DateCalc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("fonts/Jost.ttf") #Позволяет использовать шрифт, если он не установлен в системе

        '''buttons'''
        self.ui.add_pushButton.clicked.connect(self.add_stop_date)
        self.ui.del_pushButton.clicked.connect(self.del_stop_date)
        self.ui.del_all_pushButton.clicked.connect(self.del_all)
        self.ui.result_pushButton.clicked.connect(self.result_date)



    def add_stop_date(self):

        rowPosition = self.ui.tableWidget.rowCount()  # считает кол-во строк в таблице
        self.ui.tableWidget.insertRow(rowPosition)  # добавляет новую строку к последней

        reason = self.ui.reason_lineEdit.text() # задаем объект причина и считываем в него значения из reason_lineEdit
        self.ui.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(reason))  # размещаем объект в qTableWidget

        start_date = self.ui.start_dateEdit.text()          # задаем начальную дату и считываем ее с start_dateEdit
        self.ui.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(start_date))  # размещаем объект qTableWidget

        end_date = self.ui.end_dateEdit.text()              # задаем начальную дату и считываем ее с start_dateEdit
        self.ui.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(end_date))  # размещаем объект в qTableWidget

        delta_date = days_calc(start_date, end_date)
        self.ui.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(delta_date))  # размещаем объект в qTableWidget

        self.ui.tableWidget.resizeColumnsToContents()       # выравниваем ширину столбцов по контексту



    def del_stop_date(self):
        row = self.ui.tableWidget.currentRow()
        if row > -1:                                        # Если есть выделенная строка/элемент
            self.ui.tableWidget.removeRow(row)
            # Следующий вызов нужен для того, чтобы
            # сбросить индекс выбранной строки (чтобы currentRow установился в -1)
            self.ui.tableWidget.selectionModel().clearCurrentIndex()

    def del_all(self):
        self.ui.tableWidget.setRowCount(0)                  # устанавливаем кол-во строк в таблице = 0

    def result_date(self):
        rowPosition = self.ui.tableWidget.rowCount()        # считает кол-во строк в таблице
        first_date = self.ui.First_dateEdit.text()          # считывает дату с First_dateEdit
        max_days = int(self.ui.max_days_spinBox.text())     # считываает max кол-во дней с max_days_label
        days_in_tableWidget = []
        for i in range(rowPosition):
            day = int(self.ui.tableWidget.item(i, 3).text())
            days_in_tableWidget.append(day)

        res = result_date_calc(first_date, max_days, sum(days_in_tableWidget))
                                                #получаем с помощью функции result_date_calc конечный результат
        self.ui.result_label.setText(res)                   #отображаем в result_label


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DateCalc()
    window.show()
    sys.exit(app.exec())
