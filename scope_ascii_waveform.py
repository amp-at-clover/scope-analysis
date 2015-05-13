import re
import numpy as np

'''
Example->
:WFMOUTPRE:
BYT_NR 1;
BIT_NR 8;
ENCDG ASCII;
BN_FMT RI;
BYT_OR MSB;
WFID "Ch1, DC coupling, 100.0mV/div, 4.000us/div,10000 points, Sample mode"
NR_PT 20;
PT_FMT Y;
PT_ORDER LINEAR;
XUNIT "s";
XINCR 4.0000E-9;
XZERO -20.0000E-6;
PT_OFF 0;
YUNIT "V";
YMULT 4.0000E-3;
YOFF 0.0000;
YZERO 0.0000;
:CURVE

'''

class AsciiWaveform:

	def __init__(self, waveformString ):
		waveform_list = re.split(';',waveformString)
		self.waveformSettings = {}
		self.waveFormOptions= {
			0:self.BYT_NR, 1:self.BIT_NR, 2:self.ENCDG, 3:self.BN_FMT, 4:self.BYT_OR, 5:self.WFID,
			6:self.NR_PT, 7:self.PT_FMT, 8:self.PT_ORDER, 9:self.XUNIT, 10:self.XINCR, 
			11:self.XZERO, 12:self.PT_OFF, 13:self.YUNIT, 14:self.YMULT, 15:self.YOFF, 16:self.YOFF, 
			17:self.YZERO, 22:self.CURVE
		}
		for idx, val in enumerate(waveform_list):
			try:
				self.waveFormOptions[idx](val)
			except:
				pass

	def BYT_NR(self,value):
		self.waveformSettings['BYTE_NR'] = value

	def BIT_NR(self,value):
		self.waveformSettings['BIT_NR'] = value
	
	def ENCDG(self,value):
		self.waveformSettings['ENCDG'] = value

	def BN_FMT(self,value):
		self.waveformSettings['BN_FMT'] = value

	def BYT_OR(self,value):
		self.waveformSettings['BYT_OR'] = value

	def WFID(self,value):
		self.waveformSettings['WFID'] = value

	def NR_PT(self,value):
		self.waveformSettings['NR_PT'] = value

	def PT_FMT(self,value):
		self.waveformSettings['PT_FMT'] = value

	def PT_ORDER(self,value):
		self.waveformSettings['PT_ORDER'] = value

	def XUNIT(self,value):
		self.waveformSettings['XUNIT'] = value

	def XINCR(self,value):
		self.waveformSettings['XINCR'] = value

	def XZERO(self,value):
		self.waveformSettings['XZERO'] = value

	def PT_OFF(self,value):
		self.waveformSettings['PT_OFF'] = value

	def YUNIT(self,value):
		self.waveformSettings['YUNIT'] = value

	def YMULT(self,value):
		self.waveformSettings['YMULT'] = value

	def YOFF(self,value):
		self.waveformSettings['YOFF'] = value

	def YZERO(self,value):
		self.waveformSettings['YZERO'] = value

	def CURVE(self,value):
		# Make this faster later
		waveform = []
		for val in re.split(',',value):
			try:
				waveform.append(int(val))
			except:
				pass
		self.waveform = np.array(waveform)


	


 
