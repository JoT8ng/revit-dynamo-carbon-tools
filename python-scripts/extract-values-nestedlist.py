# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Store List of EPD Products as Array
data = IN[0]

# Create list to store product name
prodNames = []

try:
# Loop through lists in array and extract product name
	for list in data:
		for item in list:
			prodNames.append(str(item[1]))
			OUT = prodNames
	
except Exception as e:
	OUT = "An error occured: {}".format(e)
	# Print error on console
	print("Error: {}".format(e))