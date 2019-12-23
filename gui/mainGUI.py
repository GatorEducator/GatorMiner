from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Setup main window
        MainWindow.resize(794, 592)
        MainWindow.setWindowTitle("Ethical Toolbox")

        self.addMenuBar(MainWindow)
        #Set up the central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.addTabWidget()
        #New horizontal layout
        self.hLayout1 = QtWidgets.QHBoxLayout(self.centralwidget)

        #self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_3)
        # self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # # self.graph = QtWidgets.QWidget(self.tab_3)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.graph.sizePolicy().hasHeightForWidth())
        # # self.graph.setSizePolicy(sizePolicy)
        # # self.graph.setMinimumSize(QtCore.QSize(200, 100))
        # # self.graph.setObjectName("graph")
        # self.horizontalLayout_3.addWidget(self.graph)
        # self.line = QtWidgets.QFrame(self.tab_3)
        # self.line.setFrameShape(QtWidgets.QFrame.VLine)
        # self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line.setObjectName("line")
        # self.horizontalLayout_3.addWidget(self.line)
        # self.verticalLayout = QtWidgets.QVBoxLayout()
        # self.verticalLayout.setSpacing(1)
        # self.verticalLayout.setObjectName("verticalLayout")
        # self.checkBox = QtWidgets.QCheckBox(self.tab_3)
        # self.checkBox.setObjectName("checkBox")
        # self.verticalLayout.addWidget(self.checkBox, 0, QtCore.Qt.AlignTop)
        # self.checkBox_4 = QtWidgets.QCheckBox(self.tab_3)
        # self.checkBox_4.setObjectName("checkBox_4")
        # self.verticalLayout.addWidget(self.checkBox_4, 0, QtCore.Qt.AlignTop)
        # self.checkBox_3 = QtWidgets.QCheckBox(self.tab_3)
        # self.checkBox_3.setObjectName("checkBox_3")
        # self.verticalLayout.addWidget(self.checkBox_3, 0, QtCore.Qt.AlignTop)
        # self.checkBox_2 = QtWidgets.QCheckBox(self.tab_3)
        # self.checkBox_2.setObjectName("checkBox_2")
        # self.verticalLayout.addWidget(self.checkBox_2, 0, QtCore.Qt.AlignTop)
        # self.horizontalSlider = QtWidgets.QSlider(self.tab_3)
        # self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        # self.horizontalSlider.setObjectName("horizontalSlider")
        # self.verticalLayout.addWidget(self.horizontalSlider, 0, QtCore.Qt.AlignHCenter)
        # spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.verticalLayout.addItem(spacerItem)
        # self.horizontalLayout_3.addLayout(self.verticalLayout)
        # self.tabWidget.addTab(self.tab_3, "")
        # self.tab_4 = QtWidgets.QWidget()
        # self.tab_4.setObjectName("tab_4")
        # self.tabWidget.addTab(self.tab_4, "")
        self.hLayout1.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)


        #self.retranslateUi(MainWindow)
        # self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showNewTabDialog(self):
        self.window = QtWidgets.QDialog() #Create the window
        self.ui = Ui_NewTab() #Create the UI
        self.ui.setupUi(self.window) #Apply the UI to the window
        self.window.show() #Show the window
        title = self.ui.getInput(self.window)
        if title != None:
            self.addTabtoWidget(title)

    def showAboutDialog(self):
        self.window = QtWidgets.QDialog() #Create the window
        self.ui = Ui_About() #Create the UI
        self.ui.setupUi(self.window) #Apply the UI to the window
        self.window.show() #Show the window

    def addTabWidget(self):
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)

    def addTabtoWidget(self, title):
        tab = QtWidgets.QWidget()
        self.tabWidget.addTab(tab, title)

    def addMenuBar(self, MainWindow):
        #Create Menubar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 22))

        #Create the "File" menu
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setTitle(" &File") #Set the name of the menu
        self.actionNewTab = QtWidgets.QAction(MainWindow) #Create the newtab action
        self.actionNewTab.setText(" &New Tab") #Set the name of the action
        self.actionNewTab.triggered.connect(self.showNewTabDialog)
        self.menuFile.addAction(self.actionNewTab) #Add our newtab action to the menu

        #Create the "Help" menu
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setTitle(" &Help") #Set the name of the menu
        self.actionAbout = QtWidgets.QAction(MainWindow) #Create the about action
        self.actionAbout.setText(" &About") #Set the name of the action
        self.actionAbout.triggered.connect(self.showAboutDialog)
        self.menuHelp.addAction(self.actionAbout) #Add the about action to the menu

        #Add File and Help menus to the menubar
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        #Set the window menubar to ours
        MainWindow.setMenuBar(self.menubar)

        #Set up the status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        #Set the status bar to ours
        MainWindow.setStatusBar(self.statusbar)

class Ui_NewTab(object):
    def getInput(self, window):
        if window.exec_() == QDialog.Accepted:
            return self.comboBox.currentText()
        else:
            print("Return NONE")
            return None

    def setupUi(self, NewTab):
        NewTab.resize(400, 85)
        self.vLayout = QtWidgets.QVBoxLayout(NewTab)
        self.comboBox = QtWidgets.QComboBox(NewTab)
        self.comboBox.addItem("Graph")
        self.comboBox.addItem("Other Graph")
        self.vLayout.addWidget(self.comboBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewTab)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vLayout.addWidget(self.buttonBox, 0, QtCore.Qt.AlignBottom)

        self.retranslateUi(NewTab)
        self.buttonBox.accepted.connect(NewTab.accept)
        self.buttonBox.rejected.connect(NewTab.reject)
        QtCore.QMetaObject.connectSlotsByName(NewTab)

    def retranslateUi(self, NewTab):
        _translate = QtCore.QCoreApplication.translate
        NewTab.setWindowTitle(_translate("NewTab", "Create New Tab"))

    # def retranslateUi(self, MainWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     MainWindow.setWindowTitle(_translate("MainWindow", "Ethical Toolbox"))
    #     self.checkBox.setText(_translate("MainWindow", "Option1"))
    #     self.checkBox_4.setText(_translate("MainWindow", "Option2"))
    #     self.checkBox_3.setText(_translate("MainWindow", "Option3"))
    #     self.checkBox_2.setText(_translate("MainWindow", "Option4"))
    #     self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab 1"))
    #     self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))
    #     self.menuFile.setTitle(_translate("MainWindow", "File"))
    #     self.menuabout.setTitle(_translate("MainWindow", "Help"))
    #     self.actionNew.setText(_translate("MainWindow", "New Tab"))
    #     self.actionAbout.setText(_translate("MainWindow", "About"))

class Ui_About(object):
    def setupUi(self, About):
        About.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(About)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(About)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(About)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(About)
        self.buttonBox.accepted.connect(About.accept)
        self.buttonBox.rejected.connect(About.reject)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))
        self.label.setText(_translate("About", "Ethical Toolbox\n"
"\n"
"Created by:\n"
"Allegheny Mozilla Fellows\n"
"NamesListHere"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) #Create the application
    MainWindow = QtWidgets.QMainWindow() #Create the main window
    ui = Ui_MainWindow() #Create the UI
    ui.setupUi(MainWindow) #Apply the UI to the main window
    MainWindow.show() #Show the window
    sys.exit(app.exec_()) #Cleanly handle exit
