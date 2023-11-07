# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Get inputs
prodNames = IN[0]
nameIndex = int(IN[1])

# Declare string variable for selected product name
selectName = ""

try:
	for item in prodNames:
		selectName = str(item[nameIndex])
		OUT = selectName

except Exception as e:
	OUT = "An error occured: {}".format(e)
	# Print error on console
	print("Error: {}".format(e))
