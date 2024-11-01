# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStackedWidget,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1175, 775)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/res/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        MainWindow.setIconSize(QSize(24, 24))
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.btn_check_update = QAction(MainWindow)
        self.btn_check_update.setObjectName(u"btn_check_update")
        self.btn_check_update.setEnabled(True)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SyncSynchronizing))
        self.btn_check_update.setIcon(icon1)
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.btn_check_user_access_group = QAction(MainWindow)
        self.btn_check_user_access_group.setObjectName(u"btn_check_user_access_group")
        self.btn_check_user_access_port = QAction(MainWindow)
        self.btn_check_user_access_port.setObjectName(u"btn_check_user_access_port")
        self.btn_about_program = QAction(MainWindow)
        self.btn_about_program.setObjectName(u"btn_about_program")
        self.btn_about_program.setEnabled(True)
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.btn_about_program.setIcon(icon2)
        self.btn_reboot_server = QAction(MainWindow)
        self.btn_reboot_server.setObjectName(u"btn_reboot_server")
        self.btn_reboot_server.setEnabled(False)
        self.btn_backup_new = QAction(MainWindow)
        self.btn_backup_new.setObjectName(u"btn_backup_new")
        self.btn_backup_restore = QAction(MainWindow)
        self.btn_backup_restore.setObjectName(u"btn_backup_restore")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_11 = QGridLayout(self.centralwidget)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tabs_general = QTabWidget(self.centralwidget)
        self.tabs_general.setObjectName(u"tabs_general")
        self.tabs_general.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabs_general.sizePolicy().hasHeightForWidth())
        self.tabs_general.setSizePolicy(sizePolicy1)
        self.tabs_general.setTabPosition(QTabWidget.TabPosition.North)
        self.tabs_general.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabs_general.setDocumentMode(False)
        self.tabs_general.setTabsClosable(False)
        self.tabs_general.setMovable(True)
        self.tabs_general.setTabBarAutoHide(True)
        self.tab_dashboard = QWidget()
        self.tab_dashboard.setObjectName(u"tab_dashboard")
        self.tab_dashboard.setAcceptDrops(True)
        self.gridLayout_20 = QGridLayout(self.tab_dashboard)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.widget = QWidget(self.tab_dashboard)
        self.widget.setObjectName(u"widget")
        self.widget.setAcceptDrops(True)
        self.gridLayout_18 = QGridLayout(self.widget)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.groupBox_15 = QGroupBox(self.widget)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setAcceptDrops(True)
        self.gridLayout_26 = QGridLayout(self.groupBox_15)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.DevButton2 = QPushButton(self.groupBox_15)
        self.DevButton2.setObjectName(u"DevButton2")

        self.gridLayout_26.addWidget(self.DevButton2, 1, 1, 1, 1)

        self.DevButton1 = QPushButton(self.groupBox_15)
        self.DevButton1.setObjectName(u"DevButton1")

        self.gridLayout_26.addWidget(self.DevButton1, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.groupBox_15)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_3)
        self.gridLayout_27.setObjectName(u"gridLayout_27")

        self.gridLayout_26.addWidget(self.frame_3, 0, 0, 1, 2)


        self.gridLayout_18.addWidget(self.groupBox_15, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.widget, 0, 1, 1, 1)

        self.widget_2 = QWidget(self.tab_dashboard)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setAcceptDrops(True)
        self.gridLayout_22 = QGridLayout(self.widget_2)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.groupBox_14 = QGroupBox(self.widget_2)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setAcceptDrops(True)
        self.gridLayout_28 = QGridLayout(self.groupBox_14)
        self.gridLayout_28.setObjectName(u"gridLayout_28")

        self.gridLayout_22.addWidget(self.groupBox_14, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.widget_2, 0, 0, 1, 1)


        self.gridLayout_20.addLayout(self.gridLayout_19, 0, 0, 1, 1)

        self.tabs_general.addTab(self.tab_dashboard, "")
        self.tab_users = QWidget()
        self.tab_users.setObjectName(u"tab_users")
        self.gridLayout_6 = QGridLayout(self.tab_users)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabs_users = QTabWidget(self.tab_users)
        self.tabs_users.setObjectName(u"tabs_users")
        sizePolicy1.setHeightForWidth(self.tabs_users.sizePolicy().hasHeightForWidth())
        self.tabs_users.setSizePolicy(sizePolicy1)
        self.tabs_users.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabs_users.setDocumentMode(False)
        self.tabs_users.setTabsClosable(False)
        self.tabs_users.setMovable(False)
        self.tabs_users.setTabBarAutoHide(False)
        self.users_tab_info = QWidget()
        self.users_tab_info.setObjectName(u"users_tab_info")
        self.gridLayout_4 = QGridLayout(self.users_tab_info)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.groupBox_7 = QGroupBox(self.users_tab_info)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_10 = QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.groupBox_7)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.users_fullname_label = QLabel(self.groupBox)
        self.users_fullname_label.setObjectName(u"users_fullname_label")
        sizePolicy.setHeightForWidth(self.users_fullname_label.sizePolicy().hasHeightForWidth())
        self.users_fullname_label.setSizePolicy(sizePolicy)
        self.users_fullname_label.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.users_fullname_label)

        self.le_user_cn = QLineEdit(self.groupBox)
        self.le_user_cn.setObjectName(u"le_user_cn")
        self.le_user_cn.setInputMethodHints(Qt.InputMethodHint.ImhNone)

        self.horizontalLayout.addWidget(self.le_user_cn)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox1 = QGroupBox(self.groupBox_7)
        self.groupBox1.setObjectName(u"groupBox1")
        self.groupBox1.setFlat(False)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox1)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_user_name = QLineEdit(self.groupBox1)
        self.le_user_name.setObjectName(u"le_user_name")
        self.le_user_name.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.le_user_name.setDragEnabled(False)
        self.le_user_name.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.le_user_name)


        self.verticalLayout.addWidget(self.groupBox1)

        self.groupBox2 = QGroupBox(self.groupBox_7)
        self.groupBox2.setObjectName(u"groupBox2")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(self.groupBox2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.label_11)

        self.le_user_default_ip = QLineEdit(self.groupBox2)
        self.le_user_default_ip.setObjectName(u"le_user_default_ip")
        self.le_user_default_ip.setFrame(True)
        self.le_user_default_ip.setDragEnabled(False)

        self.horizontalLayout_4.addWidget(self.le_user_default_ip)


        self.verticalLayout.addWidget(self.groupBox2)

        self.groupBox_43 = QGroupBox(self.groupBox_7)
        self.groupBox_43.setObjectName(u"groupBox_43")
        self.horizontalLayout_56 = QHBoxLayout(self.groupBox_43)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_56 = QLabel(self.groupBox_43)
        self.label_56.setObjectName(u"label_56")
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        self.label_56.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_56.addWidget(self.label_56)

        self.le_user_pass = QLineEdit(self.groupBox_43)
        self.le_user_pass.setObjectName(u"le_user_pass")
        self.le_user_pass.setInputMethodHints(Qt.InputMethodHint.ImhNoAutoUppercase|Qt.InputMethodHint.ImhNoPredictiveText|Qt.InputMethodHint.ImhSensitiveData)
        self.le_user_pass.setFrame(True)
        self.le_user_pass.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.horizontalLayout_56.addWidget(self.le_user_pass)

        self.btn_show_pass = QPushButton(self.groupBox_43)
        self.btn_show_pass.setObjectName(u"btn_show_pass")
        icon3 = QIcon()
        icon3.addFile(u":/res/icons/eye_on.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/res/icons/eye_off.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_show_pass.setIcon(icon3)
        self.btn_show_pass.setCheckable(True)
        self.btn_show_pass.setAutoRepeat(False)
        self.btn_show_pass.setAutoExclusive(False)

        self.horizontalLayout_56.addWidget(self.btn_show_pass)


        self.verticalLayout.addWidget(self.groupBox_43)

        self.groupBox3 = QGroupBox(self.groupBox_7)
        self.groupBox3.setObjectName(u"groupBox3")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_12 = QLabel(self.groupBox3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.label_12)

        self.le_user_email = QLineEdit(self.groupBox3)
        self.le_user_email.setObjectName(u"le_user_email")

        self.horizontalLayout_5.addWidget(self.le_user_email)


        self.verticalLayout.addWidget(self.groupBox3)

        self.groupBox4 = QGroupBox(self.groupBox_7)
        self.groupBox4.setObjectName(u"groupBox4")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.groupBox4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_6.addWidget(self.label_10)

        self.le_user_comment = QLineEdit(self.groupBox4)
        self.le_user_comment.setObjectName(u"le_user_comment")

        self.horizontalLayout_6.addWidget(self.le_user_comment)


        self.verticalLayout.addWidget(self.groupBox4)

        self.groupBox_34 = QGroupBox(self.groupBox_7)
        self.groupBox_34.setObjectName(u"groupBox_34")
        self.horizontalLayout_43 = QHBoxLayout(self.groupBox_34)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_44 = QLabel(self.groupBox_34)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_43.addWidget(self.label_44)

        self.le_user_tg_id = QLineEdit(self.groupBox_34)
        self.le_user_tg_id.setObjectName(u"le_user_tg_id")

        self.horizontalLayout_43.addWidget(self.le_user_tg_id)


        self.verticalLayout.addWidget(self.groupBox_34)

        self.groupBox_42 = QGroupBox(self.groupBox_7)
        self.groupBox_42.setObjectName(u"groupBox_42")
        self.horizontalLayout_55 = QHBoxLayout(self.groupBox_42)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_55 = QLabel(self.groupBox_42)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_55.addWidget(self.label_55)

        self.le_user_tg_code = QLineEdit(self.groupBox_42)
        self.le_user_tg_code.setObjectName(u"le_user_tg_code")
        self.le_user_tg_code.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.horizontalLayout_55.addWidget(self.le_user_tg_code)

        self.btn_show_tg_code = QPushButton(self.groupBox_42)
        self.btn_show_tg_code.setObjectName(u"btn_show_tg_code")
        self.btn_show_tg_code.setIcon(icon3)
        self.btn_show_tg_code.setCheckable(True)

        self.horizontalLayout_55.addWidget(self.btn_show_tg_code)


        self.verticalLayout.addWidget(self.groupBox_42)

        self.groupBox5 = QGroupBox(self.groupBox_7)
        self.groupBox5.setObjectName(u"groupBox5")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox5)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setMaximumSize(QSize(150, 16777215))
        self.label_3.setBaseSize(QSize(0, 0))
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setTextFormat(Qt.TextFormat.AutoText)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.cb_user_active = QCheckBox(self.groupBox5)
        self.cb_user_active.setObjectName(u"cb_user_active")
        sizePolicy.setHeightForWidth(self.cb_user_active.sizePolicy().hasHeightForWidth())
        self.cb_user_active.setSizePolicy(sizePolicy)
        self.cb_user_active.setMinimumSize(QSize(150, 20))
        self.cb_user_active.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(9)
        font.setItalic(False)
        self.cb_user_active.setFont(font)
        self.cb_user_active.setChecked(True)
        self.cb_user_active.setTristate(False)

        self.horizontalLayout_3.addWidget(self.cb_user_active)


        self.verticalLayout.addWidget(self.groupBox5)


        self.gridLayout_10.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.btn_user_save_params = QPushButton(self.groupBox_7)
        self.btn_user_save_params.setObjectName(u"btn_user_save_params")
        self.btn_user_save_params.setFlat(False)

        self.gridLayout_10.addWidget(self.btn_user_save_params, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_7, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.tabs_users.addTab(self.users_tab_info, "")
        self.users_tab_group_policies = QWidget()
        self.users_tab_group_policies.setObjectName(u"users_tab_group_policies")
        self.gridLayout_5 = QGridLayout(self.users_tab_group_policies)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.stack_user_policies = QStackedWidget(self.users_tab_group_policies)
        self.stack_user_policies.setObjectName(u"stack_user_policies")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_29 = QGridLayout(self.page)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.tbl_user_policies = QTableWidget(self.page)
        if (self.tbl_user_policies.columnCount() < 10):
            self.tbl_user_policies.setColumnCount(10)
        font1 = QFont()
        font1.setPointSize(9)
        font1.setKerning(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tbl_user_policies.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_user_policies.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_user_policies.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_user_policies.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_user_policies.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_user_policies.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_user_policies.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbl_user_policies.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbl_user_policies.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbl_user_policies.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        if (self.tbl_user_policies.rowCount() < 3):
            self.tbl_user_policies.setRowCount(3)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbl_user_policies.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbl_user_policies.setVerticalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tbl_user_policies.setVerticalHeaderItem(2, __qtablewidgetitem12)
        font2 = QFont()
        font2.setPointSize(1)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setCheckState(Qt.Checked);
        __qtablewidgetitem13.setFont(font2);
        __qtablewidgetitem13.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled|Qt.ItemIsAutoTristate);
        self.tbl_user_policies.setItem(0, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tbl_user_policies.setItem(0, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tbl_user_policies.setItem(0, 9, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setCheckState(Qt.Unchecked);
        __qtablewidgetitem16.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tbl_user_policies.setItem(1, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tbl_user_policies.setItem(1, 9, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tbl_user_policies.setItem(2, 9, __qtablewidgetitem18)
        self.tbl_user_policies.setObjectName(u"tbl_user_policies")
        self.tbl_user_policies.setEnabled(True)
        self.tbl_user_policies.setLineWidth(100)
        self.tbl_user_policies.setMidLineWidth(50)
        self.tbl_user_policies.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tbl_user_policies.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbl_user_policies.setSortingEnabled(False)
        self.tbl_user_policies.setRowCount(3)
        self.tbl_user_policies.setColumnCount(10)
        self.tbl_user_policies.verticalHeader().setProperty(u"showSortIndicator", False)

        self.gridLayout_29.addWidget(self.tbl_user_policies, 0, 0, 1, 1)

        self.stack_user_policies.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_30 = QGridLayout(self.page_2)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.tree_user_policies = QTreeWidget(self.page_2)
        font3 = QFont()
        font3.setBold(False)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font3);
        self.tree_user_policies.setHeaderItem(__qtreewidgetitem)
        brush = QBrush(QColor(65, 68, 82, 100))
        brush.setStyle(Qt.SolidPattern)
        font4 = QFont()
        font4.setBold(True)
        __qtreewidgetitem1 = QTreeWidgetItem(self.tree_user_policies)
        __qtreewidgetitem1.setCheckState(0, Qt.Checked);
        __qtreewidgetitem1.setFont(0, font4);
        __qtreewidgetitem1.setBackground(0, brush);
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem3 = QTreeWidgetItem(self.tree_user_policies)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        self.tree_user_policies.setObjectName(u"tree_user_policies")

        self.gridLayout_30.addWidget(self.tree_user_policies, 0, 0, 1, 1)

        self.stack_user_policies.addWidget(self.page_2)

        self.gridLayout_5.addWidget(self.stack_user_policies, 0, 0, 1, 1)

        self.groupBox_18 = QGroupBox(self.users_tab_group_policies)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.gridLayout_21 = QGridLayout(self.groupBox_18)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.frame = QFrame(self.groupBox_18)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout_14 = QHBoxLayout(self.frame)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_user_policies_create = QPushButton(self.frame)
        self.btn_user_policies_create.setObjectName(u"btn_user_policies_create")

        self.horizontalLayout_14.addWidget(self.btn_user_policies_create)

        self.btn_user_policies_delete = QPushButton(self.frame)
        self.btn_user_policies_delete.setObjectName(u"btn_user_policies_delete")

        self.horizontalLayout_14.addWidget(self.btn_user_policies_delete)

        self.btn_change_view_user_policies = QPushButton(self.frame)
        self.btn_change_view_user_policies.setObjectName(u"btn_change_view_user_policies")
        self.btn_change_view_user_policies.setMaximumSize(QSize(30, 16777215))
        icon4 = QIcon()
        icon4.addFile(u":/res/icons/strings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_change_view_user_policies.setIcon(icon4)
        self.btn_change_view_user_policies.setCheckable(False)

        self.horizontalLayout_14.addWidget(self.btn_change_view_user_policies)

        self.btn_show_user_policies = QPushButton(self.frame)
        self.btn_show_user_policies.setObjectName(u"btn_show_user_policies")
        self.btn_show_user_policies.setMaximumSize(QSize(30, 16777215))
        self.btn_show_user_policies.setIcon(icon3)
        self.btn_show_user_policies.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.btn_show_user_policies)


        self.gridLayout_21.addWidget(self.frame, 0, 0, 1, 1)

        self.btn_user_policies_save = QPushButton(self.groupBox_18)
        self.btn_user_policies_save.setObjectName(u"btn_user_policies_save")

        self.gridLayout_21.addWidget(self.btn_user_policies_save, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_18, 2, 0, 1, 1)

        self.tabs_users.addTab(self.users_tab_group_policies, "")
        self.users_tab_usb_policices = QWidget()
        self.users_tab_usb_policices.setObjectName(u"users_tab_usb_policices")
        self.users_tab_usb_policices.setEnabled(True)
        self.gridLayout_7 = QGridLayout(self.users_tab_usb_policices)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame1 = QFrame(self.users_tab_usb_policices)
        self.frame1.setObjectName(u"frame1")
        self.gridLayout_9 = QGridLayout(self.frame1)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tbl_user_ports = QTreeWidget(self.frame1)
        __qtreewidgetitem4 = QTreeWidgetItem()
        __qtreewidgetitem4.setText(0, u"1");
        self.tbl_user_ports.setHeaderItem(__qtreewidgetitem4)
        self.tbl_user_ports.setObjectName(u"tbl_user_ports")
        self.tbl_user_ports.setEnabled(True)
        self.tbl_user_ports.setAlternatingRowColors(False)
        self.tbl_user_ports.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tbl_user_ports.setRootIsDecorated(True)
        self.tbl_user_ports.setItemsExpandable(True)
        self.tbl_user_ports.setSortingEnabled(False)
        self.tbl_user_ports.setAnimated(True)
        self.tbl_user_ports.setHeaderHidden(True)
        self.tbl_user_ports.header().setVisible(False)
        self.tbl_user_ports.header().setCascadingSectionResizes(False)
        self.tbl_user_ports.header().setHighlightSections(False)

        self.gridLayout_9.addWidget(self.tbl_user_ports, 1, 0, 1, 1)

        self.btn_user_ports_save = QPushButton(self.frame1)
        self.btn_user_ports_save.setObjectName(u"btn_user_ports_save")

        self.gridLayout_9.addWidget(self.btn_user_ports_save, 2, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame1, 0, 0, 1, 1)

        self.tabs_users.addTab(self.users_tab_usb_policices, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setEnabled(False)
        self.tabs_users.addTab(self.tab, "")

        self.gridLayout_6.addWidget(self.tabs_users, 1, 1, 1, 1)

        self.users_list_layout = QGroupBox(self.tab_users)
        self.users_list_layout.setObjectName(u"users_list_layout")
        self.users_list_layout.setMaximumSize(QSize(350, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.users_list_layout)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.le_search_user = QLineEdit(self.users_list_layout)
        self.le_search_user.setObjectName(u"le_search_user")
        self.le_search_user.setClearButtonEnabled(True)

        self.horizontalLayout_57.addWidget(self.le_search_user)

        self.btn_refresh_users_tab = QPushButton(self.users_list_layout)
        self.btn_refresh_users_tab.setObjectName(u"btn_refresh_users_tab")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.btn_refresh_users_tab.setIcon(icon5)
        self.btn_refresh_users_tab.setFlat(False)

        self.horizontalLayout_57.addWidget(self.btn_refresh_users_tab)


        self.verticalLayout_3.addLayout(self.horizontalLayout_57)

        self.list_users = QTreeWidget(self.users_list_layout)
        QTreeWidgetItem(self.list_users)
        self.list_users.setObjectName(u"list_users")
        sizePolicy1.setHeightForWidth(self.list_users.sizePolicy().hasHeightForWidth())
        self.list_users.setSizePolicy(sizePolicy1)
        self.list_users.setDragEnabled(False)
        self.list_users.setRootIsDecorated(False)
        self.list_users.setUniformRowHeights(False)
        self.list_users.setItemsExpandable(False)
        self.list_users.setSortingEnabled(True)
        self.list_users.setAnimated(True)
        self.list_users.setAllColumnsShowFocus(True)
        self.list_users.setWordWrap(False)
        self.list_users.setHeaderHidden(False)
        self.list_users.header().setHighlightSections(False)

        self.verticalLayout_3.addWidget(self.list_users)

        self.groupBox_16 = QGroupBox(self.users_list_layout)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_16)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_user_create = QPushButton(self.groupBox_16)
        self.btn_user_create.setObjectName(u"btn_user_create")

        self.verticalLayout_5.addWidget(self.btn_user_create)

        self.btn_user_delete = QPushButton(self.groupBox_16)
        self.btn_user_delete.setObjectName(u"btn_user_delete")

        self.verticalLayout_5.addWidget(self.btn_user_delete)

        self.btn_user_export = QPushButton(self.groupBox_16)
        self.btn_user_export.setObjectName(u"btn_user_export")

        self.verticalLayout_5.addWidget(self.btn_user_export)


        self.verticalLayout_3.addWidget(self.groupBox_16)


        self.gridLayout_6.addWidget(self.users_list_layout, 1, 0, 1, 1)

        self.tabs_general.addTab(self.tab_users, "")
        self.tab_groups = QWidget()
        self.tab_groups.setObjectName(u"tab_groups")
        self.tab_groups.setEnabled(True)
        self.gridLayout_14 = QGridLayout(self.tab_groups)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.groupBox_19 = QGroupBox(self.tab_groups)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setMaximumSize(QSize(350, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_19)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.le_search_group = QLineEdit(self.groupBox_19)
        self.le_search_group.setObjectName(u"le_search_group")
        self.le_search_group.setClearButtonEnabled(True)

        self.horizontalLayout_17.addWidget(self.le_search_group)

        self.btn_refresh_groups_tab = QPushButton(self.groupBox_19)
        self.btn_refresh_groups_tab.setObjectName(u"btn_refresh_groups_tab")
        self.btn_refresh_groups_tab.setIcon(icon5)
        self.btn_refresh_groups_tab.setFlat(False)

        self.horizontalLayout_17.addWidget(self.btn_refresh_groups_tab)


        self.verticalLayout_8.addLayout(self.horizontalLayout_17)

        self.list_groups = QTreeWidget(self.groupBox_19)
        QTreeWidgetItem(self.list_groups)
        QTreeWidgetItem(self.list_groups)
        QTreeWidgetItem(self.list_groups)
        self.list_groups.setObjectName(u"list_groups")
        self.list_groups.setTabletTracking(False)
        self.list_groups.setTabKeyNavigation(True)
        self.list_groups.setProperty(u"showDropIndicator", True)
        self.list_groups.setRootIsDecorated(False)
        self.list_groups.setSortingEnabled(True)
        self.list_groups.setAnimated(True)
        self.list_groups.header().setProperty(u"showSortIndicator", True)

        self.verticalLayout_8.addWidget(self.list_groups)

        self.groupBox_13 = QGroupBox(self.groupBox_19)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setEnabled(False)
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_14 = QPushButton(self.groupBox_13)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.horizontalLayout_15.addWidget(self.pushButton_14)

        self.pushButton_18 = QPushButton(self.groupBox_13)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.horizontalLayout_15.addWidget(self.pushButton_18)


        self.verticalLayout_8.addWidget(self.groupBox_13)

        self.groupBox_17 = QGroupBox(self.groupBox_19)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_17)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_group_new = QPushButton(self.groupBox_17)
        self.btn_group_new.setObjectName(u"btn_group_new")
        self.btn_group_new.setEnabled(False)
        self.btn_group_new.setCheckable(False)
        self.btn_group_new.setChecked(False)

        self.verticalLayout_6.addWidget(self.btn_group_new)

        self.btn_group_delete = QPushButton(self.groupBox_17)
        self.btn_group_delete.setObjectName(u"btn_group_delete")
        self.btn_group_delete.setEnabled(False)

        self.verticalLayout_6.addWidget(self.btn_group_delete)

        self.btn_group_export = QPushButton(self.groupBox_17)
        self.btn_group_export.setObjectName(u"btn_group_export")
        self.btn_group_export.setEnabled(False)

        self.verticalLayout_6.addWidget(self.btn_group_export)

        self.line = QFrame(self.groupBox_17)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.btn_group_start = QPushButton(self.groupBox_17)
        self.btn_group_start.setObjectName(u"btn_group_start")
        self.btn_group_start.setCheckable(False)
        self.btn_group_start.setChecked(False)

        self.verticalLayout_6.addWidget(self.btn_group_start)

        self.btn_group_restart = QPushButton(self.groupBox_17)
        self.btn_group_restart.setObjectName(u"btn_group_restart")
        self.btn_group_restart.setCheckable(False)
        self.btn_group_restart.setChecked(False)

        self.verticalLayout_6.addWidget(self.btn_group_restart)

        self.btn_group_stop = QPushButton(self.groupBox_17)
        self.btn_group_stop.setObjectName(u"btn_group_stop")
        self.btn_group_stop.setCheckable(False)
        self.btn_group_stop.setChecked(False)

        self.verticalLayout_6.addWidget(self.btn_group_stop)


        self.verticalLayout_8.addWidget(self.groupBox_17)


        self.gridLayout_14.addWidget(self.groupBox_19, 0, 0, 1, 1)

        self.tabs_group = QTabWidget(self.tab_groups)
        self.tabs_group.setObjectName(u"tabs_group")
        self.tabs_group.setEnabled(True)
        self.tab_group_params = QWidget()
        self.tab_group_params.setObjectName(u"tab_group_params")
        self.gridLayout_15 = QGridLayout(self.tab_group_params)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame_2 = QFrame(self.tab_group_params)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_15.addWidget(self.frame_2, 1, 0, 1, 1)

        self.groupBox_21 = QGroupBox(self.tab_group_params)
        self.groupBox_21.setObjectName(u"groupBox_21")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_21.sizePolicy().hasHeightForWidth())
        self.groupBox_21.setSizePolicy(sizePolicy3)
        self.gridLayout_8 = QGridLayout(self.groupBox_21)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupBox_23 = QGroupBox(self.groupBox_21)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setEnabled(False)
        self.horizontalLayout_26 = QHBoxLayout(self.groupBox_23)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_22 = QLabel(self.groupBox_23)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_26.addWidget(self.label_22)

        self.le_group_password = QLineEdit(self.groupBox_23)
        self.le_group_password.setObjectName(u"le_group_password")
        self.le_group_password.setEchoMode(QLineEdit.EchoMode.Normal)

        self.horizontalLayout_26.addWidget(self.le_group_password)


        self.gridLayout_8.addWidget(self.groupBox_23, 4, 0, 1, 1)

        self.users_save_button_2 = QPushButton(self.groupBox_21)
        self.users_save_button_2.setObjectName(u"users_save_button_2")
        self.users_save_button_2.setEnabled(False)

        self.gridLayout_8.addWidget(self.users_save_button_2, 5, 0, 1, 1)

        self.groupBox_25 = QGroupBox(self.groupBox_21)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.horizontalLayout_28 = QHBoxLayout(self.groupBox_25)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_26 = QLabel(self.groupBox_25)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_28.addWidget(self.label_26)

        self.le_group_port = QLineEdit(self.groupBox_25)
        self.le_group_port.setObjectName(u"le_group_port")

        self.horizontalLayout_28.addWidget(self.le_group_port)


        self.gridLayout_8.addWidget(self.groupBox_25, 1, 0, 1, 1)

        self.groupBox_24 = QGroupBox(self.groupBox_21)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.horizontalLayout_27 = QHBoxLayout(self.groupBox_24)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_24 = QLabel(self.groupBox_24)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_27.addWidget(self.label_24)

        self.le_group_name = QLineEdit(self.groupBox_24)
        self.le_group_name.setObjectName(u"le_group_name")

        self.horizontalLayout_27.addWidget(self.le_group_name)


        self.gridLayout_8.addWidget(self.groupBox_24, 0, 0, 1, 1)

        self.groupBox_28 = QGroupBox(self.groupBox_21)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.groupBox_28.setEnabled(False)
        self.horizontalLayout_33 = QHBoxLayout(self.groupBox_28)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_36 = QLabel(self.groupBox_28)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_33.addWidget(self.label_36)

        self.le_group_login = QLineEdit(self.groupBox_28)
        self.le_group_login.setObjectName(u"le_group_login")
        self.le_group_login.setEchoMode(QLineEdit.EchoMode.Normal)

        self.horizontalLayout_33.addWidget(self.le_group_login)


        self.gridLayout_8.addWidget(self.groupBox_28, 3, 0, 1, 1)

        self.groupBox_26 = QGroupBox(self.groupBox_21)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.horizontalLayout_29 = QHBoxLayout(self.groupBox_26)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_27 = QLabel(self.groupBox_26)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_29.addWidget(self.label_27)

        self.le_group_ip = QLineEdit(self.groupBox_26)
        self.le_group_ip.setObjectName(u"le_group_ip")

        self.horizontalLayout_29.addWidget(self.le_group_ip)


        self.gridLayout_8.addWidget(self.groupBox_26, 2, 0, 1, 1)


        self.gridLayout_15.addWidget(self.groupBox_21, 0, 0, 1, 1)

        self.tabs_group.addTab(self.tab_group_params, "")
        self.tab_group_usb = QWidget()
        self.tab_group_usb.setObjectName(u"tab_group_usb")
        self.tab_group_usb.setEnabled(False)
        self.gridLayout_24 = QGridLayout(self.tab_group_usb)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.groupBox_20 = QGroupBox(self.tab_group_usb)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.gridLayout_23 = QGridLayout(self.groupBox_20)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.groupBox_22 = QGroupBox(self.groupBox_20)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_22)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_6 = QPushButton(self.groupBox_22)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_12.addWidget(self.pushButton_6)

        self.pushButton_4 = QPushButton(self.groupBox_22)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_12.addWidget(self.pushButton_4)


        self.gridLayout_23.addWidget(self.groupBox_22, 1, 0, 1, 1)

        self.listWidget = QListWidget(self.groupBox_20)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setSortingEnabled(True)

        self.gridLayout_23.addWidget(self.listWidget, 0, 0, 1, 1)


        self.gridLayout_24.addWidget(self.groupBox_20, 0, 0, 1, 1)

        self.tabs_group.addTab(self.tab_group_usb, "")
        self.tab_group_access = QWidget()
        self.tab_group_access.setObjectName(u"tab_group_access")
        self.tab_group_access.setEnabled(False)
        self.gridLayout_25 = QGridLayout(self.tab_group_access)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.tabs_group.addTab(self.tab_group_access, "")

        self.gridLayout_14.addWidget(self.tabs_group, 0, 1, 1, 1)

        self.tabs_general.addTab(self.tab_groups, "")
        self.tab_ports = QWidget()
        self.tab_ports.setObjectName(u"tab_ports")
        self.tab_ports.setEnabled(False)
        self.gridLayout_12 = QGridLayout(self.tab_ports)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.lw_users = QGroupBox(self.tab_ports)
        self.lw_users.setObjectName(u"lw_users")
        self.lw_users.setMaximumSize(QSize(350, 16777215))
        self.gridLayout = QGridLayout(self.lw_users)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_10 = QPushButton(self.lw_users)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 3, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lineEdit_7 = QLineEdit(self.lw_users)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_16.addWidget(self.lineEdit_7)

        self.pushButton_8 = QPushButton(self.lw_users)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_16.addWidget(self.pushButton_8)


        self.gridLayout.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.lw_users)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_13 = QPushButton(self.groupBox_4)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout_8.addWidget(self.pushButton_13)

        self.pushButton_11 = QPushButton(self.groupBox_4)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_8.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.groupBox_4)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_8.addWidget(self.pushButton_12)


        self.gridLayout.addWidget(self.groupBox_4, 2, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.lw_users)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout.addWidget(self.pushButton_15, 4, 0, 1, 1)

        self.treeWidget = QTreeWidget(self.lw_users)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setSortingEnabled(True)

        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 1)


        self.gridLayout_12.addWidget(self.lw_users, 0, 0, 1, 1)

        self.tabs_ports = QTabWidget(self.tab_ports)
        self.tabs_ports.setObjectName(u"tabs_ports")
        self.tabWidget_3Page1 = QWidget()
        self.tabWidget_3Page1.setObjectName(u"tabWidget_3Page1")
        self.gridLayout_17 = QGridLayout(self.tabWidget_3Page1)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.groupBox_2 = QGroupBox(self.tabWidget_3Page1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.groupBox_2.setAcceptDrops(False)
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_10.addWidget(self.label_4)

        self.checkBox_2 = QCheckBox(self.groupBox_5)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy4)
        self.checkBox_2.setChecked(True)

        self.horizontalLayout_10.addWidget(self.checkBox_2)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.groupBox_9 = QGroupBox(self.groupBox_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.horizontalLayout_18 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.groupBox_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_18.addWidget(self.label_13)

        self.label_9 = QLabel(self.groupBox_9)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)

        self.horizontalLayout_18.addWidget(self.label_9)


        self.verticalLayout_4.addWidget(self.groupBox_9)

        self.groupBox_10 = QGroupBox(self.groupBox_2)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.horizontalLayout_20 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_15 = QLabel(self.groupBox_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_20.addWidget(self.label_15)

        self.label_16 = QLabel(self.groupBox_10)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)

        self.horizontalLayout_20.addWidget(self.label_16)


        self.verticalLayout_4.addWidget(self.groupBox_10)

        self.groupBox_6 = QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.groupBox_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_11.addWidget(self.label_5)

        self.comboBox_3 = QComboBox(self.groupBox_6)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy5)

        self.horizontalLayout_11.addWidget(self.comboBox_3)


        self.verticalLayout_4.addWidget(self.groupBox_6)

        self.groupBox_11 = QGroupBox(self.groupBox_2)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.horizontalLayout_21 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_17 = QLabel(self.groupBox_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_21.addWidget(self.label_17)

        self.lineEdit_8 = QLineEdit(self.groupBox_11)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy5.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy5)

        self.horizontalLayout_21.addWidget(self.lineEdit_8)


        self.verticalLayout_4.addWidget(self.groupBox_11)

        self.pushButton_9 = QPushButton(self.groupBox_2)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_4.addWidget(self.pushButton_9)


        self.gridLayout_17.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.tabWidget_3Page1)
        self.frame_4.setObjectName(u"frame_4")

        self.gridLayout_17.addWidget(self.frame_4, 1, 0, 1, 1)

        self.tabs_ports.addTab(self.tabWidget_3Page1, "")
        self.usb_tab_access_list = QWidget()
        self.usb_tab_access_list.setObjectName(u"usb_tab_access_list")
        self.usb_tab_access_list.setAutoFillBackground(False)
        self.usb_tab_access_list.setStyleSheet(u"")
        self.gridLayout_13 = QGridLayout(self.usb_tab_access_list)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.groupBox_3 = QGroupBox(self.usb_tab_access_list)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_14 = QFrame(self.groupBox_3)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy3.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy3)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lineEdit_10 = QLineEdit(self.frame_14)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_9.addWidget(self.lineEdit_10)

        self.pushButton_3 = QPushButton(self.frame_14)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_9.addWidget(self.pushButton_3)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.listWidget_3 = QListWidget(self.groupBox_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        self.listWidget_3.setObjectName(u"listWidget_3")
        sizePolicy.setHeightForWidth(self.listWidget_3.sizePolicy().hasHeightForWidth())
        self.listWidget_3.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.listWidget_3)

        self.groupBox_8 = QGroupBox(self.groupBox_3)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy3.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy3)
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton = QPushButton(self.groupBox_8)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_7.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox_8)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_7.addWidget(self.pushButton_2)


        self.verticalLayout_2.addWidget(self.groupBox_8)


        self.gridLayout_13.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.tabs_ports.addTab(self.usb_tab_access_list, "")

        self.gridLayout_12.addWidget(self.tabs_ports, 0, 1, 1, 1)

        self.tabs_general.addTab(self.tab_ports, "")
        self.tab_logs = QWidget()
        self.tab_logs.setObjectName(u"tab_logs")
        self.tab_logs.setEnabled(False)
        self.tabs_general.addTab(self.tab_logs, "")

        self.gridLayout_11.addWidget(self.tabs_general, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1175, 22))
        self.menu_1 = QMenu(self.menuBar)
        self.menu_1.setObjectName(u"menu_1")
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menu)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_2.setEnabled(False)
        self.menu_3 = QMenu(self.menu)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_3.setEnabled(False)
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
#if QT_CONFIG(shortcut)
        self.users_fullname_label.setBuddy(self.le_user_cn)
        self.label_2.setBuddy(self.le_user_name)
        self.label_11.setBuddy(self.le_user_default_ip)
        self.label_56.setBuddy(self.le_user_pass)
        self.label_12.setBuddy(self.le_user_email)
        self.label_10.setBuddy(self.le_user_comment)
        self.label_44.setBuddy(self.le_user_tg_id)
        self.label_55.setBuddy(self.le_user_tg_code)
        self.label_3.setBuddy(self.cb_user_active)
