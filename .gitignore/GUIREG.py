 # -*- coding: utf-8 -*-     
import wx
import REG

class Regframe(wx.Frame):
	def __init__(self,*args,**kwargs):
		super(Regframe,self).__init__(*args,**kwargs)
		self.SetSize((500,200))
		self.SetPosition((500,400))
		panel = wx.Panel(self)
		self.filepicker = wx.FilePickerCtrl(panel, pos = (30, 30) , size = (100,25))
		self.savepicker = wx.TextCtrl(panel)
		sb = wx.StaticBox(panel, label = '文件路径')
		sbs = wx.StaticBoxSizer(sb,wx.VERTICAL) 
		sbs.Add(wx.StaticText(panel, -1, '请选择文件:'))
		sbs.Add(self.filepicker)
		sbs.Add(wx.StaticText(panel, -1, 'Save As:'))
		sbs.Add(self.savepicker)

		plotbutton = wx.Button(panel, label = '画图')
		plotbutton.Bind(wx.EVT_BUTTON , self.plot)
		
		hsizer=wx.BoxSizer(wx.HORIZONTAL)
		hsizer.Add(sbs)
		hsizer.Add(plotbutton)		
		panel.SetSizer(hsizer)
		
		
	def plot(self,event):
		fileloc = self.filepicker.GetPath()
		if self.savepicker.GetValue() == '':
			saveloc = fileloc + '.HeatMap.PNG'
		else:
			saveloc = self.savepicker.GetValue() + '.PNG'
		REG.RegPlot(fileloc,saveloc)
		
		
		
if __name__=='__main__':
	app = wx.App(False)
	top = Regframe(None)
	top.Show(True)
	app.MainLoop()
		
