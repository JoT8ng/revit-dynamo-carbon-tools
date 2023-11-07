# Load the Python Standard and DesignScript Libraries
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import Transaction

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Set current open family file as variable
doc = DocumentManager.Instance.CurrentDBDocument

# Get the active family document
familyManager = doc.FamilyManager

# Store List of EPD Products as Array
data = IN[0]

# Store rest of inputs
stage = IN[1]
product = int(IN[2])
area = int(IN[3])
prodNumber = IN[4]

# Create variable to store carbon value
gwp = []

# Create index value for construction stage
stageIndex = 0

try:
	if stage == "A1-A3":
		stageIndex = 8
	elif stage == "A4":
		stageIndex = 9
	elif stage == "C1":
		stageIndex = 10
	elif stage == "C2":
		stageIndex = 11
	elif stage == "C3":
		stageIndex = 12
	elif stage == "C4":
		stageIndex = 13
	elif stage == "D":
		stageIndex = 14

	# Loop through data lists and get all GWP values for construction stage
	for list in data:
		for item in list:
			gwp.append(item[stageIndex])
			
	# Get GWP for specific product
	chosenGWP = int(gwp[product])
	
	# Calculate embodied carbon for product in family
	carbon = chosenGWP * area
	
	# Store carbon value as parameter
	# Begin new Revit Transaction
	TransactionManager.Instance.EnsureInTransaction(doc)

	# Create new Area Type Family Parameter
	paramName = "prod-" + str(prodNumber) + "-" + str(stage) + "-Carbon"
	newParam = familyManager.AddParameter(paramName, BuiltInParameterGroup.PG_DATA, ParameterType.Integer, False)

	# Set Parameter value
	familyManager.Set(newParam, carbon)

	# Commit transaction changes and close transaction
	TransactionManager.Instance.TransactionTaskDone()
	
	OUT = carbon
	
except Exception as e:
	OUT = "An error occured: {}".format(e)
	# Print error on console
	print("Error: {}".format(e))