#endif // QT_CONFIG(shortcut)

        self.menuBar.addAction(self.menu_1.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.menu_1.addAction(self.btn_check_update)
        self.menu_1.addAction(self.btn_about_program)
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.btn_reboot_server)
        self.menu_2.addAction(self.btn_check_user_access_group)
        self.menu_2.addAction(self.btn_check_user_access_port)
        self.menu_3.addAction(self.btn_backup_new)
        self.menu_3.addAction(self.btn_backup_restore)

        self.retranslateUi(MainWindow)

        self.tabs_general.setCurrentIndex(0)
        self.tabs_users.setCurrentIndex(0)
        self.btn_user_save_params.setDefault(False)
        self.stack_user_policies.setCurrentIndex(0)
        self.btn_refresh_users_tab.setDefault(False)
        self.tabs_group.setCurrentIndex(0)
        self.tabs_ports.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"hubM Admin Panel", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0441\u0435\u0440\u0432\u0435\u0440", None))
        self.btn_check_update.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043a\u0435\u043d", None))
        self.btn_check_user_access_group.setText(QCoreApplication.translate("MainWindow", u"\u043a \u0433\u0440\u0443\u043f\u043f\u0435", None))
        self.btn_check_user_access_port.setText(QCoreApplication.translate("MainWindow", u"\u043a \u043f\u043e\u0440\u0442\u0443", None))
        self.btn_about_program.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.btn_reboot_server.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0441\u0435\u0440\u0432\u0435\u0440", None))
        self.btn_backup_new.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u043a\u043e\u043f\u0438\u044f", None))
        self.btn_backup_restore.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.groupBox_15.setTitle("")
        self.DevButton2.setText(QCoreApplication.translate("MainWindow", u"DevButton2", None))
        self.DevButton1.setText(QCoreApplication.translate("MainWindow", u"DevButton1", None))
        self.groupBox_14.setTitle("")
        self.tabs_general.setTabText(self.tabs_general.indexOf(self.tab_dashboard), QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0448\u0431\u043e\u0440\u0434", None))
        self.users_fullname_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u043e\u0435 \u0438\u043c\u044f", None))
        self.le_user_cn.setText("")
        self.le_user_cn.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u0432\u0430\u043d\u043e\u0432 \u0418\u0432\u0430\u043d \u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u043e\u0435 \u0438\u043c\u044f", None))
        self.le_user_name.setText("")
        self.le_user_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ii.ivanov", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 IP", None))
        self.le_user_default_ip.setInputMask("")
        self.le_user_default_ip.setText("")
        self.le_user_default_ip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"255.255.255.255", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.le_user_pass.setInputMask("")
        self.le_user_pass.setText("")
        self.le_user_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MyTopP@ssw0rd", None))
        self.btn_show_pass.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.le_user_email.setText("")
        self.le_user_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ii.ivanov@unistroyrf.ru", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.le_user_comment.setText("")
        self.le_user_comment.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u042d\u043d\u0435\u0440\u0433\u043e\u0440\u0435\u0441\u0443\u0440\u0441, \u044e\u0440\u0438\u0441\u0442", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Telegram id", None))
        self.le_user_tg_id.setText("")
        self.le_user_tg_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"912561677", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Telegram code", None))
        self.le_user_tg_code.setText("")
        self.le_user_tg_code.setPlaceholderText(QCoreApplication.translate("MainWindow", u"!hahg@21ga", None))
        self.btn_show_tg_code.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.cb_user_active.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432\u0435\u043d", None))
        self.btn_user_save_params.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tabs_users.setTabText(self.tabs_users.indexOf(self.users_tab_info), QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        ___qtablewidgetitem = self.tbl_user_policies.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0441\u0442\u0443\u043f", None));
        ___qtablewidgetitem1 = self.tbl_user_policies.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"IP-\u0430\u0434\u0440\u0435\u0441\u0430", None));
        ___qtablewidgetitem2 = self.tbl_user_policies.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"USB-\u0444\u0438\u043b\u044c\u0442\u0440", None));
        ___qtablewidgetitem3 = self.tbl_user_policies.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Auth-Method", None));
        ___qtablewidgetitem4 = self.tbl_user_policies.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"OTP-\u0441\u0435\u043a\u0440\u0435\u0442", None));
        ___qtablewidgetitem5 = self.tbl_user_policies.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None));
        ___qtablewidgetitem6 = self.tbl_user_policies.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Permit-Login", None));
        ___qtablewidgetitem7 = self.tbl_user_policies.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Can kick", None));
        ___qtablewidgetitem8 = self.tbl_user_policies.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Kickable", None));
        ___qtablewidgetitem9 = self.tbl_user_policies.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Until", None));
        ___qtablewidgetitem10 = self.tbl_user_policies.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Smart", None));
        ___qtablewidgetitem11 = self.tbl_user_policies.verticalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Unistroy-Region", None));
        ___qtablewidgetitem12 = self.tbl_user_policies.verticalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"USKStandart", None));

        __sortingEnabled = self.tbl_user_policies.isSortingEnabled()
        self.tbl_user_policies.setSortingEnabled(False)
        ___qtablewidgetitem13 = self.tbl_user_policies.item(0, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"{10.20.30.100,10.20.1.22}", None));
        ___qtablewidgetitem14 = self.tbl_user_policies.item(0, 9)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"2024.01.23 15:48", None));
        ___qtablewidgetitem15 = self.tbl_user_policies.item(1, 9)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"2024.02.23 15:48", None));
        ___qtablewidgetitem16 = self.tbl_user_policies.item(2, 9)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"2023.01.23 15:48", None));
        self.tbl_user_policies.setSortingEnabled(__sortingEnabled)

        ___qtreewidgetitem = self.tree_user_policies.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));

        __sortingEnabled1 = self.tree_user_policies.isSortingEnabled()
        self.tree_user_policies.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.tree_user_policies.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Smart", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0434\u043e\u0447\u0435\u0440\u043d\u0438\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(3)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem1.child(4)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0434\u043e\u0447\u0435\u0440\u043d\u0438\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qtreewidgetitem7 = self.tree_user_policies.topLevelItem(1)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem7.child(0)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0434\u043e\u0447\u0435\u0440\u043d\u0438\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem7.child(1)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem7.child(2)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem7.child(3)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem7.child(4)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        self.tree_user_policies.setSortingEnabled(__sortingEnabled1)

        self.groupBox_18.setTitle("")
        self.btn_user_policies_create.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u043f\u043e\u043b\u0438\u0442\u0438\u043a\u0430", None))
        self.btn_user_policies_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u043b\u0438\u0442\u0438\u043a\u0443", None))
        self.btn_change_view_user_policies.setText("")
        self.btn_show_user_policies.setText("")
        self.btn_user_policies_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tabs_users.setTabText(self.tabs_users.indexOf(self.users_tab_group_policies), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0438\u0442\u0438\u043a\u0438 \u0433\u0440\u0443\u043f\u043f", None))
        self.btn_user_ports_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tabs_users.setTabText(self.tabs_users.indexOf(self.users_tab_usb_policices), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0438\u0442\u0438\u043a\u0438 USB-\u043f\u043e\u0440\u0442\u043e\u0432", None))
        self.tabs_users.setTabText(self.tabs_users.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c", None))
        self.users_list_layout.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.le_search_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.btn_refresh_users_tab.setText("")
        ___qtreewidgetitem13 = self.list_users.headerItem()
        ___qtreewidgetitem13.setText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u043e\u0435 \u0438\u043c\u044f", None));
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u043e\u0435 \u0438\u043c\u044f", None));

        __sortingEnabled2 = self.list_users.isSortingEnabled()
        self.list_users.setSortingEnabled(False)
        ___qtreewidgetitem14 = self.list_users.topLevelItem(0)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        self.list_users.setSortingEnabled(__sortingEnabled2)

        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        self.btn_user_create.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.btn_user_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.btn_user_export.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.tabs_general.setTabText(self.tabs_general.indexOf(self.tab_users), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u044b", None))
        self.le_search_group.setText("")
        self.le_search_group.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.btn_refresh_groups_tab.setText("")
        ___qtreewidgetitem15 = self.list_groups.headerItem()
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u043e\u0435 \u0438\u043c\u044f", None));

        __sortingEnabled3 = self.list_groups.isSortingEnabled()
        self.list_groups.setSortingEnabled(False)
        ___qtreewidgetitem16 = self.list_groups.topLevelItem(0)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"Unistroy-Region", None));
        ___qtreewidgetitem17 = self.list_groups.topLevelItem(1)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"Smart", None));
        ___qtreewidgetitem18 = self.list_groups.topLevelItem(2)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"Sever-Volzh", None));
        self.list_groups.setSortingEnabled(__sortingEnabled3)

        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"TCP \u043f\u043e\u0440\u0442", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        self.btn_group_new.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430", None))
        self.btn_group_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443", None))
        self.btn_group_export.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.btn_group_start.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443", None))
        self.btn_group_restart.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443", None))
        self.btn_group_stop.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443", None))
        self.groupBox_21.setTitle("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.le_group_password.setText("")
        self.le_group_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.users_save_button_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"TCP \u043f\u043e\u0440\u0442", None))
        self.le_group_port.setText("")
        self.le_group_port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"7501", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.le_group_name.setText("")
        self.le_group_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Group Name", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.le_group_login.setText("")
        self.le_group_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"IP/Hostname", None))
        self.le_group_ip.setText("")
        self.le_group_ip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"10.10.8.161", None))
        self.tabs_group.setTabText(self.tabs_group.indexOf(self.tab_group_params), QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.groupBox_20.setTitle("")
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0440\u0442", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u0440\u0442", None))

        __sortingEnabled4 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0430\u0440\u0442 \u0410\u0445\u0442\u044f\u043c\u043e\u0432", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043d\u0420\u0435\u04331", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043d\u0420\u0435\u04332", None));
        self.listWidget.setSortingEnabled(__sortingEnabled4)

        self.tabs_group.setTabText(self.tabs_group.indexOf(self.tab_group_usb), QCoreApplication.translate("MainWindow", u"USB-\u043f\u043e\u0440\u0442\u044b", None))
        self.tabs_group.setTabText(self.tabs_group.indexOf(self.tab_group_access), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0441\u0442\u0443\u043f\u044b", None))
        self.tabs_general.setTabText(self.tabs_general.indexOf(self.tab_groups), QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u044b", None))
        self.lw_users.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u0442\u044b", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0440\u0442", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Virtual Port", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Bus", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u0440\u0442", None))
        ___qtreewidgetitem19 = self.treeWidget.headerItem()
        ___qtreewidgetitem19.setText(2, QCoreApplication.translate("MainWindow", u"Group", None));
        ___qtreewidgetitem19.setText(1, QCoreApplication.translate("MainWindow", u"VID", None));
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None));

        __sortingEnabled5 = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem20 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem20.setText(2, QCoreApplication.translate("MainWindow", u"Smart", None));
        ___qtreewidgetitem20.setText(1, QCoreApplication.translate("MainWindow", u"1.1", None));
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"\u0418\u043a\u0441\u043e\u043d \u0414\u0435\u0432\u0435\u043b\u043e\u043f\u043c\u0435\u043d\u0442 \u0411\u0443\u043b\u0430\u0442\u043e\u0432\u0430", None));
        ___qtreewidgetitem21 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem21.setText(2, QCoreApplication.translate("MainWindow", u"Smart", None));
        ___qtreewidgetitem21.setText(1, QCoreApplication.translate("MainWindow", u"1.2", None));
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MainWindow", u"\u0418\u043a\u0441\u043e\u043d \u0414\u0435\u0432\u0435\u043b\u043e\u043f\u043c\u0435\u043d\u0442 \u0410\u0445\u0442\u044f\u043c\u043e\u0432", None));
        ___qtreewidgetitem22 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem22.setText(1, QCoreApplication.translate("MainWindow", u"1.3", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled5)

        self.groupBox_2.setTitle("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432\u0435\u043d", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Virtual Port", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"1.21", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Bus", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"1.2.1-2.2.4", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u0438\u0442", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Smart", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Unistroy-Region", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"USKStandart", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043a\u0441\u043e\u043d \u0414\u0435\u0432\u0435\u043b\u043e\u043f\u043c\u0435\u043d\u0442 \u0410\u0445\u0442\u044f\u043c\u043e\u0432", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tabs_ports.setTabText(self.tabs_ports.indexOf(self.tabWidget_3Page1), QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.groupBox_3.setTitle("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))

        __sortingEnabled6 = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        ___qlistwidgetitem3 = self.listWidget_3.item(0)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem4 = self.listWidget_3.item(1)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem5 = self.listWidget_3.item(2)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem6 = self.listWidget_3.item(3)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem7 = self.listWidget_3.item(4)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem8 = self.listWidget_3.item(5)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem9 = self.listWidget_3.item(6)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem10 = self.listWidget_3.item(7)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem11 = self.listWidget_3.item(8)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem12 = self.listWidget_3.item(9)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem13 = self.listWidget_3.item(10)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem14 = self.listWidget_3.item(11)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem15 = self.listWidget_3.item(12)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem16 = self.listWidget_3.item(13)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem17 = self.listWidget_3.item(14)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem18 = self.listWidget_3.item(15)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem19 = self.listWidget_3.item(16)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem20 = self.listWidget_3.item(17)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem21 = self.listWidget_3.item(18)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem22 = self.listWidget_3.item(19)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem23 = self.listWidget_3.item(20)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem24 = self.listWidget_3.item(21)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem25 = self.listWidget_3.item(22)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem26 = self.listWidget_3.item(23)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem27 = self.listWidget_3.item(24)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem28 = self.listWidget_3.item(25)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem29 = self.listWidget_3.item(26)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem30 = self.listWidget_3.item(27)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem31 = self.listWidget_3.item(28)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem32 = self.listWidget_3.item(29)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem33 = self.listWidget_3.item(30)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem34 = self.listWidget_3.item(31)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        self.listWidget_3.setSortingEnabled(__sortingEnabled6)

        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u043e\u0435 \u0438\u043c\u044f", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u043e\u0435 \u0438\u043c\u044f", None))
        self.tabs_ports.setTabText(self.tabs_ports.indexOf(self.usb_tab_access_list), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0441\u0442\u0443\u043f\u044b", None))
        self.tabs_general.setTabText(self.tabs_general.indexOf(self.tab_ports), QCoreApplication.translate("MainWindow", u"USB-\u043f\u043e\u0440\u0442\u044b", None))
        self.tabs_general.setTabText(self.tabs_general.indexOf(self.tab_logs), QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438", None))
        self.menu_1.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0434\u043e\u0441\u0442\u0443\u043f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0435\u0440\u0432\u043d\u043e\u0435 \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
    # retranslateUi

