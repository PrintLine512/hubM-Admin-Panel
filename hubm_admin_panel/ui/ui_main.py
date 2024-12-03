# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QAction, QFont, QIcon)
from PySide6.QtWidgets import (QAbstractItemView, QCheckBox, QComboBox,
                               QFrame, QGridLayout, QGroupBox, QHBoxLayout,
                               QLabel, QLayout, QLineEdit,
                               QMenu, QMenuBar, QPushButton,
                               QSizePolicy, QStackedWidget, QStatusBar, QTabWidget,
                               QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem,
                               QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1126, 941)
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
        self.users_list_layout = QGroupBox(self.tab_users)
        self.users_list_layout.setObjectName(u"users_list_layout")
        self.users_list_layout.setMinimumSize(QSize(350, 0))
        self.users_list_layout.setMaximumSize(QSize(350, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.users_list_layout)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.le_search_user = QLineEdit(self.users_list_layout)
        self.le_search_user.setObjectName(u"le_search_user")
        self.le_search_user.setClearButtonEnabled(True)

        self.horizontalLayout_57.addWidget(self.le_search_user)

        self.verticalLayout_3.addLayout(self.horizontalLayout_57)

        self.list_users = QTreeWidget(self.users_list_layout)
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
        self.frame_7 = QFrame(self.users_tab_info)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setLineWidth(0)
        self.gridLayout_10 = QGridLayout(self.frame_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.frame_7)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.users_fullname_label = QLabel(self.groupBox)
        self.users_fullname_label.setObjectName(u"users_fullname_label")
        sizePolicy.setHeightForWidth(self.users_fullname_label.sizePolicy().hasHeightForWidth())
        self.users_fullname_label.setSizePolicy(sizePolicy)
        self.users_fullname_label.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_23.addWidget(self.users_fullname_label)

        self.le_user_cn = QLineEdit(self.groupBox)
        self.le_user_cn.setObjectName(u"le_user_cn")
        self.le_user_cn.setInputMethodHints(Qt.InputMethodHint.ImhNone)

        self.horizontalLayout_23.addWidget(self.le_user_cn)

        self.verticalLayout_10.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_24.addWidget(self.label_2)

        self.le_user_name = QLineEdit(self.groupBox)
        self.le_user_name.setObjectName(u"le_user_name")
        self.le_user_name.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.le_user_name.setDragEnabled(False)
        self.le_user_name.setReadOnly(True)

        self.horizontalLayout_24.addWidget(self.le_user_name)

        self.verticalLayout_10.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_25.addWidget(self.label_11)

        self.le_user_default_ip = QLineEdit(self.groupBox)
        self.le_user_default_ip.setObjectName(u"le_user_default_ip")
        self.le_user_default_ip.setFrame(True)
        self.le_user_default_ip.setDragEnabled(False)

        self.horizontalLayout_25.addWidget(self.le_user_default_ip)

        self.verticalLayout_10.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_56 = QLabel(self.groupBox)
        self.label_56.setObjectName(u"label_56")
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        self.label_56.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_26.addWidget(self.label_56)

        self.le_user_pass = QLineEdit(self.groupBox)
        self.le_user_pass.setObjectName(u"le_user_pass")
        self.le_user_pass.setInputMethodHints(
            Qt.InputMethodHint.ImhNoAutoUppercase | Qt.InputMethodHint.ImhNoPredictiveText | Qt.InputMethodHint.ImhSensitiveData)
        self.le_user_pass.setFrame(True)
        self.le_user_pass.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.horizontalLayout_26.addWidget(self.le_user_pass)

        self.btn_show_pass = QPushButton(self.groupBox)
        self.btn_show_pass.setObjectName(u"btn_show_pass")
        icon3 = QIcon()
        icon3.addFile(u":/res/icons/eye_on.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/res/icons/eye_off.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_show_pass.setIcon(icon3)
        self.btn_show_pass.setCheckable(True)
        self.btn_show_pass.setAutoRepeat(False)
        self.btn_show_pass.setAutoExclusive(False)

        self.horizontalLayout_26.addWidget(self.btn_show_pass)

        self.verticalLayout_10.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_27.addWidget(self.label_12)

        self.le_user_email = QLineEdit(self.groupBox)
        self.le_user_email.setObjectName(u"le_user_email")

        self.horizontalLayout_27.addWidget(self.le_user_email)

        self.verticalLayout_10.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_28.addWidget(self.label_10)

        self.le_user_comment = QLineEdit(self.groupBox)
        self.le_user_comment.setObjectName(u"le_user_comment")

        self.horizontalLayout_28.addWidget(self.le_user_comment)

        self.verticalLayout_10.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_44 = QLabel(self.groupBox)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_29.addWidget(self.label_44)

        self.le_user_tg_id = QLineEdit(self.groupBox)
        self.le_user_tg_id.setObjectName(u"le_user_tg_id")

        self.horizontalLayout_29.addWidget(self.le_user_tg_id)

        self.verticalLayout_10.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_55 = QLabel(self.groupBox)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_30.addWidget(self.label_55)

        self.le_user_tg_code = QLineEdit(self.groupBox)
        self.le_user_tg_code.setObjectName(u"le_user_tg_code")
        self.le_user_tg_code.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.horizontalLayout_30.addWidget(self.le_user_tg_code)

        self.btn_show_tg_code = QPushButton(self.groupBox)
        self.btn_show_tg_code.setObjectName(u"btn_show_tg_code")
        self.btn_show_tg_code.setIcon(icon3)
        self.btn_show_tg_code.setCheckable(True)

        self.horizontalLayout_30.addWidget(self.btn_show_tg_code)

        self.verticalLayout_10.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setMaximumSize(QSize(150, 16777215))
        self.label_3.setBaseSize(QSize(0, 0))
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setTextFormat(Qt.TextFormat.AutoText)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.label_3)

        self.cb_user_active = QCheckBox(self.groupBox)
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

        self.horizontalLayout_31.addWidget(self.cb_user_active)

        self.verticalLayout_10.addLayout(self.horizontalLayout_31)

        self.btn_user_save_params = QPushButton(self.groupBox)
        self.btn_user_save_params.setObjectName(u"btn_user_save_params")
        self.btn_user_save_params.setFlat(False)

        self.verticalLayout_10.addWidget(self.btn_user_save_params)

        self.verticalLayout.addWidget(self.groupBox)

        self.gridLayout_10.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.frame_7)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_5 = QGridLayout(self.groupBox_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_18 = QFrame(self.groupBox_7)
        self.frame_18.setObjectName(u"frame_18")
        self.gridLayout_21 = QGridLayout(self.frame_18)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_18)
        self.frame_5.setObjectName(u"frame_5")
        self.horizontalLayout_14 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_user_policies_create = QPushButton(self.frame_5)
        self.btn_user_policies_create.setObjectName(u"btn_user_policies_create")

        self.horizontalLayout_14.addWidget(self.btn_user_policies_create)

        self.btn_user_policies_delete = QPushButton(self.frame_5)
        self.btn_user_policies_delete.setObjectName(u"btn_user_policies_delete")

        self.horizontalLayout_14.addWidget(self.btn_user_policies_delete)

        self.btn_change_view_user_policies = QPushButton(self.frame_5)
        self.btn_change_view_user_policies.setObjectName(u"btn_change_view_user_policies")
        self.btn_change_view_user_policies.setMaximumSize(QSize(30, 16777215))
        icon4 = QIcon()
        icon4.addFile(u":/res/icons/strings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_change_view_user_policies.setIcon(icon4)
        self.btn_change_view_user_policies.setCheckable(False)

        self.horizontalLayout_14.addWidget(self.btn_change_view_user_policies)

        self.btn_show_user_policies = QPushButton(self.frame_5)
        self.btn_show_user_policies.setObjectName(u"btn_show_user_policies")
        self.btn_show_user_policies.setMaximumSize(QSize(30, 16777215))
        self.btn_show_user_policies.setIcon(icon3)
        self.btn_show_user_policies.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.btn_show_user_policies)

        self.gridLayout_21.addWidget(self.frame_5, 0, 0, 1, 1)

        self.btn_user_policies_save = QPushButton(self.frame_18)
        self.btn_user_policies_save.setObjectName(u"btn_user_policies_save")

        self.gridLayout_21.addWidget(self.btn_user_policies_save, 1, 0, 1, 1)

        self.gridLayout_5.addWidget(self.frame_18, 1, 0, 1, 1)

        self.stack_user_policies = QStackedWidget(self.groupBox_7)
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
        self.tbl_user_policies.setObjectName(u"tbl_user_policies")
        self.tbl_user_policies.setEnabled(True)
        self.tbl_user_policies.setLineWidth(100)
        self.tbl_user_policies.setMidLineWidth(50)
        self.tbl_user_policies.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tbl_user_policies.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbl_user_policies.setSortingEnabled(False)
        self.tbl_user_policies.setRowCount(0)
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
        font2 = QFont()
        font2.setBold(False)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font2);
        self.tree_user_policies.setHeaderItem(__qtreewidgetitem)
        self.tree_user_policies.setObjectName(u"tree_user_policies")

        self.gridLayout_30.addWidget(self.tree_user_policies, 0, 0, 1, 1)

        self.stack_user_policies.addWidget(self.page_2)

        self.gridLayout_5.addWidget(self.stack_user_policies, 0, 0, 1, 1)

        self.gridLayout_10.addWidget(self.groupBox_7, 2, 0, 1, 1)

        self.gridLayout_2.addWidget(self.frame_7, 0, 0, 1, 1)

        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.tabs_users.addTab(self.users_tab_info, "")
        self.users_tab_usb_policices = QWidget()
        self.users_tab_usb_policices.setObjectName(u"users_tab_usb_policices")
        self.users_tab_usb_policices.setEnabled(True)
        self.gridLayout_7 = QGridLayout(self.users_tab_usb_policices)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame = QFrame(self.users_tab_usb_policices)
        self.frame.setObjectName(u"frame")
        self.gridLayout_9 = QGridLayout(self.frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_7.addWidget(self.frame, 0, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.users_tab_usb_policices)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_13 = QGridLayout(self.groupBox_3)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.tbl_user_ports = QTreeWidget(self.groupBox_3)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.tbl_user_ports.setHeaderItem(__qtreewidgetitem1)
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

        self.gridLayout_13.addWidget(self.tbl_user_ports, 0, 0, 1, 1)

        self.btn_user_ports_save = QPushButton(self.groupBox_3)
        self.btn_user_ports_save.setObjectName(u"btn_user_ports_save")

        self.gridLayout_13.addWidget(self.btn_user_ports_save, 1, 0, 1, 1)

        self.gridLayout_7.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.tabs_users.addTab(self.users_tab_usb_policices, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setEnabled(False)
        self.tabs_users.addTab(self.tab, "")

        self.gridLayout_6.addWidget(self.tabs_users, 1, 1, 1, 1)

        self.tabs_general.addTab(self.tab_users, "")
        self.tab_groups = QWidget()
        self.tab_groups.setObjectName(u"tab_groups")
        self.tab_groups.setEnabled(True)
        self.gridLayout_14 = QGridLayout(self.tab_groups)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.groups_list_layout = QGroupBox(self.tab_groups)
        self.groups_list_layout.setObjectName(u"groups_list_layout")
        self.groups_list_layout.setMinimumSize(QSize(350, 0))
        self.groups_list_layout.setMaximumSize(QSize(350, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.groups_list_layout)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.le_search_group = QLineEdit(self.groups_list_layout)
        self.le_search_group.setObjectName(u"le_search_group")
        self.le_search_group.setClearButtonEnabled(True)

        self.horizontalLayout_17.addWidget(self.le_search_group)

        self.verticalLayout_8.addLayout(self.horizontalLayout_17)

        self.list_groups = QTreeWidget(self.groups_list_layout)
        self.list_groups.setObjectName(u"list_groups")
        self.list_groups.setTabletTracking(False)
        self.list_groups.setTabKeyNavigation(True)
        self.list_groups.setProperty(u"showDropIndicator", True)
        self.list_groups.setRootIsDecorated(False)
        self.list_groups.setSortingEnabled(True)
        self.list_groups.setAnimated(True)
        self.list_groups.header().setProperty(u"showSortIndicator", True)

        self.verticalLayout_8.addWidget(self.list_groups)

        self.groupBox_17 = QGroupBox(self.groups_list_layout)
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

        self.btn_group_stop = QPushButton(self.groupBox_17)
        self.btn_group_stop.setObjectName(u"btn_group_stop")
        self.btn_group_stop.setCheckable(False)
        self.btn_group_stop.setChecked(False)

        self.verticalLayout_6.addWidget(self.btn_group_stop)

        self.btn_group_restart = QPushButton(self.groupBox_17)
        self.btn_group_restart.setObjectName(u"btn_group_restart")
        self.btn_group_restart.setCheckable(False)
        self.btn_group_restart.setChecked(False)

        self.verticalLayout_6.addWidget(self.btn_group_restart)

        self.verticalLayout_8.addWidget(self.groupBox_17)

        self.gridLayout_14.addWidget(self.groups_list_layout, 0, 0, 1, 1)

        self.tabs_group = QTabWidget(self.tab_groups)
        self.tabs_group.setObjectName(u"tabs_group")
        self.tabs_group.setEnabled(True)
        self.tab_group_params = QWidget()
        self.tab_group_params.setObjectName(u"tab_group_params")
        self.gridLayout_15 = QGridLayout(self.tab_group_params)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame_21 = QFrame(self.tab_group_params)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.gridLayout_8 = QGridLayout(self.frame_21)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_group_save = QPushButton(self.frame_21)
        self.btn_group_save.setObjectName(u"btn_group_save")
        self.btn_group_save.setEnabled(True)

        self.gridLayout_8.addWidget(self.btn_group_save, 4, 0, 1, 1)

        self.groupBox_24 = QGroupBox(self.frame_21)
        self.groupBox_24.setObjectName(u"groupBox_24")
        sizePolicy2.setHeightForWidth(self.groupBox_24.sizePolicy().hasHeightForWidth())
        self.groupBox_24.setSizePolicy(sizePolicy2)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_24)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.frame_group_status = QHBoxLayout()
        self.frame_group_status.setObjectName(u"frame_group_status")
        self.label_28 = QLabel(self.groupBox_24)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(150, 0))

        self.frame_group_status.addWidget(self.label_28)

        self.verticalLayout_9.addLayout(self.frame_group_status)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_24 = QLabel(self.groupBox_24)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_9.addWidget(self.label_24)

        self.le_group_name = QLineEdit(self.groupBox_24)
        self.le_group_name.setObjectName(u"le_group_name")

        self.horizontalLayout_9.addWidget(self.le_group_name)

        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_26 = QLabel(self.groupBox_24)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_13.addWidget(self.label_26)

        self.le_group_port = QLineEdit(self.groupBox_24)
        self.le_group_port.setObjectName(u"le_group_port")

        self.horizontalLayout_13.addWidget(self.le_group_port)

        self.verticalLayout_9.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_27 = QLabel(self.groupBox_24)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_15.addWidget(self.label_27)

        self.le_group_ip = QLineEdit(self.groupBox_24)
        self.le_group_ip.setObjectName(u"le_group_ip")

        self.horizontalLayout_15.addWidget(self.le_group_ip)

        self.verticalLayout_9.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_36 = QLabel(self.groupBox_24)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_19.addWidget(self.label_36)

        self.le_group_login = QLineEdit(self.groupBox_24)
        self.le_group_login.setObjectName(u"le_group_login")
        self.le_group_login.setEchoMode(QLineEdit.EchoMode.Normal)

        self.horizontalLayout_19.addWidget(self.le_group_login)

        self.verticalLayout_9.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_22 = QLabel(self.groupBox_24)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_22.addWidget(self.label_22)

        self.le_group_password = QLineEdit(self.groupBox_24)
        self.le_group_password.setObjectName(u"le_group_password")
        self.le_group_password.setEchoMode(QLineEdit.EchoMode.Normal)

        self.horizontalLayout_22.addWidget(self.le_group_password)

        self.verticalLayout_9.addLayout(self.horizontalLayout_22)

        self.gridLayout_8.addWidget(self.groupBox_24, 0, 0, 1, 1)

        self.groupBox1 = QGroupBox(self.frame_21)
        self.groupBox1.setObjectName(u"groupBox1")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.list_group_usb = QTreeWidget(self.groupBox1)
        self.list_group_usb.setObjectName(u"list_group_usb")
        sizePolicy1.setHeightForWidth(self.list_group_usb.sizePolicy().hasHeightForWidth())
        self.list_group_usb.setSizePolicy(sizePolicy1)
        self.list_group_usb.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.list_group_usb.setSortingEnabled(True)

        self.verticalLayout_2.addWidget(self.list_group_usb)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, 0)
        self.btn_group_usb_add = QPushButton(self.groupBox1)
        self.btn_group_usb_add.setObjectName(u"btn_group_usb_add")

        self.horizontalLayout.addWidget(self.btn_group_usb_add)

        self.btn_group_usb_remove = QPushButton(self.groupBox1)
        self.btn_group_usb_remove.setObjectName(u"btn_group_usb_remove")

        self.horizontalLayout.addWidget(self.btn_group_usb_remove)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.gridLayout_8.addWidget(self.groupBox1, 1, 0, 1, 1)

        self.gridLayout_15.addWidget(self.frame_21, 0, 0, 1, 1)

        self.tabs_group.addTab(self.tab_group_params, "")
        self.tab_group_access = QWidget()
        self.tab_group_access.setObjectName(u"tab_group_access")
        self.tab_group_access.setEnabled(False)
        self.gridLayout_25 = QGridLayout(self.tab_group_access)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.tabs_group.addTab(self.tab_group_access, "")

        self.gridLayout_14.addWidget(self.tabs_group, 0, 2, 1, 1)

        self.tabs_general.addTab(self.tab_groups, "")
        self.tab_ports = QWidget()
        self.tab_ports.setObjectName(u"tab_ports")
        self.tab_ports.setEnabled(True)
        self.gridLayout_12 = QGridLayout(self.tab_ports)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.groupBox_8 = QGroupBox(self.tab_ports)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_16 = QGridLayout(self.groupBox_8)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.groupBox_12 = QGroupBox(self.groupBox_8)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_17 = QGridLayout(self.groupBox_12)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.btn_usb_permission_add = QPushButton(self.groupBox_12)
        self.btn_usb_permission_add.setObjectName(u"btn_usb_permission_add")

        self.horizontalLayout_2.addWidget(self.btn_usb_permission_add)

        self.btn_usb_permission_remove = QPushButton(self.groupBox_12)
        self.btn_usb_permission_remove.setObjectName(u"btn_usb_permission_remove")

        self.horizontalLayout_2.addWidget(self.btn_usb_permission_remove)

        self.gridLayout_17.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.list_usb_access = QTreeWidget(self.groupBox_12)
        self.list_usb_access.setObjectName(u"list_usb_access")
        self.list_usb_access.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.list_usb_access.setSortingEnabled(True)
        self.list_usb_access.setHeaderHidden(False)
        self.list_usb_access.header().setVisible(True)
        self.list_usb_access.header().setCascadingSectionResizes(False)
        self.list_usb_access.header().setHighlightSections(True)
        self.list_usb_access.header().setProperty(u"showSortIndicator", True)
        self.list_usb_access.header().setStretchLastSection(True)

        self.gridLayout_17.addWidget(self.list_usb_access, 0, 0, 1, 1)

        self.gridLayout_16.addWidget(self.groupBox_12, 1, 0, 1, 1)

        self.btn_usb_save = QPushButton(self.groupBox_8)
        self.btn_usb_save.setObjectName(u"btn_usb_save")

        self.gridLayout_16.addWidget(self.btn_usb_save, 2, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.groupBox_8)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.groupBox_2.setAcceptDrops(False)
        self.groupBox_2.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_6 = QFrame(self.groupBox_2)
        self.frame_6.setObjectName(u"frame_6")
        self.horizontalLayout_11 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_11.addWidget(self.label_5)

        self.combo_usb_group = QComboBox(self.frame_6)
        self.combo_usb_group.setObjectName(u"combo_usb_group")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.combo_usb_group.sizePolicy().hasHeightForWidth())
        self.combo_usb_group.setSizePolicy(sizePolicy4)

        self.horizontalLayout_11.addWidget(self.combo_usb_group)

        self.btn_usb_group_clear = QPushButton(self.frame_6)
        self.btn_usb_group_clear.setObjectName(u"btn_usb_group_clear")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditClear))
        self.btn_usb_group_clear.setIcon(icon5)

        self.horizontalLayout_11.addWidget(self.btn_usb_group_clear)

        self.gridLayout_3.addWidget(self.frame_6, 8, 0, 1, 1)

        self.frame_11 = QFrame(self.groupBox_2)
        self.frame_11.setObjectName(u"frame_11")
        self.horizontalLayout_21 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_21.addWidget(self.label_17)

        self.le_usb_name = QLineEdit(self.frame_11)
        self.le_usb_name.setObjectName(u"le_usb_name")
        sizePolicy4.setHeightForWidth(self.le_usb_name.sizePolicy().hasHeightForWidth())
        self.le_usb_name.setSizePolicy(sizePolicy4)

        self.horizontalLayout_21.addWidget(self.le_usb_name)

        self.gridLayout_3.addWidget(self.frame_11, 2, 0, 1, 1)

        self.frame_9 = QFrame(self.groupBox_2)
        self.frame_9.setObjectName(u"frame_9")
        self.horizontalLayout_18 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_18.addWidget(self.label_13)

        self.le_usb_virtual_port = QLineEdit(self.frame_9)
        self.le_usb_virtual_port.setObjectName(u"le_usb_virtual_port")
        self.le_usb_virtual_port.setEnabled(True)

        self.horizontalLayout_18.addWidget(self.le_usb_virtual_port)

        self.gridLayout_3.addWidget(self.frame_9, 5, 0, 1, 1)

        self.frame_usb_status = QHBoxLayout()
        self.frame_usb_status.setObjectName(u"frame_usb_status")
        self.frame_usb_status.setContentsMargins(-1, 0, -1, -1)
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setMinimumSize(QSize(150, 0))

        self.frame_usb_status.addWidget(self.label_4)

        self.gridLayout_3.addLayout(self.frame_usb_status, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.groupBox_2)
        self.frame_10.setObjectName(u"frame_10")
        self._2 = QHBoxLayout(self.frame_10)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(150, 0))

        self._2.addWidget(self.label_15)

        self.le_usb_bus = QLineEdit(self.frame_10)
        self.le_usb_bus.setObjectName(u"le_usb_bus")
        self.le_usb_bus.setEnabled(True)

        self._2.addWidget(self.le_usb_bus)

        self.gridLayout_3.addWidget(self.frame_10, 6, 0, 1, 1)

        self.frame_15 = QFrame(self.groupBox_2)
        self.frame_15.setObjectName(u"frame_15")
        self._4 = QHBoxLayout(self.frame_15)
        self._4.setObjectName(u"_4")
        self._4.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_15)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(150, 0))

        self._4.addWidget(self.label_19)

        self.lb_usb_device = QLabel(self.frame_15)
        self.lb_usb_device.setObjectName(u"lb_usb_device")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lb_usb_device.sizePolicy().hasHeightForWidth())
        self.lb_usb_device.setSizePolicy(sizePolicy5)

        self._4.addWidget(self.lb_usb_device)

        self.gridLayout_3.addWidget(self.frame_15, 1, 0, 1, 1)

        self.gridLayout_16.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.gridLayout_12.addWidget(self.groupBox_8, 0, 1, 1, 1)

        self.usb_ports_list_layout = QGroupBox(self.tab_ports)
        self.usb_ports_list_layout.setObjectName(u"usb_ports_list_layout")
        self.usb_ports_list_layout.setMaximumSize(QSize(350, 16777215))
        self.gridLayout = QGridLayout(self.usb_ports_list_layout)
        self.gridLayout.setObjectName(u"gridLayout")
        self.list_usb = QTreeWidget(self.usb_ports_list_layout)
        self.list_usb.setObjectName(u"list_usb")
        self.list_usb.setSortingEnabled(True)

        self.gridLayout.addWidget(self.list_usb, 1, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.le_usb_list_search = QLineEdit(self.usb_ports_list_layout)
        self.le_usb_list_search.setObjectName(u"le_usb_list_search")

        self.horizontalLayout_16.addWidget(self.le_usb_list_search)

        self.gridLayout.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.usb_ports_list_layout)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_usb_add = QPushButton(self.groupBox_4)
        self.btn_usb_add.setObjectName(u"btn_usb_add")
        self.btn_usb_add.setEnabled(False)

        self.verticalLayout_7.addWidget(self.btn_usb_add)

        self.btn_usb_remove = QPushButton(self.groupBox_4)
        self.btn_usb_remove.setObjectName(u"btn_usb_remove")
        self.btn_usb_remove.setEnabled(False)

        self.verticalLayout_7.addWidget(self.btn_usb_remove)

        self.line_2 = QFrame(self.groupBox_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        self.btn_usb_start = QPushButton(self.groupBox_4)
        self.btn_usb_start.setObjectName(u"btn_usb_start")

        self.verticalLayout_7.addWidget(self.btn_usb_start)

        self.btn_usb_stop = QPushButton(self.groupBox_4)
        self.btn_usb_stop.setObjectName(u"btn_usb_stop")

        self.verticalLayout_7.addWidget(self.btn_usb_stop)

        self.btn_usb_restart = QPushButton(self.groupBox_4)
        self.btn_usb_restart.setObjectName(u"btn_usb_restart")

        self.verticalLayout_7.addWidget(self.btn_usb_restart)

        self.gridLayout.addWidget(self.groupBox_4, 2, 0, 1, 1)

        self.gridLayout_12.addWidget(self.usb_ports_list_layout, 0, 0, 1, 1)

        self.tabs_general.addTab(self.tab_ports, "")
        self.tab_logs = QWidget()
        self.tab_logs.setObjectName(u"tab_logs")
        self.tab_logs.setEnabled(True)
        self.tabs_general.addTab(self.tab_logs, "")

        self.gridLayout_11.addWidget(self.tabs_general, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1126, 22))
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
        self.tabs_group.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"hubM Admin Panel", None))
        # if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.action_6.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435",
                                                         None))
        self.action.setText(QCoreApplication.translate("MainWindow",
                                                       u"\u041f\u0435\u0440\u0435\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0441\u0435\u0440\u0432\u0435\u0440",
                                                       None))
        self.btn_check_update.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435",
                                                                 None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043a\u0435\u043d", None))
        self.btn_check_user_access_group.setText(
            QCoreApplication.translate("MainWindow", u"\u043a \u0433\u0440\u0443\u043f\u043f\u0435", None))
        self.btn_check_user_access_port.setText(
            QCoreApplication.translate("MainWindow", u"\u043a \u043f\u043e\u0440\u0442\u0443", None))
        self.btn_about_program.setText(
            QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435",
                                       None))
        self.btn_reboot_server.setText(QCoreApplication.translate("MainWindow",
                                                                  u"\u041f\u0435\u0440\u0435\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0441\u0435\u0440\u0432\u0435\u0440",
                                                                  None))
        self.btn_backup_new.setText(
            QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u043a\u043e\u043f\u0438\u044f",
                                       None))
        self.btn_backup_restore.setText(QCoreApplication.translate("MainWindow",
                                                                   u"\u0412\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c",
                                                                   None))
        self.action_3.setText(
            QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.groupBox_15.setTitle("")
        self.DevButton2.setText(QCoreApplication.translate("MainWindow", u"DevButton2", None))
        self.DevButton1.setText(QCoreApplication.translate("MainWindow", u"DevButton1", None))
        self.groupBox_14.setTitle("")
        self.tabs_general.setTabText(self.tabs_general.indexOf(self.tab_dashboard),
                                     QCoreApplication.translate("MainWindow",
                                                                u"\u0414\u0435\u0448\u0431\u043e\u0440\u0434", None))
        self.users_list_layout.setTitle(QCoreApplication.translate("MainWindow",
                                                                   u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438",
                                                                   None))
        self.le_search_user.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        ___qtreewidgetitem = self.list_users.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow",
                                                                 u"\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u043e\u0435 \u0438\u043c\u044f",
                                                                 None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow",
                                                                 u"\u041f\u043e\u043b\u043d\u043e\u0435 \u0438\u043c\u044f",
                                                                 None));
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow",
                                                             u"\u0412\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435",
                                                             None))
        self.btn_user_create.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u041d\u043e\u0432\u044b\u0439 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c",
                                                                None))
        self.btn_user_delete.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f",
                                                                None))
        self.btn_user_export.setText(
            QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.users_fullname_label.setText(
            QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u043e\u0435 \u0438\u043c\u044f", None))
        self.le_user_cn.setText("")
        self.le_user_cn.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                      u"\u0418\u0432\u0430\u043d\u043e\u0432 \u0418\u0432\u0430\u043d \u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447",
                                                                      None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u043e\u0435 \u0438\u043c\u044f",
                                                        None))
        self.le_user_name.setText("")
        self.le_user_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ii.ivanov", None))
        self.label_11.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 IP", None))
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
        self.le_user_email.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"ii.ivanov@unistroyrf.ru", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439",
                                                         None))
        self.le_user_comment.setText("")
        self.le_user_comment.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                           u"\u042d\u043d\u0435\u0440\u0433\u043e\u0440\u0435\u0441\u0443\u0440\u0441, \u044e\u0440\u0438\u0441\u0442",
                                                                           None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Telegram id", None))
        self.le_user_tg_id.setText("")
        self.le_user_tg_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"912561677", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Telegram code", None))
        self.le_user_tg_code.setText("")
        self.le_user_tg_code.setPlaceholderText(QCoreApplication.translate("MainWindow", u"!hahg@21ga", None))
        self.btn_show_tg_code.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.cb_user_active.setText(
            QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432\u0435\u043d", None))
        self.btn_user_save_params.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow",
                                                            u"\u041f\u043e\u043b\u0438\u0442\u0438\u043a\u0438 \u0433\u0440\u0443\u043f\u043f",
                                                            None))
        self.btn_user_policies_create.setText(QCoreApplication.translate("MainWindow",
                                                                         u"\u041d\u043e\u0432\u0430\u044f \u043f\u043e\u043b\u0438\u0442\u0438\u043a\u0430",
                                                                         None))
        self.btn_user_policies_delete.setText(QCoreApplication.translate("MainWindow",
                                                                         u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u043b\u0438\u0442\u0438\u043a\u0443",
                                                                         None))
        self.btn_change_view_user_policies.setText("")
        self.btn_show_user_policies.setText("")
        self.btn_user_policies_save.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        ___qtablewidgetitem = self.tbl_user_policies.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0441\u0442\u0443\u043f", None));
        ___qtablewidgetitem1 = self.tbl_user_policies.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", u"IP-\u0430\u0434\u0440\u0435\u0441\u0430", None));
        ___qtablewidgetitem2 = self.tbl_user_policies.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", u"USB-\u0444\u0438\u043b\u044c\u0442\u0440", None));
        ___qtablewidgetitem3 = self.tbl_user_policies.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Auth-Method", None));
        ___qtablewidgetitem4 = self.tbl_user_policies.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", u"OTP-\u0441\u0435\u043a\u0440\u0435\u0442", None));
        ___qtablewidgetitem5 = self.tbl_user_policies.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None));
        ___qtablewidgetitem6 = self.tbl_user_policies.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Permit-Login", None));
        ___qtablewidgetitem7 = self.tbl_user_policies.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Can kick", None));
        ___qtablewidgetitem8 = self.tbl_user_policies.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Kickable", None));
        ___qtablewidgetitem9 = self.tbl_user_policies.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Until", None));
        ___qtreewidgetitem1 = self.tree_user_policies.headerItem()
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow",
                                                                  u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435",
                                                                  None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow",
                                                                  u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435",
                                                                  None));
        self.tabs_users.setTabText(self.tabs_users.indexOf(self.users_tab_info),
                                   QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0435\u0435", None))
        self.groupBox_3.setTitle("")
        self.btn_user_ports_save.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tabs_users.setTabText(self.tabs_users.indexOf(self.users_tab_usb_policices),
                                   QCoreApplication.translate("MainWindow",
                                                              u"\u041f\u043e\u043b\u0438\u0442\u0438\u043a\u0438 USB-\u043f\u043e\u0440\u0442\u043e\u0432",
                                                              None))
        self.tabs_users.setTabText(self.tabs_users.indexOf(self.tab), QCoreApplication.translate("MainWindow",
                                                                                                 u"\u0410\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c",
                                                                                                 None))
        self.tabs_general.setTabText(self.tabs_general.indexOf(self.tab_users), QCoreApplication.translate("MainWindow",
                                                                                                           u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438",
                                                                                                           None))
        self.groups_list_layout.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u044b", None))
        self.le_search_group.setText("")
        self.le_search_group.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        ___qtreewidgetitem2 = self.list_groups.headerItem()
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"TCP-\u043f\u043e\u0440\u0442", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow",
                                                                  u"\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u043e\u0435 \u0438\u043c\u044f",
                                                                  None));
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow",
                                                             u"\u0412\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435",
                                                             None))
        self.btn_group_new.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u041d\u043e\u0432\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430",
                                                              None))
        self.btn_group_delete.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443",
                                                                 None))
        self.btn_group_export.setText(
            QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.btn_group_start.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443",
                                                                None))
        # if QT_CONFIG(shortcut)
        self.btn_group_start.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_group_stop.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u0412\u044b\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443",
                                                               None))
        # if QT_CONFIG(shortcut)
        self.btn_group_stop.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_group_restart.setText(QCoreApplication.translate("MainWindow",
                                                                  u"\u041f\u0435\u0440\u0435\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443",
                                                                  None))
        # if QT_CONFIG(shortcut)
        self.btn_group_restart.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_group_save.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.groupBox_24.setTitle(
            QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.le_group_name.setText("")
        self.le_group_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Group Name", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"TCP \u043f\u043e\u0440\u0442", None))
        self.le_group_port.setText("")
        self.le_group_port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"7501", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"IP/Hostname", None))
        self.le_group_ip.setText("")
        self.le_group_ip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"10.10.8.161", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.le_group_login.setText("")
        self.le_group_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.le_group_password.setText("")
        self.le_group_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.groupBox1.setTitle(QCoreApplication.translate("MainWindow", u"USB-\u043f\u043e\u0440\u0442\u044b", None))
        ___qtreewidgetitem3 = self.list_group_usb.headerItem()
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"VID", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None));
        self.btn_group_usb_add.setText(QCoreApplication.translate("MainWindow",
                                                                  u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0440\u0442\u044b",
                                                                  None))
        self.btn_group_usb_remove.setText(QCoreApplication.translate("MainWindow",
                                                                     u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u0440\u0442\u044b",
                                                                     None))
        self.tabs_group.setTabText(self.tabs_group.indexOf(self.tab_group_params),
                                   QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0435\u0435", None))
        self.tabs_group.setTabText(self.tabs_group.indexOf(self.tab_group_access),
                                   QCoreApplication.translate("MainWindow",
                                                              u"\u0414\u043e\u0441\u0442\u0443\u043f\u044b", None))
        self.tabs_general.setTabText(self.tabs_general.indexOf(self.tab_groups),
                                     QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u044b",
                                                                None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0435\u0435", None))
        self.groupBox_12.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0441\u0442\u0443\u043f\u044b", None))
        self.btn_usb_permission_add.setText(QCoreApplication.translate("MainWindow",
                                                                       u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u043e\u0441\u0442\u0443\u043f\u044b",
                                                                       None))
        self.btn_usb_permission_remove.setText(QCoreApplication.translate("MainWindow",
                                                                          u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0434\u043e\u0441\u0442\u0443\u043f\u044b",
                                                                          None))
        ___qtreewidgetitem4 = self.list_usb_access.headerItem()
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow",
                                                                  u"\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u043e\u0435 \u0438\u043c\u044f",
                                                                  None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow",
                                                                  u"\u041f\u043e\u043b\u043d\u043e\u0435 \u0438\u043c\u044f",
                                                                  None));
        self.btn_usb_save.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.groupBox_2.setTitle(
            QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u041f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u0438\u0442",
                                                        None))
        self.combo_usb_group.setCurrentText("")
        self.btn_usb_group_clear.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"USB \u0438\u043c\u044f", None))
        self.le_usb_name.setText("")
        self.le_usb_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usb Name", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Virtual Port", None))
        self.le_usb_virtual_port.setText("")
        self.le_usb_virtual_port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1.1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Bus", None))
        self.le_usb_bus.setText("")
        self.le_usb_bus.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1.2.1-2.2.4", None))
        self.label_19.setText(
            QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e",
                                       None))
        self.lb_usb_device.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u041d\u0435\u0442 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438",
                                                              None))
        self.usb_ports_list_layout.setTitle(
            QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u0442\u044b", None))
        ___qtreewidgetitem5 = self.list_usb.headerItem()
        ___qtreewidgetitem5.setText(2, QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430",
                                                                  None));
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("MainWindow", u"VID", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None));
        self.le_usb_list_search.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow",
                                                            u"\u0412\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435",
                                                            None))
        self.btn_usb_add.setText(QCoreApplication.translate("MainWindow",
                                                            u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0440\u0442",
                                                            None))
        self.btn_usb_remove.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u0440\u0442",
                                                               None))
        self.btn_usb_start.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043f\u043e\u0440\u0442",
                                                              None))
        # if QT_CONFIG(shortcut)
        self.btn_usb_start.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_usb_stop.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u0412\u044b\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043f\u043e\u0440\u0442",
                                                             None))
        # if QT_CONFIG(shortcut)
        self.btn_usb_stop.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_usb_restart.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u041f\u0435\u0440\u0435\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043f\u043e\u0440\u0442",
                                                                None))
        # if QT_CONFIG(shortcut)
        self.btn_usb_restart.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
        # endif // QT_CONFIG(shortcut)
        self.tabs_general.setTabText(self.tabs_general.indexOf(self.tab_ports),
                                     QCoreApplication.translate("MainWindow", u"USB-\u043f\u043e\u0440\u0442\u044b",
                                                                None))
        self.tabs_general.setTabText(self.tabs_general.indexOf(self.tab_logs),
                                     QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438", None))
        self.menu_1.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow",
                                                      u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b",
                                                      None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow",
                                                        u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0434\u043e\u0441\u0442\u0443\u043f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f",
                                                        None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow",
                                                        u"\u0420\u0435\u0437\u0435\u0440\u0432\u043d\u043e\u0435 \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435",
                                                        None))
    # retranslateUi
