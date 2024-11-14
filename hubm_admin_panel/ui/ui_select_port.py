# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_select_port.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QSizePolicy, QTreeWidget,
    QTreeWidgetItem, QWidget)

class Ui_SelectPort(object):
    def setupUi(self, SelectPort):
        if not SelectPort.objectName():
            SelectPort.setObjectName(u"SelectPort")
        SelectPort.resize(448, 619)
        self.gridLayout = QGridLayout(SelectPort)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(SelectPort)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.treeWidget = QTreeWidget(self.groupBox)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.treeWidget.setSortingEnabled(True)

        self.gridLayout_2.addWidget(self.treeWidget, 2, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(SelectPort)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(SelectPort)
        self.buttonBox.accepted.connect(SelectPort.accept)
        self.buttonBox.rejected.connect(SelectPort.reject)

        QMetaObject.connectSlotsByName(SelectPort)
    # setupUi

    def retranslateUi(self, SelectPort):
        SelectPort.setWindowTitle(QCoreApplication.translate("SelectPort", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c USB-\u043f\u043e\u0440\u0442", None))
        self.groupBox.setTitle("")
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("SelectPort", u"VID", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("SelectPort", u"\u0418\u043c\u044f", None));
        self.label.setText(QCoreApplication.translate("SelectPort", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0432\u043e\u0431\u043e\u0434\u043d\u044b\u0435 USB-\u043f\u043e\u0440\u0442\u044b:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("SelectPort", u"\u041f\u043e\u0438\u0441\u043a", None))
    # retranslateUi

