#Revit Dynamo Carbon Tools
*Last update 10/11/2023*

Ongoing project that uses the Revit API Dynamo Python Primer to calculate the embodied carbon emissions of building components using an existing EPD (Environmental Product Declaration) database within a Revit BIM model. This tool allows architects to store and schedule carbon data to conduct analysis of the overall embodied carbon of their construction projects.

##Workflow
Work in Progress

##Files to download
Please refer to the documentation under the workflow section for how to use the scripts and which scripts to use. The three main Dynamo script files to download are:
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

#External Dynamo Packages Required
List of external Dynamo packages that need to be installed:
*archi-lab.net
archilab is required because the scripts require the "mass addition" node.
