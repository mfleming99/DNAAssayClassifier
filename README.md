## DNAAssayClassifier
This is Max Fleming and Udit Sharma's independent study project for Fall 2019, where we will be building a classier that can identify the assay of an unsequenced DNA read based of the result of Bowtie2 and other DNA analysis tools. This project is split up in to two parts, data generation and model training.

#Data Generation
All the functionnality needed to generate data is under our `data` folder. 
In order to generate your own data using our functionality you will need the following dependancies.

1. [Bowtie2] (https://github.com/BenLangmead/bowtie2/tree/bt2_cxx11) we used this branch which enables random sampling of SRA files. 
2. NCLS (https://github.com/biocore-ntnu/ncls) This is the interval tree implimentation we used to implement our gene annotatoin percentage.

After installing depencancies, you will be able to generate data using the following command

`python3 driver.py --index "location of your Bowtie index" --gtf "Location of your gene transfer format file" --mrna "List of your mRNA accessions" --srna "List of your sRNA accessions" --wgs "List of your WGS accessions"`

The output will be three files: `data_output_mrna.csv`, `data_output_srna.csv` and `data_output_wgs.csv`. These files contain data about the SRA accesssions that it was passed. 
