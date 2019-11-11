# SNA-Project
Bust Route Analysis using social networking techniques. This readme consist of how to run various code files and description of major functions. Out Project uses python3 for data processing and Gephi and Google Earth for visualization.
Requirements:
For Python install the packages in req.txt. These can be installed also using pip install 
```bash
pip install -r req.txt
```
For Gephi we have used "Event Graph Layout" plugin. 

## Data collection
The [AUTODOWNLOAD.ipyb](https://github.com/eet182561/SNA-Project/blob/master/AUTODOWNLOAD.ipynb/) file contains step by step instruction how we downloaded the data from various websites.
This file generates a csv file, [Basicmodtable.csv](https://github.com/eet182561/SNA-Project/blob/master/BasicTablemod.csv) containing route information and geographical cordinates. We use this file to extract L1 space.
### Format of the output file
The output csv file must have the following coulumn heading necessary for further processing. We have called the output table as [Basicmodtable.csv](https://github.com/eet182561/SNA-Project/blob/master/BasicTablemod.csv).It must have "RouteNumber","Source","Destination" (all without quotes)columns required for further processing by other script files.
## Formation of different Spaces
### L-Space
The output of [AUTODOWNLOAD.ipyb](https://github.com/eet182561/SNA-Project/blob/master/AUTODOWNLOAD.ipynb/) script [BasicTablemod.csv](https://github.com/eet182561/SNA-Project/blob/master/BasicTablemod.csv) generates a CSV file which is our L Space. We will derive other spaces based on this space.

### P-space
Use the script [PSpace.py](https://github.com/eet182561/SNA-Project/blob/master/PSpace.py) to generate the Pspace. Set the variable loc to the location of the CSV file in the above mentioned format.
```python
loc = 'BasicTablemod.csv' #Replace this with your filename in the above format
```
This script will store the P-space graph in a networkx variable called PGraph. We run networkx's Flyod Warshall Algorithm to get the minimum hops(route changes required) to reach from one bus station to another. The minimum hops are stored in "fwnp" variable which is a numpy matrix where each row and coumn correspond to a bus station. The script finally uses fwnp matrix to plot the histogram of number of hops.
### BiPartite Graph(B-Space)
The [CSVtoGEFX.py](https://github.com/eet182561/SNA-Project/blob/master/CSVtoGEFX.py)This takes input from CSV and edits the standard GEXF to add labels to nodes so that they can be plotted by "Event Layout" plugin in the gephi. The output of this file is a siple gexf file and the the label are read as string. So one needs to duplicate the "label" column in the "Data Explorer" Tab > "Nodes" to integer values.
### C-space
The [CspaceTablemaker.py](https://github.com/eet182561/SNA-Project/blob/master/CSpaceTableMaker.py) script takes our [BasicTablemod.csv](https://github.com/eet182561/SNA-Project/blob/master/BasicTablemod.csv) and process it to fowm various C-space tables and save them in .csv format. Our results can be found in the [Output/Cspace](https://github.com/eet182561/SNA-Project/tree/master/Outputs/CSpace) folder.

## Misc Scripts
[viz.py](https://github.com/eet182561/SNA-Project/blob/master/viz.py) A quick script to visualize the the graph on network x
