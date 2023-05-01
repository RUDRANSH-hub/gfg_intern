#1. Protein visualization using showmol()function
#Using py3Dmol object
#To visualize any protein structure, all we need is the PDB ID of the protein.

from stmol import showmol
import py3Dmol
# 1A2C
# Structure of thrombin inhibited by AERUGINOSIN298-A from a BLUE-GREEN ALGA
xyzview = py3Dmol.view(query='pdb:1A2C') 
xyzview.setStyle({'cartoon':{'color':'spectrum'}})
showmol(xyzview, height = 500,width=800)

