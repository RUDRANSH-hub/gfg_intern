# giving labeling to our 3D- image:
#Labelling protein using render_pdb_resn()function
#Inorder to mark the residues, we can use the render_pdb_resn() function, which in this example marks the Alanine [ALA] residues,
from stmol import *
# showmol(render_pdb(id = '1A2C'))
showmol(render_pdb_resn(viewer = render_pdb(id = '1A2C'),resn_lst = ['ALA',]))