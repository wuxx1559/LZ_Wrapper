# **LZ_Wrapper: A wrapper utility to create data, a local web server and html files for LocusZoom js to work.**

## **Requirements**

- Python
- Python Flask package
- Pandas
- Internet connection

## **Input data**

Three types of input files are needed for this utility to work:
 
### 1. For each trait/phenotype of interest, a \<trait\>.txt file with all the loci of interest in it. 

For example, one would have a si.txt for smoking initiation, sc.txt for smoking cessation, and so on. These files **should have a header line**.

  The important columns here are:
  - Column 1 : **Chromosome**
  - Column 2 : **Position**
  - Column 3 : **Marker/Variant ID**. The variant ID should be of the format chr:position_REF/ALT. The ref allele is inferred from this variant id.
  - Column 4 : **p value**
  The trait file can have other columns after column 4 - those will be ignored.
  See Examples for trait file examples (t1.txt, t2.txt, t3.txt).
  
### 2. A sig_variant.txt file with all the significant variants a user may want to explore (the TOP hits in the app). 

For the example, this file contains the positions in TOP Hits in the following image:
 ![Alt text](/Example/TopHits.png?raw=true "Top Hits")

  There are two columns in the significant variants file:
  - Column 1 : **Chromosome**
  - Column 2 : **Position**
  
### 3. A phenotypes file. 

This file specifies the different phenotypes/traits of interest and their ids.

  There are two columns in the phenotypes file:
  - Column 1 : **Phenotype id**
  - Column 2 : **Phenotype name**
  
  **NOTE:** Be very careful to have the phenotype id exactly the same as the filenames for each trait (trait.txt) file.

## **Step 1**

The first step is to create a csv file with the input data. Here we use the \<trait\>.txt files as input to the **createCSV.py** script. The script outputs a file named **assoc.csv**.

`python createCSV.py -h` to look at the inputs needed. 

`python createCSV.py t1.txt t2.txt ...` 

For example: `python createCSV.py ai.txt cpd.txt si.txt sc.txt`

## **Step2**

The second step is to create the html file needed to run LocusZoom js. The script **createCode.py** creates this html file. Inputs to the script are the sig_variant.txt and phenotypes.txt files. The script outputs text in html format which can be redirected to a html file of user's choice.

`python createCode.py -h` to look at the inputs needed. 

`python createCode.py sig_variant.txt phenotypes.txt > Example.html`

 As a reminder, the phenotype ids (column 1) of the phenotypes file should exactly match the input file names for each trait in step 1.

## **Step3**

The third and the final step is to run the **app.py** script.

`python app.py`

This starts a localhost server at port 8000. 

If your local port 8000 is already taken, specify another part by changing the following line in app.py before running it:

`app.run(port=8000)`

You can specify any port number there.

Be sure to also modify the html file generated in step 2 by changing the port number in the following line:

`var dataBase = 'http://127.0.0.1:8000/single/'`

by replacing the 8000 with the actual port number. Alternatively, you can modify that line in mid.html and then run createCode.py again.

## **Step 4**

Now that the app is running, open the html file generated in **step 2** in a browser of your choice, and explore!

**NOTE:** The initial panel for LocusZoom is around the `15:78800000-78820000` region of chromosome 15. If you wish to modify that, go into your html file, and modify the following line:

`<div id="plot" data-region="15:78800000-78820000"></div>`

to your region of interest. For example, if a user wants the initial view to have the range 1011001-1020000 of Chromosome 1, they will replace the `15:78800000-78820000` with `1:1011001-1020000`.


