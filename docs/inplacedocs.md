# In Place Family Embodied Carbon Tools - Documentation

Below image shows an overview of the Dynamo script and all its nodes:
<img src="/media/InPlaceFamily/InPlaceFamilyOverview.png" alt="In place family Dynamo Script overview">

* Nodes grouped in pink/red requires some form of user input
* Output groups are in blue

Open the Revit model and open the `EmbodiedCarbon-InPlaceFamily-S.dyn` or `EmbodiedCarbon-InPlaceFamily.dyn` script in Dynamo.

## Step 1: Select family geometry
<img src="/media/InPlaceFamily/FamilyCarbon-Select.png" alt="select family geometry">
As indicated by the node, select the geometry within the family that you wish to get the embodied carbon value of.

## Step 2: Calculate the area and volume of the geometry
Depending on which Dynamo script you have chosen the group of nodes will either show its original complexity:
<img src="/media/InPlaceFamily/CalculateAreaVolume.png" alt="calculate area volume nodes">
or it will show the custom-node:
<img src="/media/GeometryCalculateAreaVolumeNode.png" alt="custom node">
These group of nodes will have three outputs into a nested list:
* volume by solid
* area by solid
* area by surfaces
  
The user is then required to select one of these outputs and feed it into the group of nodes that calculates the total area or volume of the listed values.
<img src="/media/InPlaceFamily/CalculateTotalAreaVolume.png" alt="calculate total area volume nodes">

## Step 3: Select EPD Database/Excel Document
<img src="/media/InPlaceFamily/FamilyCarbon-SelectExcel.png" alt="select excel document">
As indicated by the node, select the Excel file saved on your computer that contains all the EPD product information. The nodes will retrieve the document file path and extract the data from the excel file and format it into a nested list. 
<img src="/media/InPlaceFamily/FamilyCarbon-ExtractExcelData.png" alt="extract data from excel">

## Step 4: Select EPD Product
<img src="/media/InPlaceFamily/FamilyCarbon-SelectProductName.png" alt="select EPD product">
The group of nodes in green will output a list of EPD product names. The user will input the list index number of the EPD product they would like to use into the node called `Index of Product Names List` inside the pink/red node group. For example: In the image above the user selects `WICTEC EL60` and inputs the value of `1` into the node.

## Step 5: Select Construction Stage
<img src="/media/InPlaceFamily/CalculateEmbodiedCarbon.png" alt="select construction stage">
Connect the node with the chosen construction stage into `IN[1]` of the `Python Script` node. The `output` of the `Python Script` node will be the embodied carbon value of the geometry based on the chosen product and the GWP of the selected construction stage.

## Step 6: Output
The following group of nodes will save the chosen EPD Product and the embodied carbon value into a shared project parameter for the in place Revit family.
<img src="/media/InPlaceFamily/StoreEmbodiedCarbonParameter.png" alt="output store EPD product name">
<img src="/media/InPlaceFamily/StoreEPDParameter.png" alt="output store embodied carbon value">
Ensure that the parameter name given in the `Parameter Name` node correctly matches the shared project parameter created in the family.
When selecting the in place family in the Revit model, the properties tab should show the embodied carbon and EPD product information stored in the shared project parameters:
<img src="/media/InPlaceFamily/RevitOutputExample.png" alt="Revit model output">
