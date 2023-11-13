# System Family Embodied Carbon Tools - Documentation

Below image shows an overview of the Dynamo script and all its nodes:
<img src="/media/SystemFamily/SystemFamily-Overview.png" alt="System family Dynamo Script overview">

* Nodes grouped in pink/red requires some form of user input
* Output groups are in blue

Open the Revit model and open the `EmbodiedCarbon-SystemFamilyTool-S.dyn` or `EmbodiedCarbon-SystemFamilyTool.dyn` script in Dynamo.

## Step 1: Select family category and filter elements
<img src="/media/SystemFamily/SelectFamilyCategory.png" alt="select family category">
As indicated by the node, select the family category that you wish to get the embodied carbon value of (in the above example the user has selected the walls category).

Lets say that only walls of a certain family type and name share the same EPD product. Therefore, the walls must be filtered to select only the ones that share the same EPD product that the user would like to measure.
<img src="/media/SystemFamily/FilterElements.png" alt="filter elements in category">
In the `Filter Elements` grouped node, adjust the value in the strings to the family type name of the elements you would like to filter out.

## Step 2: Extract area parameter from a nested list of element parameters
Once a family category has been selected, the script will extract all the family parameters and their values into a nested list.
<img src="/media/SystemFamily/ExtractElementParameters.png" alt="filter elements extract parameters">
Take a note of the list index value of the `area` and `family type and name` parameters. These index values will need to be input by the user into the node group called `Filter Elements and Extract Area Parameter` in `Family Name List Index` and `Parameter Name List Index`.
<img src="/media/SystemFamily/ExtractArea.png" alt="extract area parameter value">
In the example above the index value for the area parameter is `1` and the index value for the family type and name value is `34`. These numbers will change depending on the parameters in each Revit project. Also note that the values in the string inputs are the same values in the strings in step 1 to filter out the element category. The `output` should be a list of areas or volumes of the selected and filtered elements.

_Optionally: The Dynamo script also calculates the total area of the selected and filtered elements._

## Step 3: Select EPD Database/Excel Document
<img src="/media/SystemFamily/FamilyCarbon-SelectExcel.png" alt="select excel document">
As indicated by the node, select the Excel file saved on your computer that contains all the EPD product information. The nodes will retrieve the document file path and extract the data from the excel file and format it into a nested list. 
<img src="/media/SystemFamily/FamilyCarbon-ExtractExcelData.png" alt="extract data from excel">

## Step 4: Select EPD Product
<img src="/media/SystemFamily/FamilyCarbon-SelectProductName.png" alt="select EPD product">
The group of nodes in green will output a list of EPD product names. The user will input the list index number of the EPD product they would like to use into the node called `Index of Product Names List` inside the pink/red node group. For example: In the image above the user selects `WICTEC EL60` and inputs the value of `1` into the node.

## Step 5: Select Construction Stage
<img src="/media/SystemFamily/CalculateEmbodiedCarbon.png" alt="select construction stage">
Connect the node with the chosen construction stage into `IN[1]` of the `Python Script` node. The `output` of the `Python Script` node will be the embodied carbon value of the geometry based on the chosen product and the GWP of the selected construction stage.

## Step 6: Output
The following group of nodes will save the chosen EPD Product and the embodied carbon value into a shared project parameter for the in place Revit family.
<img src="/media/SystemFamily/StoreEPDParameter.png" alt="output store EPD product name">
<img src="/media/InPlaceFamily/SetEmbodiedCarbonParameter.png" alt="output store embodied carbon value">
Ensure that the parameter name given in the `Parameter Name` node correctly matches the shared project parameter created in the family.
When selecting the system family in the Revit model, the properties tab should show the embodied carbon and EPD product information stored in the shared project parameters:
<img src="/media/SystemFamily/RevitOutputExample.png" alt="Revit model output">
