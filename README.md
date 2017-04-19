<b>LZ_Wrapper: A wrapper utility to create data, a local web server and html files for LocusZoom js to work.</b>

<b>Requirements</b>

  Python
  Python Flask package
  Pandas
  Internet connection

<b>Input data</b>
  Three types of input files are needed for this utility to work:
  1. For each trait/phenotype of interest, a \<trait\>.txt file with all the loci of interest in it. For example, one would have a si.txt for smoking initiation, sc.txt for smoking cessation, and so on. These files <b>should have a header line</b>.
  
  The important columns here are:
    Column 1 : <b>Chromosome</b>
    Column 2 : <b>Position</b>
    Column 3 : <b>Marker/Variant ID</b>. The variant ID should be of the format chr:position_REF/ALT. The ref allele is inferred from this variant id.
    Column 4 : <b>p value</b>
  The trait file can have other columns after column 4 - those will be ignored.
  See Examples for trait file examples (t1.txt, t2.txt, t3.txt).
  
  2. A sig_variant.txt file with all the significant variants a user may want to explore (the TOP hits in the app). For the example, this file contains the positions in TOP Hits in the following image:
 ![Alt text](/Example/TopHits.png?raw=true "Top Hits")

  There are two columns in the significant variants file:
    Column 1 : <b>Chromosome</b>
    Column 2 : <b>Position</b>
  
  3. A phenotypes file. This file specifies the different phenotypes/traits of interest and their ids. 
  There are two columns in the phenotypes file:
    Column 1 : <b>Phenotype id</b>
    Column 2 : <b>Phenotype name</b>
  
  <b>NOTE:</b> Be very careful to have the phenotype id exactly the same as the filenames for each trait (trait.txt) file. 
