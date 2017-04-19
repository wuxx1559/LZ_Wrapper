**LZ_Wrapper: A wrapper utility to create data, a local web server and html files for LocusZoom js to work.**

## **Requirements**

- Python
- Python Flask package
- Pandas
- Internet connection

## **Input data**

Three types of input files are needed for this utility to work:
 
1. For each trait/phenotype of interest, a \<trait\>.txt file with all the loci of interest in it. For example, one would have a si.txt for smoking initiation, sc.txt for smoking cessation, and so on. These files **should have a header line**.

The important columns here are:
- Column 1 : **Chromosome**
- Column 2 : **Position**
- Column 3 : **Marker/Variant ID**. The variant ID should be of the format chr:position_REF/ALT. The ref allele is inferred from this variant id.
- Column 4 : **p value**
  The trait file can have other columns after column 4 - those will be ignored.<br>
  See Examples for trait file examples (t1.txt, t2.txt, t3.txt).<br><br>
  
  2. A sig_variant.txt file with all the significant variants a user may want to explore (the TOP hits in the app). For the example, this file contains the positions in TOP Hits in the following image:<br>
 ![Alt text](/Example/TopHits.png?raw=true "Top Hits")

  There are two columns in the significant variants file:<br> 
  - Column 1 : <b>Chromosome</b><br>
  - Column 2 : <b>Position</b><br><br>
  
  3. A phenotypes file. This file specifies the different phenotypes/traits of interest and their ids. <br>
  There are two columns in the phenotypes file:<br>
  - Column 1 : <b>Phenotype id</b><br>
  - Column 2 : <b>Phenotype name</b><br>
  
  <b>NOTE:</b> Be very careful to have the phenotype id exactly the same as the filenames for each trait (trait.txt) file. <br><br>

<b>Step 1</b><br><br>
The first step is to create a csv file with the input data. Here we use the \<trait\>.txt files as input to the createCSV.py script. The script outputs a file named <b>assoc.csv</b>. <br>
`python createCSV.py -h` to look at the inputs needed. <br>
`python createCSV.py t1.txt t2.txt ...` <br>
For example: `python createCSV.py ai.txt cpd.txt si.txt sc.txt` <br><br>



