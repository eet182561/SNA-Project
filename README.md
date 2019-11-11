# SNA-Project
Bust Route Analysis using social networking techniques. This readme consist of how to run various code files and description of major functions.


## Data collection
The [AUTODOWNLOAD.ipyb](https://github.com/eet182561/SNA-Project/blob/master/AUTODOWNLOAD.ipynb/) file contains step by step instruction how we downloaded the data from various websites.
This file generates a csv file containing route information and geographical cordinates. We use this file to extract L1 space.
### Format of the output file
The output csv file must have the following coulumn heading necessary for further processing. We have called the output table as [Basicmodtable.csv].It must have "RouteNumber","Source","Destination" (all without quotes)columns required for further processing by other script files.
## Formation of different Spaces
### L-Space
The output of [AUTODOWNLOAD.ipyb](https://github.com/eet182561/SNA-Project/blob/master/AUTODOWNLOAD.ipynb/) script [BasicTablemod.csv](https://github.com/eet182561/SNA-Project/blob/master/BasicTablemod.csv) generates a CSV file which is our L Space. We will derive other spaces based on this space.

### P-space
Use the script [PSpace.py](https://github.com/eet182561/SNA-Project/blob/master/PSpace.py) to generate the Pspace. Set the parameter loc to the location of the CSV file in the above mentioned format. 
### BiPartite Graph(B-Space)
The [CSVtoGEFX.py](https://github.com/eet182561/SNA-Project/blob/master/CSVtoGEFX.py)This takes input from CSV and edits the standard GEXF to add labels to nodes so that they can be plotted by "Event Layout" plugin in the gephi.
