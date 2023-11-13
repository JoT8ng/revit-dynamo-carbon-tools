# Loadable Family Embodied Carbon Tools - Documentation

Below image shows an overview of the Dynamo script and all its nodes:
<img src="/media/LoadableFamily/FamilyCarbon-Overview.png" alt="Loadable family Dynamo Script overview">

* Nodes grouped in pink/red requires some form of user input
* Output groups are in blue

Open the Revit model and open the `EmbodiedCarbon-LoadableFamilyTool-S.dyn` or `EmbodiedCarbon-LoadableFamilyTool.dyn` script in Dynamo.

## Step 1: Select family geometry and input product number
<img src="/media/LoadableFamily/FamilyCarbon-Select.png" alt="select family geometry">
As indicated by the node, select the geometry within the family that you wish to get the embodied carbon value of. As there may be multiple geometries within a family (extrusions, sweeps, massing etc.), this script will create parameters for each geometry for EPD product name, area or volume, and embodied carbon. Therefore, for each geometry with a different product the user must input a different product number each time the script is run.
<img src="/media/LoadableFamily/FamilyCarbon-ProductNumber.png" alt="input product number">

## Step 2: Calculate the area and volume of the geometry
Depending on which Dynamo script you have chosen the group of nodes will either show its original complexity:
<img src="/media/LoadableFamily/FamilyCarbon-AreaVolume.png" alt="calculate area volume nodes">

or it will show the custom-node:
<img src="/media/GeometryCalculateAreaVolumeNode.png" alt="custom node">

These group of nodes will have three outputs into a nested list:
* volume by solid
* area by solid
* area by surfaces
The user is then required to select one of these outputs and feed it into the group of nodes that calculates the total area or volume of the listed values.
<img src="/media/LoadableFamily/FamilyCarbon-TotalAreaVolume.png" alt="calculate total area volume nodes">

## Step 3: Select EPD Database/Excel Document
<img src="/media/LoadableFamily/FamilyCarbon-SelectExcel.png" alt="select excel document">
As indicated by the node, select the Excel file saved on your computer that contains all the EPD product information. The nodes will retrieve the document file path and extract the data from the excel file and format it into a nested list. 
<img src="/media/LoadableFamily/FamilyCarbon-ExtractExcelData.png" alt="extract data from excel">

## Step 4: Select EPD Product
<img src="/media/LoadableFamily/FamilyCarbon-SelectProductName.png" alt="select EPD product">
The group of nodes in green will output a list of EPD product names. The user will input the list index number of the EPD product they would like to use into the node called `Index of Product Names List` inside the pink/red node group. For example: In the image above the user selects `WICTEC EL60` and inputs the value of `1` into the node.

## Step 5: Select Construction Stage
<img src="/media/LoadableFamily/FamilyCarbon-OutputCarbon.png" alt="select construction stage">
Connect the node with the chosen construction stage into `IN[1]` of the `Python Script` node. The `output` of the `Python Script` node will be the embodied carbon value of the geometry based on the chosen product and the GWP of the selected construction stage.

## Step 6: Output
The following group of nodes will save the chosen EPD Product and the embodied carbon value into a type family parameter inside the Revit family.
<img src="/media/LoadableFamily/FamilyCarbon-OutputAreaVolume.png" alt="output store area or volume">
Ensure that you choose either area or volume for the parameter name.
<img src="/media/LoadableFamily/FamilyCarbon-OutputCarbon.png" alt="output store embodied carbon value">
<img src="/media/LoadableFamily/FamilyCarbon-OutputProduct.png" alt="output store embodied carbon value">
The parameters tab should show the embodied carbon and EPD product information for each geometry inside the Revit Family:
<img src="/media/LoadableFamily/FamilyCarbon-ModelExample.png" alt="Revit model output">
_To schedule the information, it is recommended that the user stores the total embodied carbon values for all the products in the family into a shared project parameter called `Embodied Carbon`._
