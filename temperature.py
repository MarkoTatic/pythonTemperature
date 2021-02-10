
#!/usr/bin/python
#tempmon.py
 
# Graphical User Interface for TCN75A sensor
 
# Imports
import time
import serial
from Tkinter import *
 
# Serial port parameters
serial_speed = 9600
# Your serial port instead of ttyUSB0
serial_port = '/dev/ttyUSB0'
 
ser = serial.Serial(serial_port, serial_speed, timeout=1)
 
# Main Tkinter application
class Application(Frame):
 
    # Measure data from the sensor
    def measure(self):
 
          # Request data and read the answer
          data = ser.readline() # read data from serial
          # port and strip line endings
 
          # If the answer is not empty, process & display data
          if (data != ""):
               processed_data = data.split(',')
               self.tempC_data.set("Temp. in " + unichr(176) + "C: " + str(processed_data[0]))
               self.temperatureC.pack()
 
               self.tempF_data.set("Temp. in " + unichr(176) + "F: " + str(processed_data[1]))
               self.temperatureF.pack()
 
               self.alertT_data.set(str(processed_data[0]))
               self.alertT.pack()
 
          # Wait 1 second between each measurement
          self.after(100,self.measure)
 
    # Create display elements
    def createWidgets(self):
 
              self.temperatureC = Label(self, textvariable=self.tempC_data, font=('Verdana', 24, 'bold'))
              self.tempC_data.set("Temp in C")
              self.temperatureC.pack()
 
              self.temperatureF = Label(self, textvariable=self.tempF_data, font=('Verdana', 24, 'bold'))
              self.tempF_data.set("Temp in F")
              self.temperatureF.pack()
 
              self.alertT = Label(self, textvariable=self.alertT_data, font=('Verdana', 24, 'bold'))
              self.alertT_data.set("")
              self.alertT.pack()
 
     # Init the variables & start measurements
    def __init__(self, master=None):
              Frame.__init__(self, master)
              self.tempC_data = StringVar()
              self.tempF_data = StringVar()
              self.alertT_data = StringVar()
              self.createWidgets()
              self.pack()
              self.measure()
 
# Create and run the GUI
root = Tk()
root.title('Aliatron Office')
app = Application(master=root)
app.mainloop()