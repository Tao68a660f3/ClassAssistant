# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(466, 478)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_9.addWidget(self.label_14)
        self.areaName = QtWidgets.QLineEdit(Form)
        self.areaName.setObjectName("areaName")
        self.horizontalLayout_9.addWidget(self.areaName)
        self.exitBtn = QtWidgets.QPushButton(Form)
        self.exitBtn.setObjectName("exitBtn")
        self.horizontalLayout_9.addWidget(self.exitBtn)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_8.addWidget(self.label_15)
        self.sayingEdit = QtWidgets.QTextEdit(Form)
        self.sayingEdit.setObjectName("sayingEdit")
        self.verticalLayout_8.addWidget(self.sayingEdit)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_10.addWidget(self.label_16)
        self.noticeOnly = QtWidgets.QCheckBox(Form)
        self.noticeOnly.setObjectName("noticeOnly")
        self.horizontalLayout_10.addWidget(self.noticeOnly)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        self.noticeEdit = QtWidgets.QTextEdit(Form)
        self.noticeEdit.setObjectName("noticeEdit")
        self.verticalLayout_9.addWidget(self.noticeEdit)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_12.addWidget(self.checkBox)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout_12.addWidget(self.dateTimeEdit)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.eatalarm = QtWidgets.QCheckBox(Form)
        self.eatalarm.setObjectName("eatalarm")
        self.horizontalLayout_16.addWidget(self.eatalarm)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_17.addWidget(self.label_28)
        self.lunchTime = QtWidgets.QTimeEdit(Form)
        self.lunchTime.setObjectName("lunchTime")
        self.horizontalLayout_17.addWidget(self.lunchTime)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_31 = QtWidgets.QLabel(Form)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_18.addWidget(self.label_31)
        self.dinnerTime = QtWidgets.QTimeEdit(Form)
        self.dinnerTime.setObjectName("dinnerTime")
        self.horizontalLayout_18.addWidget(self.dinnerTime)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_18)
        self.verticalLayout_10.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.OpenPPT = QtWidgets.QPushButton(Form)
        self.OpenPPT.setObjectName("OpenPPT")
        self.horizontalLayout_13.addWidget(self.OpenPPT)
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_13.addWidget(self.label_22)
        self.pptTime = QtWidgets.QTimeEdit(Form)
        self.pptTime.setObjectName("pptTime")
        self.horizontalLayout_13.addWidget(self.pptTime)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_14.addWidget(self.label_25)
        self.shutdownTime = QtWidgets.QTimeEdit(Form)
        self.shutdownTime.setObjectName("shutdownTime")
        self.horizontalLayout_14.addWidget(self.shutdownTime)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_14)
        self.verticalLayout_10.addLayout(self.horizontalLayout_15)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mTopMost = QtWidgets.QPushButton(Form)
        self.mTopMost.setObjectName("mTopMost")
        self.horizontalLayout.addWidget(self.mTopMost)
        self.mColor = QtWidgets.QPushButton(Form)
        self.mColor.setMaximumSize(QtCore.QSize(20, 16))
        self.mColor.setText("")
        self.mColor.setObjectName("mColor")
        self.horizontalLayout.addWidget(self.mColor)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.mSize = QtWidgets.QSpinBox(Form)
        self.mSize.setObjectName("mSize")
        self.horizontalLayout.addWidget(self.mSize)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mLock = QtWidgets.QPushButton(Form)
        self.mLock.setObjectName("mLock")
        self.horizontalLayout_2.addWidget(self.mLock)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.mTransp = QtWidgets.QSlider(Form)
        self.mTransp.setOrientation(QtCore.Qt.Horizontal)
        self.mTransp.setObjectName("mTransp")
        self.horizontalLayout_2.addWidget(self.mTransp)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout_19.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sTopMost = QtWidgets.QPushButton(Form)
        self.sTopMost.setObjectName("sTopMost")
        self.horizontalLayout_3.addWidget(self.sTopMost)
        self.sColor = QtWidgets.QPushButton(Form)
        self.sColor.setMaximumSize(QtCore.QSize(20, 16))
        self.sColor.setText("")
        self.sColor.setObjectName("sColor")
        self.horizontalLayout_3.addWidget(self.sColor)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.sSize = QtWidgets.QSpinBox(Form)
        self.sSize.setObjectName("sSize")
        self.horizontalLayout_3.addWidget(self.sSize)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sLock = QtWidgets.QPushButton(Form)
        self.sLock.setObjectName("sLock")
        self.horizontalLayout_4.addWidget(self.sLock)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.sTransp = QtWidgets.QSlider(Form)
        self.sTransp.setOrientation(QtCore.Qt.Horizontal)
        self.sTransp.setObjectName("sTransp")
        self.horizontalLayout_4.addWidget(self.sTransp)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_19.addLayout(self.verticalLayout_4)
        self.verticalLayout_11.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bTopMost = QtWidgets.QPushButton(Form)
        self.bTopMost.setObjectName("bTopMost")
        self.horizontalLayout_5.addWidget(self.bTopMost)
        self.bColor = QtWidgets.QPushButton(Form)
        self.bColor.setMaximumSize(QtCore.QSize(20, 16))
        self.bColor.setText("")
        self.bColor.setObjectName("bColor")
        self.horizontalLayout_5.addWidget(self.bColor)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.bSize = QtWidgets.QSpinBox(Form)
        self.bSize.setObjectName("bSize")
        self.horizontalLayout_5.addWidget(self.bSize)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bLock = QtWidgets.QPushButton(Form)
        self.bLock.setObjectName("bLock")
        self.horizontalLayout_6.addWidget(self.bLock)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.bTransp = QtWidgets.QSlider(Form)
        self.bTransp.setOrientation(QtCore.Qt.Horizontal)
        self.bTransp.setObjectName("bTransp")
        self.horizontalLayout_6.addWidget(self.bTransp)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout_20.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.cnFont = QtWidgets.QLineEdit(Form)
        self.cnFont.setObjectName("cnFont")
        self.horizontalLayout_7.addWidget(self.cnFont)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.ascFont = QtWidgets.QLineEdit(Form)
        self.ascFont.setObjectName("ascFont")
        self.horizontalLayout_7.addWidget(self.ascFont)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.rate = QtWidgets.QSpinBox(Form)
        self.rate.setObjectName("rate")
        self.horizontalLayout_8.addWidget(self.rate)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.step = QtWidgets.QSpinBox(Form)
        self.step.setObjectName("step")
        self.horizontalLayout_8.addWidget(self.step)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(3, 1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_20.addLayout(self.verticalLayout_7)
        self.verticalLayout_11.addLayout(self.horizontalLayout_20)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_14.setText(_translate("Form", "天气预报地区名称"))
        self.exitBtn.setText(_translate("Form", "保存设置"))
        self.label_15.setText(_translate("Form", "每日一语"))
        self.label_16.setText(_translate("Form", "通知"))
        self.noticeOnly.setText(_translate("Form", "只显示通知"))
        self.checkBox.setText(_translate("Form", "自动日期"))
        self.eatalarm.setText(_translate("Form", "提醒用餐"))
        self.label_28.setText(_translate("Form", "午餐时间"))
        self.label_31.setText(_translate("Form", "晚餐时间"))
        self.OpenPPT.setText(_translate("Form", "打开PPT"))
        self.label_22.setText(_translate("Form", "PPT开启时间"))
        self.label_25.setText(_translate("Form", "询问关机时间"))
        self.label_3.setText(_translate("Form", "消息滚动框"))
        self.mTopMost.setText(_translate("Form", "置顶显示"))
        self.label.setText(_translate("Form", "字体大小"))
        self.mLock.setText(_translate("Form", "锁定"))
        self.label_2.setText(_translate("Form", "透明度"))
        self.label_6.setText(_translate("Form", "时间日期框"))
        self.sTopMost.setText(_translate("Form", "置顶显示"))
        self.label_4.setText(_translate("Form", "字体大小"))
        self.sLock.setText(_translate("Form", "锁定"))
        self.label_5.setText(_translate("Form", "透明度"))
        self.label_7.setText(_translate("Form", "大倒计时框"))
        self.bTopMost.setText(_translate("Form", "置顶显示"))
        self.label_8.setText(_translate("Form", "字体大小"))
        self.bLock.setText(_translate("Form", "锁定"))
        self.label_9.setText(_translate("Form", "透明度"))
        self.label_10.setText(_translate("Form", "CNF"))
        self.label_11.setText(_translate("Form", "ENF"))
        self.label_12.setText(_translate("Form", "RATE"))
        self.label_13.setText(_translate("Form", "STEP"))
