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

# Get Product Number
prodNumber = IN[0]

# Get Area value
total_area = IN[1]

# Get Area or Volume Parameter Name
paramType = IN[2]

try:
	# Begin new Revit Transaction
	TransactionManager.Instance.EnsureInTransaction(doc)

	# Create new Area Type Family Parameter
	paramName = "prod " + str(prodNumber) + " " + str(paramType)
	areaParam = familyManager.AddParameter(paramName, BuiltInParameterGroup.PG_DATA, ParameterType.Integer, False)

	# Set Parameter value
	familyManager.Set(areaParam, total_area)

	# Commit transaction changes and close transaction
	TransactionManager.Instance.TransactionTaskDone()
	
	OUT = "Parameter created and value set successfully"
	
except Exception as e:
	OUT = "An error occured: {}".format(e)
	# Print error on console
	print("Error: {}".format(e))
