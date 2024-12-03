# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_select_user.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QAbstractItemView, QDialogButtonBox, QGridLayout, QGroupBox, QLabel, QLineEdit,
                               QTreeWidget)


class Ui_SelectUser(object):
    def setupUi(self, SelectUser):
        if not SelectUser.objectName():
            SelectUser.setObjectName(u"SelectUser")
        SelectUser.resize(448, 619)
        self.gridLayout = QGridLayout(SelectUser)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(SelectUser)
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

        self.buttonBox = QDialogButtonBox(SelectUser)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(SelectUser)
        self.buttonBox.accepted.connect(SelectUser.accept)
        self.buttonBox.rejected.connect(SelectUser.reject)

        QMetaObject.connectSlotsByName(SelectUser)

    # setupUi

    def retranslateUi(self, SelectUser):
        SelectUser.setWindowTitle(QCoreApplication.translate("SelectUser",
                                                             u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439",
                                                             None))
        self.groupBox.setTitle("")
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("SelectUser",
                                                                 u"\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u043e\u0435 \u0438\u043c\u044f",
                                                                 None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("SelectUser",
                                                                 u"\u041f\u043e\u043b\u043d\u043e\u0435 \u0438\u043c\u044f",
                                                                 None));
        self.label.setText(QCoreApplication.translate("SelectUser",
                                                      u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439:",
                                                      None))
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("SelectUser", u"\u041f\u043e\u0438\u0441\u043a", None))
    # retranslateUi
