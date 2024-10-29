# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_new_user.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_win_new_user(object):
    def setupUi(self, win_new_user):
        if not win_new_user.objectName():
            win_new_user.setObjectName(u"win_new_user")
        win_new_user.resize(436, 430)
        self.gridLayout = QGridLayout(win_new_user)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_6 = QGroupBox(win_new_user)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_2 = QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox_6)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_42 = QGroupBox(self.groupBox_6)
        self.groupBox_42.setObjectName(u"groupBox_42")
        self.horizontalLayout_55 = QHBoxLayout(self.groupBox_42)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_55 = QLabel(self.groupBox_42)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_55.addWidget(self.label_55)

        self.le_fullname = QLineEdit(self.groupBox_42)
        self.le_fullname.setObjectName(u"le_fullname")

        self.horizontalLayout_55.addWidget(self.le_fullname)


        self.verticalLayout.addWidget(self.groupBox_42)

        self.groupBox_44 = QGroupBox(self.groupBox_6)
        self.groupBox_44.setObjectName(u"groupBox_44")
        self.horizontalLayout_57 = QHBoxLayout(self.groupBox_44)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_57 = QLabel(self.groupBox_44)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_57.addWidget(self.label_57)

        self.le_name = QLineEdit(self.groupBox_44)
        self.le_name.setObjectName(u"le_name")

        self.horizontalLayout_57.addWidget(self.le_name)


        self.verticalLayout.addWidget(self.groupBox_44)

        self.groupBox_2 = QGroupBox(self.groupBox_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFlat(False)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_ip = QLineEdit(self.groupBox_2)
        self.le_ip.setObjectName(u"le_ip")
        self.le_ip.setLayoutDirection(Qt.LeftToRight)
        self.le_ip.setDragEnabled(False)
        self.le_ip.setReadOnly(False)

        self.horizontalLayout_2.addWidget(self.le_ip)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_43 = QGroupBox(self.groupBox_6)
        self.groupBox_43.setObjectName(u"groupBox_43")
        self.horizontalLayout_56 = QHBoxLayout(self.groupBox_43)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_56 = QLabel(self.groupBox_43)
        self.label_56.setObjectName(u"label_56")
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        self.label_56.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_56.addWidget(self.label_56)

        self.le_pass = QLineEdit(self.groupBox_43)
        self.le_pass.setObjectName(u"le_pass")
        self.le_pass.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.horizontalLayout_56.addWidget(self.le_pass)


        self.verticalLayout.addWidget(self.groupBox_43)

        self.groupBox_45 = QGroupBox(self.groupBox_6)
        self.groupBox_45.setObjectName(u"groupBox_45")
        self.horizontalLayout_59 = QHBoxLayout(self.groupBox_45)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_59 = QLabel(self.groupBox_45)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_59.addWidget(self.label_59)

        self.le_email = QLineEdit(self.groupBox_45)
        self.le_email.setObjectName(u"le_email")

        self.horizontalLayout_59.addWidget(self.le_email)


        self.verticalLayout.addWidget(self.groupBox_45)

        self.groupBox_46 = QGroupBox(self.groupBox_6)
        self.groupBox_46.setObjectName(u"groupBox_46")
        self.horizontalLayout_60 = QHBoxLayout(self.groupBox_46)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_60 = QLabel(self.groupBox_46)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_60.addWidget(self.label_60)

        self.le_comment = QLineEdit(self.groupBox_46)
        self.le_comment.setObjectName(u"le_comment")

        self.horizontalLayout_60.addWidget(self.le_comment)


        self.verticalLayout.addWidget(self.groupBox_46)

        self.groupBox_47 = QGroupBox(self.groupBox_6)
        self.groupBox_47.setObjectName(u"groupBox_47")
        self.horizontalLayout_61 = QHBoxLayout(self.groupBox_47)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_61 = QLabel(self.groupBox_47)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_61.addWidget(self.label_61)

        self.cb_active = QCheckBox(self.groupBox_47)
        self.cb_active.setObjectName(u"cb_active")
        self.cb_active.setLayoutDirection(Qt.RightToLeft)
        self.cb_active.setChecked(True)

        self.horizontalLayout_61.addWidget(self.cb_active)


        self.verticalLayout.addWidget(self.groupBox_47)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 2)

        self.btns = QDialogButtonBox(self.groupBox_6)
        self.btns.setObjectName(u"btns")
        self.btns.setOrientation(Qt.Horizontal)
        self.btns.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.gridLayout_2.addWidget(self.btns, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_6, 0, 0, 1, 1)


        self.retranslateUi(win_new_user)
        self.btns.accepted.connect(win_new_user.accept)
        self.btns.rejected.connect(win_new_user.reject)

        QMetaObject.connectSlotsByName(win_new_user)
    # setupUi

    def retranslateUi(self, win_new_user):
        win_new_user.setWindowTitle(QCoreApplication.translate("win_new_user", u"\u041d\u043e\u0432\u044b\u0439 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.groupBox_6.setTitle("")
        self.label.setText(QCoreApplication.translate("win_new_user", u"* - \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.label_55.setText(QCoreApplication.translate("win_new_user", u"\u041f\u043e\u043b\u043d\u043e\u0435 \u0438\u043c\u044f*", None))
#if QT_CONFIG(tooltip)
        self.le_fullname.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.le_fullname.setText("")
        self.le_fullname.setPlaceholderText(QCoreApplication.translate("win_new_user", u"\u0418\u0432\u0430\u043d\u043e\u0432 \u0418\u0432\u0430\u043d \u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447", None))
        self.label_57.setText(QCoreApplication.translate("win_new_user", u"\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u043e\u0435 \u0438\u043c\u044f*", None))
#if QT_CONFIG(tooltip)
        self.le_name.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.le_name.setText("")
        self.le_name.setPlaceholderText(QCoreApplication.translate("win_new_user", u"ii.ivanov", None))
        self.label_2.setText(QCoreApplication.translate("win_new_user", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 IP*", None))
        self.le_ip.setText("")
        self.le_ip.setPlaceholderText(QCoreApplication.translate("win_new_user", u"255.255.255.255", None))
        self.label_56.setText(QCoreApplication.translate("win_new_user", u"\u041f\u0430\u0440\u043e\u043b\u044c*", None))
        self.le_pass.setText("")
        self.le_pass.setPlaceholderText(QCoreApplication.translate("win_new_user", u"MyTopP@ssw0rd", None))
        self.label_59.setText(QCoreApplication.translate("win_new_user", u"Email", None))
#if QT_CONFIG(tooltip)
        self.le_email.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.le_email.setText("")
        self.le_email.setPlaceholderText(QCoreApplication.translate("win_new_user", u"ii.ivanov@unistroyrf.ru", None))
        self.label_60.setText(QCoreApplication.translate("win_new_user", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
#if QT_CONFIG(tooltip)
        self.le_comment.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.le_comment.setText("")
        self.le_comment.setPlaceholderText(QCoreApplication.translate("win_new_user", u"\u042d\u043d\u0435\u0440\u0433\u043e\u0440\u0435\u0441\u0443\u0440\u0441, \u044e\u0440\u0438\u0441\u0442", None))
        self.label_61.setText(QCoreApplication.translate("win_new_user", u"\u0421\u0442\u0430\u0442\u0443\u0441*", None))
        self.cb_active.setText(QCoreApplication.translate("win_new_user", u"\u0410\u043a\u0442\u0438\u0432\u0435\u043d", None))
    # retranslateUi

