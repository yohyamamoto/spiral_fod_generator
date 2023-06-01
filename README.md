# Spiral FOD generator
FOD generator that uses spiral algorithm

Usage:

Edit and change the lines in the code where you can specify the numbers of electrons in the alpha/beta channel and the center of the atom. 


  #User inputs  
  #no. of orbitals in first, second, third shells  
  num_orb_a = 1, 4, 9  
  num_orb_b = 1, 4, 3  
  #center position  
  pos = 0.0, 0.0, 0.0


Then run:

`python3 spiralfod.py > FRMIDT`




Future todo:

* Loop over atoms to generate FODs for molecules

* Improve the input
