# DNAAssayClassifier
This is Max Fleming and Udit Sharma's independent study project for Fall 2019, where we will be building a classier that can identify the assay of an unsequenced DNA read based of the result of Bowtie2 and other DNA analysis tools. This project is split up in to two parts, data generation and model training.

## Data Generation
All the functionnality needed to generate data is under our `data` folder. 
In order to generate your own data using our functionality you will need the following dependancies.

1. [Bowtie2](https://github.com/BenLangmead/bowtie2/tree/bt2_cxx11) we used this branch which enables random sampling of SRA files. 
2. [NCLS](https://github.com/biocore-ntnu/ncls) This is the interval tree implimentation we used to implement our gene annotatoin percentage.

After installing depencancies, you will be able to generate data using the following command.
 
>`python3 driver.py --index "location of your Bowtie index" --gtf "Location of your gene transfer format file" --mrna "List of your mRNA accessions" --srna "List of your sRNA accessions" --wgs "List of your WGS accessions"`

You can get prebuild Bowtie indexes from the [Bowtie2 Manual](http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml) . We used *H. sapiens*, NCBI GRCh38 (Download link below) as our reference genome. We used this (Download link below) gene transfer format file, however as long as your GTF matches your reference genome, and GTF should work 

(ftp://ftp.ncbi.nlm.nih.gov/genomes/archive/old_genbank/Eukaryotes/vertebrates_mammals/Homo_sapiens/GRCh38/seqs_for_alignment_pipelines/GCA_000001405.15_GRCh38_no_alt_analysis_set.fna.bowtie_index.tar.gz)
(ftp://ftp.ensembl.org/pub/release-98/gtf/homo_sapiens/Homo_sapiens.GRCh38.98.gtf.gz)

Getting SRA accessions is a little bit harder than the index and gtf, however we used __ and ___
 to find accessions that we would want to use. You could also do this manually by pursuing the SRA database. We also included the accessions we used under `data\sample_accessions` folder in this repo. 

The output will be three files: `data_output_mrna.csv`, `data_output_srna.csv` and `data_output_wgs.csv`. These files contain data about the SRA accesssions that it was passed. 

## Model 

There is an intervative version of our model avalibly on the [bt2-ui](http://bit.ly/bt2ui-beta). Here you can input an accession and our model will predict the assay of the model. 
