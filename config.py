# for file mangement and exiting
import os
import sys

# Qt imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton

# misc
from math import floor

'''
This is the class used for the setting and the corresponding QWidget.
You shouldn't have to edit this class.

Arguments:
	'settingName' is the name of the setting as it appears in the menu
	'settingType' is "check" for a checkbox, "line" for text entry,
		or "dropdown" for a dropdown box.
 
Optional arguments:
	'tooltip' lets you set the text you see when you hover over the setting
	'dropdownOptions' is a list containing options for the dropdown box
'''
class ConfigSetting(QWidget):
	def __init__(self, settingName, settingType, **kwargs):
		super().__init__()

		self.settingType = settingType

		mainLayout = QHBoxLayout()
		self.setLayout(mainLayout)

		mainLayout.addWidget(QLabel(settingName))

		if settingType == "check":
			self.settingInput = QCheckBox()
			self.settingInput.setChecked(True)
		elif settingType == "line":
			self.settingInput = QLineEdit()
		elif settingType == "dropdown":
			self.settingInput = QComboBox()
			if kwargs.get("dropdownOptions", None):
				for i in kwargs["dropdownOptions"]:
					self.settingInput.addItem(i)
			else:
				print("No options were provided for setting \'" + settingName + "\'")

		mainLayout.addWidget(self.settingInput)

		if kwargs.get("tooltip", None):
			self.setToolTip(kwargs["tooltip"])

	def setSetting(self, setting):
		if self.settingType == "check":
			if setting == "1":
				self.settingInput.setChecked(True)
			elif setting == "0":
				self.settingInput.setChecked(False)
		elif self.settingType == "line":
			self.settingInput.setText(setting)
		elif self.settingType == "dropdown":
			self.settingInput.setCurrentIndex(self.settingInput.findText(setting))

	def getSetting(self):
		if self.settingType == "check":
			if self.settingInput.isChecked():
				return "1"
			else:
				return "0"
		elif self.settingType == "line":
			return self.settingInput.text()
		elif self.settingType == "dropdown":
			return self.settingInput.currentText()

