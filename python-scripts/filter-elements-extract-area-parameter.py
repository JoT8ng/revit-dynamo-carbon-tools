# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Get inputs
data = IN[0]
param = int(IN[2])
filterIndex = int(IN[1])

# Declare filters
filter1 = IN[3]
filter2 = IN[4]
filter3 = IN[5]

# Create output lists
elements = []
paramValue = []

index = 0

try:
# Loop through lists in array and extract product name
	for list in data:
		index += 1
		for item in list:
			if filter1 in str(item[filterIndex]):
				elements.append(str(item[param]))
			elif filter2 in str(item[filterIndex]):
				elements.append(str(item[param]))
			elif filter3 in str(item[filterIndex]):
				elements.append(str(item[param]))
				
	for item in elements:
		new_string = ''.join((x for x in item if x.isdigit()))
		paramValue.append(str(new_string))		
		OUT = paramValue
	
except Exception as e:
	OUT = "An error occured: {}".format(e)
	# Print error on console
	print("Error: {}".format(e))