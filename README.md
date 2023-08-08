# STEVFNs
Space Time Energy Vector Flow Networks


## Referencing

Please cite all the references in "CITATIONS.bib" file.

## Installation

1. Clone the repository to your desired local path
```
...your_path/ % git clone https://github.com/OmNomNomzzz/STEVFNs.git
```

and either:
2. Create an environment from the environment.yaml file
```
...your_path/STEVFNs % conda env create -f envs/environment.yaml
```

Or
3. install the following required dependencies individually:

(a) cvxpy
```
conda install -c conda-forge cvxpy
```
(b) pandas
```
conda install pandas
```

(c) matplotlib
```
conda install matplotlib
```



## Tutorials
A seminar series on the STEVFNs tool is available on Aniq's YouTube channel:

1. A tutorial on how to use the STEVFNs tool can be found in the [STEVFNs demo seminar](https://www.youtube.com/watch?v=_n2w6Zzfofw)

2. Details of theoretical physics concepts used to develop STEVFNs is given in the [STEVFNs theory seminar](https://www.youtube.com/watch?v=GIrBYSPbma0). In this seminar, Aniq discusses how you can model any type of energy system asset using generalized coordinates and flows in space-time and type.

3. Details of how assets are modelled in STEVFNs is given in the [STEVENs asset model seminar](https://www.youtube.com/watch?v=caSYzciVFKw):


If you do not wish to watch the long video tutorial, you can follow the steps outlined in Test Run section below, and review the slides in the Training and Setup PDF file.

## Test run

### Example case study

To run the base example, run the **main.py** file in your IDE of choice. This runs an example of the energy system used by the case study in Aniq Ahsan's DPhil thesis, but for 4 days instead of a full year.

### To change the scenario:

1. Open Data/Case_Study/SG_Case_Study/scenario_0/Asset_Parameters.csv
2. Change the value in the "asset type" column for the asset that you wish to change. This should be a number that is defined as an asset brand (see the parameters.csv files in the corresponding asset's folder in Code/Assets).
3. Open Data/Case_Study/SG_Case_Study/scenario_0/Location_Parameters.csv
4. Change the values of the lat and lon for the respective locations.
5. The main branch only contains PV and WIND data for the following locations:
(0,0); (30,30); (30,-30); (-30,30); (-30,-30)
6. To use a different location, make sure you add the necessary RE profiles for the locations in the RE asset code folder. Syntax required for naming these files to their corresponding lat-lon can be found in slide 23 of the setup and training PDF file.

### To make a new scenario:

1. Duplicate (copy and paste) a scenario folder, e.g. the Data/Case_Study/SG_Case_Study/scenario_0 folder in the Data/Case_Study/SG_Case_Study folder
2. Make relevant changes to the scenario.

### To check and add a new brand type for an asset:

1. Open Code/Assets/insert_asset_name/parameters.csv For example, for the EL_Transport asset: Code/Assets/EL_Transport/parameters.csv
2. Add a new line. Make sure the numbers in the "Type" column increase from 0, 1, 2, etc.
3. The units are just for reference, they do not affect the code.
4. Make sure all values columns are filled.
6. You can now use the "Type" number for the new asset brand when changing scenario parameters.

### To change case study:

1. Open Data/Case_Study/SG_Case_Study/Network_Structure.csv
2. Add or remove lines with assets.
3. Make sure the "Asset_Number" column goes from 0,1,2,3,... 
4. Copy the "Asset_Number", "Asset_Class", "Location_1" and "Location_2" columns to all the scenario "Asset_Parameters.csv" files. Make sure the scenarios have brand types defined for all assets.

### To make a new case study:

1. Duplicate (copy and paste) a case study folder, e.g. the Data/Case_Study/SG_Case_Study folder in the Data/Case_Study folder
2. Make relevant changes to the case study.
3. Make relevant changes to scenarios.
4. Open main.py
5. Replace case_study_name from "SG_Case_Study" to the name of the name of the new case study folder.
6. e.g. if the new case study folder is "Aniq_Case_Study", replace the line:
```
case_study_name = "SG_Case_Study"
```
  with the line:
```
case_study_name = "Aniq_Case_Study"
```





