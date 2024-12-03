# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_exception.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QGroupBox, QLabel, QSizePolicy,
    QTextBrowser, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(741, 548)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.buttonBox = QDialogButtonBox(self.groupBox)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.gridLayout_2.addWidget(self.buttonBox, 4, 0, 1, 1)

        self.tb_traceback_text = QTextBrowser(self.groupBox)
        self.tb_traceback_text.setObjectName(u"tb_traceback_text")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_traceback_text.sizePolicy().hasHeightForWidth())
        self.tb_traceback_text.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.tb_traceback_text, 3, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.te_user_report = QTextEdit(self.groupBox)
        self.te_user_report.setObjectName(u"te_user_report")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.te_user_report.sizePolicy().hasHeightForWidth())
        self.te_user_report.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.te_user_report, 1, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043f\u0440\u0430\u0432\u043a\u0430 \u043e\u0442\u0447\u0435\u0442\u0430 \u043e\u0431 \u043e\u0448\u0438\u0431\u043a\u0435", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u0420\u0435\u043f\u043e\u0440\u0442", None))
        self.tb_traceback_text.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"                                        <html><head><meta name=\"qrichtext\" content=\"1\"\n"
"                                        /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"                                        p, li { white-space: pre-wrap; }\n"
"                                        hr { height: 1px; border-width: 0; }\n"
"                                        li.unchecked::marker { content: \"\\2610\"; }\n"
"                                        li.checked::marker { content: \"\\2612\"; }\n"
"                                        </style></head><body style=\" font-family:'Segoe UI';\n"
"                                        font-size:9pt; font-weight:400; font-style:normal;\">\n"
"                                        <p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;\n"
"                                        margin-right:0px; -qt-block-indent:0; text-indent"
                        ":0px;\">TRACEBACK TEXT</p></body></html>\n"
"                                    ", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u043e\u0434\u0440\u043e\u0431\u043d\u043e \u0447\u0442\u043e \u043f\u0440\u043e\u0438\u0437\u043e\u0448\u043b\u043e \u043f\u0435\u0440\u0435\u0434 \u043e\u0448\u0438\u0431\u043a\u043e\u0439:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Traceback", None))
    # retranslateUi

