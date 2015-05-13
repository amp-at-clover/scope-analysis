import re


'''
	Get the settings of the scope


'''

class ScopeSettings:
	def __init__(self, settingsString ):
		settings_list = re.split(';',settingsString)
		self.settings_dict = {}
		for setting in settings_list:
			k,v = re.split(' ',setting)
			self.settings_dict[k] = v



