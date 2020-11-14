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
		self.setWindowTitle("smlinux configuration")
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
			"PRESET": ConfigSetting("Preset", "dropdown", dropdownOptions = ["sm64ex","sm64nx","sm64ex-coop","render96ex","cheaterex","sm64dos","sm64-portweb","sm64exweb","sm64-port-android-base","androidex","sm64pc","sm64-port","r96proto","r96alpha","UserDefined"]),
			"VERSION": ConfigSetting("ROM Version", "dropdown", tooltip = "Must correspond to ROM region", dropdownOptions = ["us","jp","eu"]),
			"RENDER_API": ConfigSetting("RENDER_API", "dropdown", tooltip = "Supports GL (2.1+) or GL_LEGACY (1.1+)", dropdownOptions = ["GL","GL_LEGACY","D3D11"]),
			"WINDOW_API": ConfigSetting("WINDOW_API", "dropdown", tooltip = "Supports SDL2 or SDL1 (1.2)", dropdownOptions = ["SDL2","SDL1"]),
			"MAXJOBS": ConfigSetting("Maximum Jobs", "line", tooltip = "Set to limit cpu threads used during compile"),
			"BASEPATH": ConfigSetting("Base Folder", "line", tooltip = "Base folder must exist and is where folders for each repo will be placed"),
			"InstallHD": ConfigSetting("Install HD", "check", tooltip = "Install Upscale Add-ons described in FAQ"),
			"UpdateHD": ConfigSetting("Update HD", "check", tooltip = "Update HD Add-ons when rebuilding"),
			"InstallR96": ConfigSetting("Install R96 Models", "check", tooltip = "Install Render 96 Model Pack"),
			"FPS60": ConfigSetting("60fps patch", "check", tooltip="Apply 60fps patch if included in repo"),
			"DYNOS": ConfigSetting("DynOS patch", "check", tooltip = "Apply Dynamic Option System by PeachyPeach"),
			"CHEATER": ConfigSetting("CHEATER patch", "check", tooltip = "Apply CHEATER by s4ys"),
			
			"BETTERCAMERA": ConfigSetting("BETTERCAMERA", "check", tooltip = "Build Option for sm64ex and its forks"),
			"NODRAWINGDISTANCE": ConfigSetting("NODRAWINGDISTANCE", "check", tooltip = "Build Option for sm64ex and its forks"),
			"TEXTURE_FIX": ConfigSetting("TEXTURE_FIX", "check", tooltip = "Build Option for sm64ex and its forks"),
			"EXTERNAL_DATA": ConfigSetting("EXTERNAL_DATA", "check", tooltip = "Build Option for sm64ex and its forks"),
			"DISCORDRPC": ConfigSetting("DISCORDRPC", "check", tooltip = "Build Option for sm64ex and its forks"),
			"TEXTSAVES": ConfigSetting("TEXTSAVES", "check", tooltip = "Build Option for sm64ex and its forks"),
			"DEBUG": ConfigSetting("DEBUG", "check", tooltip = "Advanced Build Option"),
			"TARGET_WEB": ConfigSetting("TARGET_WEB", "check", tooltip = "Build Web Version with emsdk"),
			"TARGET_RPI": ConfigSetting("TARGET_RPI", "check", tooltip = "Build Raspberry Pi version"),
			"DISCORD_SDK": ConfigSetting("DISCORD_SDK (Co-op)", "check", tooltip = "Build option for sm64ex-coop only"),
			"IMMEDIATELOAD": ConfigSetting("IMMEDIATELOAD (Co-op)", "check", tooltip = "Build option for sm64ex-coop only"),
			"LEGACY_RES": ConfigSetting("LEGACY_RES (R96)", "check", tooltip = "Built option for render96ex only"),

			"DOS_GL": ConfigSetting("DOS_GL: ", "dropdown", tooltip = "Supports dmesa (glide) or osmesa", dropdownOptions = ["dmesa","osmesa"]),
			"ENABLE_OPENGL_LEGACY": ConfigSetting("ENABLE_OPENGL_LEGACY (DOS)", "check", tooltip = "Option for DOS only"),
			"TOUCH_CONTROLS": ConfigSetting("Android TOUCH_CONTROLS", "check", tooltip = "Build option for Android only"),
			"ARMONLY": ConfigSetting("Android ARM Only", "check", tooltip = "Prevent x86 builds for Android"),
			"BuildMusic": ConfigSetting("Build Music", "check", tooltip = "Play music in the background while compiling"),
			"AutoUpdate": ConfigSetting("Automatic Updates", "check", tooltip = "Update smlinux before build"),
			"CONFIG": ConfigSetting("Prompt to Configure Before Next Build", "check", tooltip = "Prompt to edit configuration file before building"),
			"GIT": ConfigSetting("Git Repository", "line", tooltip = "GIT and BRANCH are ignored if PRESET is known"),
			"BRANCH": ConfigSetting("Branch", "line", tooltip = "GIT and BRANCH are ignored if PRESET is known"),
			"Linux": ConfigSetting("Linux", "line", tooltip = "Must be set to command appropriate to your distribution. See FAQ."),
			
		}

		# Change this variable to adjust the layout of the options.
		itemsPerColumn = 12

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