# This is the class for the configuration window
class ConfigWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		# Sets the title
		self.setWindowTitle("smlinux Configuration")
		mainLayout = QVBoxLayout()
		container = QWidget()
		container.setLayout(mainLayout)
		self.setCentralWidget(container)

		actualSettingsLayout = QGridLayout()
		actualSettingsContainer = QWidget()
		actualSettingsContainer.setLayout(actualSettingsLayout)
		mainLayout.addWidget(actualSettingsContainer)

		# This is the dictionary holding the objects for the different settings.
		# The values are the objects while the keys are the setting names
		# as seen in the config file. This is what you edit to add more settings.
		# Check the comment for "ConfigSetting()" to see the arguments.
		self.configDict = {
			"PRESET": ConfigSetting("Preset: ", "dropdown", dropdownOptions = ["sm64ex",
																			"sm64nx",
																			"sm64ex-coop",
																			"render96ex",
																			"cheaterex",
																			"sm64dos",
																			"sm64-portweb",
																			"sm64exweb",
																			"sm64-port-android-base",
																			"androidex",
																			"sm64pc",
																			"sm64-port",
																			"r96proto",
																			"r96alpha"]),
			"InstallHD": ConfigSetting("Install HD: ", "check"),
			"InstallR96": ConfigSetting("Install Render 96 :", "check"),
			"FPS60": ConfigSetting("60 Frames per Second: ", "check"),
			"DYNOS": ConfigSetting("DynOS: ", "check", tooltip = "Option for sm64ex and its forks"),
			"CHEATER": ConfigSetting("Cheats: ", "check", tooltip = "Option for sm64ex and its forks"),
			"BETTERCAMERA": ConfigSetting("Better Camera: ", "check", tooltip = "Option for sm64ex and its forks"),
			"NODRAWINGDISTANCE": ConfigSetting("Disable Drawing Distance: ", "check", tooltip = "Option for sm64ex and its forks"),
			"TEXTURE_FIX": ConfigSetting("Texture Fix: ", "check", tooltip = "Option for sm64ex and its forks"),
			"EXTERNAL_DATA": ConfigSetting("External Data: ", "check", tooltip = "Option for sm64ex and its forks"),
			"DISCORDRPC": ConfigSetting("Discord Rich Presence: ", "check", tooltip = "Option for sm64ex and its forks"),
			"RENDER_API": ConfigSetting("Rendering API: ", "dropdown", tooltip = "Supports GL (2.1+) or GL_LEGACY (1.1+)", dropdownOptions = ["GL",
																																		"GL_LEGACY"]),
			"WINDOW_API": ConfigSetting("Window API: ", "dropdown", tooltip = "Supports SDL2 or SDL1 (1.2)", dropdownOptions = ["SDL2",
																																"SDL1"]),
			"TEXTSAVES": ConfigSetting("Text Saves: ", "check"),
			"DISCORD_SDK": ConfigSetting("Discord SDK: ", "check", tooltip = "Option for sm64ex-coop only"),
			"IMMEDIATELOAD": ConfigSetting("Immediate Load: ", "check", tooltip = "Option for sm64ex-coop only"),
			"LEGACY_RES": ConfigSetting("Legacy Resolution: ", "check", tooltip = "Option for render96ex only"),
			"TOUCH_CONTROLS": ConfigSetting("Touch Controls: ", "check", tooltip = "Option for Android only"),
			"ARMONLY": ConfigSetting("ARM Only: ", "check", tooltip = "Option for Android only"),
			"ENABLE_OPENGL_LEGACY": ConfigSetting("Enable OpenGL Legacy: ", "check", tooltip = "Option for DOS only"),
			"DOS_GL": ConfigSetting("DOS GL: ", "dropdown", tooltip = "Supports dmesa (glide) or osmesa", dropdownOptions = ["dmesa",
																															"osmesa"]),
			"MAXJOBS": ConfigSetting("Compilation Thread Limit: ", "line", tooltip = "Set to limit cpu threads used during compile"),
			"CONFIG": ConfigSetting("Prompt to Configure Before Building: ", "check", tooltip = "Uncheck if you do not want to be automatically prompted before building"),
			"BASEPATH": ConfigSetting("Base Folder: ", "line", tooltip = "Base folder must exist and is where folders for each repo will be placed"),
			"UpdateHD": ConfigSetting("Update HD: ", "check", tooltip = "Uncheck to prevent smlinux updating addons when rebuilding"),
			"BuildMusic": ConfigSetting("Build Music: ", "check", tooltip = "Uncheck to prevent smlinux playing background music during compile"),
			"VERSION": ConfigSetting("Version: ", "dropdown", tooltip = "Advanced Make Flag", dropdownOptions = ["us",
																												"jp",
																												"eu"]),
			"DEBUG": ConfigSetting("Debug: ", "check", tooltip = "Advanced Make Flag"),
			"TARGET_WEB": ConfigSetting("Target Web: ", "check", tooltip = "Advanced Make Flag"),
			"TARGET_RPI": ConfigSetting("Target RPI: ", "check", tooltip = "Advanced Make Flag"),
			"GIT": ConfigSetting("Git Repository: ", "line", tooltip = "GIT and BRANCH are ignored if PRESET is known"),
			"BRANCH": ConfigSetting("Branch: ", "line", tooltip = "GIT and BRANCH are ignored if PRESET is known"),
			"Linux": ConfigSetting("Dependencies: ", "line", tooltip = "Must be set to command appropriate to your distribution. See FAQ."),
			"AutoUpdate": ConfigSetting("Auto Update: ", "check", tooltip = "Uncheck to prevent smlinux updating itself")
		}

		# Change this variable to adjust the layout of the options.
		itemsPerColumn = 17

		# This loops through the dictionary and adds all the settings to the menu.
		# This may be out of order depending on your version of Python 3.
		for i in self.configDict:
			actualSettingsLayout.addWidget(self.configDict[i], list(self.configDict.keys()).index(i) % itemsPerColumn, floor(list(self.configDict.keys()).index(i) / itemsPerColumn))
			if not list(self.configDict.keys()).index(i) % itemsPerColumn:
				actualSettingsLayout.setColumnStretch(floor(list(self.configDict.keys()).index(i) / itemsPerColumn), 1)

		# Read in the config file
		configFile = open(sys.argv[1], "r")
		configFileLines = configFile.readlines()
		for i in configFileLines:
			if i[0] == '#':
				continue
			self.configDict[i.split("=")[0]].setSetting(i.split("=")[1].strip("\n"))
		configFile.close()

		# Now we add the cancel and save buttons
		saveAndCancelContainer = QWidget()
		saveAndCancelLayout = QHBoxLayout()
		saveAndCancelContainer.setLayout(saveAndCancelLayout)

		saveButton = QPushButton()
		saveButton.setText("Save")
		saveButton.clicked.connect(self.saveAndExit)
		saveAndCancelLayout.addWidget(saveButton)
		
		cancelButton = QPushButton()
		cancelButton.setText("Cancel")
		cancelButton.clicked.connect(self.close)
		saveAndCancelLayout.addWidget(cancelButton)
		
		mainLayout.addWidget(saveAndCancelContainer)

	def saveAndExit(self):
		configFile = open(sys.argv[1], "r")
		configFileStrOld = configFile.read()
		configFile.close()

		configFileStrNew = ""
		for i in configFileStrOld.splitlines():
			if i[0] == '#':
				configFileStrNew += i + '\n'
				continue
			configFileStrNew += i.split("=")[0] + '='
			configFileStrNew += self.configDict[i.split("=")[0]].getSetting() + '\n'
		
		configFile = open(sys.argv[1], "w")
		configFile.write(configFileStrNew)
		configFile.close()

		self.close()


# This is the entrypoint for the program
def main():
	# Before we do anything, let's check to see if the config file exists
	if not os.path.exists(sys.argv[1]):
		print("ERROR: configuration \'" + sys.argv[1] + "\' does not exist.")
		sys.exit(1)

	# We declare the app
	configApp = QApplication(sys.argv)

	# We declare the window
	configWindow = ConfigWindow()

	# We show the window
	configWindow.show()

	# We trigger the event loop for the app inside of "sys.exit()" to prevents leaks
	sys.exit(configApp.exec_())

if __name__ == '__main__':
	main()
