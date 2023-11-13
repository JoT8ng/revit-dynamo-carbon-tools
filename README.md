# Revit Dynamo Carbon Tools
_Last update 13/11/2023_

Ongoing project that uses the Revit API Dynamo Python Primer to calculate the embodied carbon emissions of building components using an existing EPD (Environmental Product Declaration) database within a Revit BIM model. This tool allows architects to store and schedule carbon data to conduct analysis of the overall embodied carbon of their construction projects.

## Workflow
To start calculating the embodied carbon of Revit families/geometry in a project the user must first understand how their Revit model is built or what type of families need to be measured.

The embodied carbon Dynamo scripts are divided into three different scripts based on the three main types of Revit families/geometry:
* In Place Families
* Loadable Families
* System Families

Once the user has decided which Revit families to measure, they should open the respective Dynamo file for the chosen family type:

In Place Families:
```
EmbodiedCarbon-InPlaceFamily-S.dyn
EmbodiedCarbon-InPlaceFamily.dyn
```
Loadable Families:
```
EmbodiedCarbon-LoadableFamilyTool-S.dyn
EmbodiedCarbon-LoadableFamilyTool.dyn
```
System Families:
```
EmbodiedCarbon-SystemFamilyTool-S.dyn
EmbodiedCarbon-SystemFamilyTool.dyn
```

For more in depth documentation on how to use each Dynamo script please visit the links below:

[In Place Family](https://github.com/JoT8ng/revit-dynamo-carbon-tools/blob/main/docs/inplacedocs.md), 

[Loadable Family](https://github.com/JoT8ng/revit-dynamo-carbon-tools/blob/main/docs/loadablefamilydocs.md), 

[System Family](https://github.com/JoT8ng/revit-dynamo-carbon-tools/blob/main/docs/systemfamilydocs.md)

### Preparing the EPD Database Excel Document
Before the user starts using the Dynamo scripts to measure the areas or volumes of the geometry and calculate embodied carbon values, they must have prepared an Excel document/database of EPD products in the format below:
<img src="/media/EPDatabaseExcel.png" alt="Image of EPD Database Excel Document with correct formatting">

Please refer to the example Excel document in this repository for the correct formatting:
```
Example-EPD-Database.xlsx
```

_When filling in the EPD database with the relevant products, it is recommended that the user ensures that the GWP (Global Warming Potential) values for each of the construction stages are calculated to the desired unit of measurement for their Revit model. For example: Does the user want to measure the embodied carbon for a piece of geometry per m2 for area or per m3 for volume? Normally, EPD declarations from manufacturers will state the declared units for their products and conversion factors or formulas to m2 or m3._

For ease of use and clarity the example Excel document has been formatted to include columns to input data on the EPD declared unit, conversion formulas, and the desired unit of measurement in the Revit model. It is recommended that the user formats their Excel document in this way to be read by the Dynamo scripts. If more familiar with Dynamo, working with lists, or if the user has prior programming knowledge of data structures the Excel document and script can be modified to read the data in their desired custom way.

### Required Shared Project Parameters
The user must also create two shared Revit project parameters for all families, `EPD Product` and `Embodied Carbon`, before using the Dynamo scripts.

## Files to download
Please refer to the documentation under the workflow section for how to use the scripts and which scripts to use. 
The three main Dynamo script files to download are:
```
EmbodiedCarbon-InPlaceFamily-S.dyn
EmbodiedCarbon-LoadableFamilyTool-S.dyn
EmbodiedCarbon-SystemFamilyTool-S.dyn
```
Please load this custom node into Dynamo for the scripts to work:

Repository file location:
```
/CustomNodes/CarbonNodes/GeometryCalculateAreaVolume.dyf
```
File Name:
```
GeometryCalculateAreaVolume.dyf
```
If you would like a more customizable experience you can download the below Dynamo scripts without the custom node:
```
EmbodiedCarbon-InPlaceFamily.dyn
EmbodiedCarbon-LoadableFamilyTool.dyn
EmbodiedCarbon-SystemFamilyTool.dyn
```

# External Dynamo Packages Required
List of external Dynamo packages that need to be installed:
* archi-lab.net

`archilab` is required because the scripts require the `mass addition` node.
