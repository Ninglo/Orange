import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import gui
from functools import partial
from data_analysis import draw_figure
from func import strtofloat
from calculate import final_calc, formula_format
from save_excel import save_data

def create_list(ui):
    column = int(ui.column.text())
    row = int(ui.row.text())
    ui.tableWidget.setColumnCount(column)
    ui.tableWidget.setRowCount(row)

def change_name(ui):
    name = ui.a_name.text()
    line = int(ui.a_line.text())
    _translate = QtCore.QCoreApplication.translate
    ui.tableWidget.verticalHeaderItem(line-1).setText(_translate("MainWindow", name))

def fuc(x, relation_function):
    relation_function = formula_format(relation_function.replace('x', str(x)))
    y, _ = final_calc(relation_function)
    return y[0]

def analysis_and_show(ui):
    num = int(ui.column.text())
    x_row = int(ui.x_row.text()) - 1
    y_row = int(ui.y_row.text()) - 1
    relation_function = ui.relation_function.text()
    for i in range(0, num):
        x_ = strtofloat(ui.tableWidget.item(x_row, i).text())
        y_ = str(fuc(x_, relation_function))
        content = QtWidgets.QTableWidgetItem(y_)
        ui.tableWidget.setItem(y_row, i, content)

def get_figure(ui):
    dic = {}
    x = int(ui.x_index.text()) - 1
    y = int(ui.y_index.text()) - 1
    num = int(ui.column.text())
    exam_num = ui.exam_num.text()
    x_name = ui.x_name.text()
    y_name = ui.y_name.text()
    for i in range(0, num):
        x_ = strtofloat(ui.tableWidget.item(x, i).text())
        y_ = strtofloat(ui.tableWidget.item(y, i).text())
        dic[x_] = y_
    draw_figure(x_name, y_name, dic, exam_num)

def save(ui):
    column = int(ui.column.text())
    row = int(ui.row.text())
    data = ui.data.text()
    matrix = []
    for x in range(0, column):
        lis = []
        for y in range(0, row):
            try:
                item = ui.tableWidget.item(x, y).text()
                lis.append(item)
            except AttributeError:
                lis.append(None)
                continue
        matrix.append(lis)
    save_data(matrix, data)

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.add_btn.clicked.connect(partial(create_list, ui))
    ui.exc_btn.clicked.connect(partial(change_name, ui))
    ui.rela_btn.clicked.connect(partial(analysis_and_show, ui))
    ui.anly_btn.clicked.connect(partial(get_figure, ui))
    ui.save_btn.clicked.connect(partial(save, ui))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()