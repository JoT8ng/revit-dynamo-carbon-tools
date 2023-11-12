import clr
 
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
doc =  DocumentManager.Instance.CurrentDBDocument
 
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
 
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *


# Get input serarch terms
filter1 = IN[0]
filter2 = IN[1]
filter3 = IN[2]

# Defining the search terms
search_terms = [filter1, filter2, filter3]

# Collecting all wall instances
walls_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType()

# Filtering walls with specific family type names
filtered_walls = [wall for wall in walls_collector if any(term in wall.Name for term in search_terms)]

# Returning the list of filtered walls
OUT = filtered_walls
