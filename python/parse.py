import can
can.rc['interface'] = 'socketcan'
can.rc['channel'] = 'vcan0'
can.rc['bitrate'] = 500000
from can.interfaces.interface import Bus
from can import Message
bus = Bus()

"""

"""
def fSwitch(arg):
	switcher = {
		0x620:
		0x621:
		0x622:
		0x623:
		0x624:
	}

"""
Take recieved CANFrame and parse according to Diagram in Trello
Data outputted in milivolts
"""
def parseFrame(m):

