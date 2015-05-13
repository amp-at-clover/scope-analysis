import telnetlib
import math

from matplotlib import pyplot as plt
'''
@author: Arvind Pereira
@date:   May 13, 2015
'''

from scope_settings import ScopeSettings
from scope_ascii_waveform import AsciiWaveform

class TektronixScope:
	''' This class creates a telnet connection with a  Tektronix scope via ethernet, 
	    and allows us to perform some rudimentary communication with it.
		
		Arguments are:
		   HOST= IP address of the scope (Set it in the IO settings via Utility)
		   PORT= Port on which the socket server will be open. (Choose Terminal as protocol.)
	'''
	def __init__(self, HOST="192.168.0.11", PORT="3998"):
		self.scope = None
		try:
			self.scope = telnetlib.Telnet(HOST, PORT)
			self.host = HOST
			self.port = PORT
		except:
			print 'Error opening the port'
		else:
			print 'Opened connection: %s %s'%(HOST, PORT)
			print self.scope.read_until('milliseconds\r\n>')

	def getIDN(self):
		self.id = self.writeCommand('*IDN?\r\n')
		return self.id
		
	def getSettings(self):
		self.settings = self.writeCommand('SET?\r\n')
		self.ss = ScopeSettings( self.settings )
		return self.ss

	def setLabelForChannel(self, channel, label):
		if channel>=1 and channel<=4:
			cmdToWrite = 'CH%d:LABel "%s"\r\n'%(channel,label)
			self.writeCommand( cmdToWrite )

	def setPositionForChannel(self, channel, position):
		if channel>=1 and channel<=4:
			if math.fabs(position)<=1e-6:
				cmdToWrite = ':CH%d:POSITION 0.0E+0\r\n'%(channel)
			else:
				cmdToWrite = ':CH%d:POSITION %.1fE+%d\r\n'%(channel,position/10.0,int(math.log10(position/10)))
			self.writeCommand( cmdToWrite )

	def setScaleForChannel(self, channel, scale):
		if channel>=1 and channel<=4:
			cmdToWrite = 'CH%d:SCAle %.3f\r\n'%(channel, scale)
			self.writeCommand( cmdToWrite )

	def getScaleForChannel(self, channel, scale):
		if channel>=1 and channel<=4:
			cmdToWrite = 'CH%d:SCAle?\r\n'%(channel)
			scaleResp = self.writeCommand( cmdToWrite )
			return scaleResp

	def transferWaveformForChannel(self,channel):
		if channel>=1 and channel<=4:
			cmdToWrite = 'DATa:SOUrce CH%d\r\n'%(channel)
			self.writeCommand(cmdToWrite)
			self.writeCommand('DATa:ENCdg ASCII\r\n')
			self.writeCommand('DATa:BYT_NR 1\r\n')
			waveformData=self.writeCommand('WAVFrm?\r\n')
			awf = AsciiWaveform( waveformData )
			return awf


	def writeCommand( self, cmd ):
		''' TODO: Add some checks here to ensure this command is valid.
		'''
		if self.scope != None:
			print 'Writing out:',cmd
			self.scope.write(cmd)
			resp = self.scope.read_until('>')
			return resp
		return None


	def closeConnection(self):
		if self.scope != None:
			self.scope.close()
			self.scope = None


ts = TektronixScope('192.168.0.11','3998')
print ts.getIDN()
scope_settings=ts.getSettings().settings_dict
ts.setLabelForChannel(1,'Test')
waveform = ts.transferWaveformForChannel(1)
plt.plot( waveform.waveform )
plt.show()

#ts.closeConnection()
