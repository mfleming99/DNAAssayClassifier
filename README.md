# DNA Assay Classifier
This is Max Fleming and Udit Sharma's independent study project for Fall 2019, where we will be building a classier that can identify the assay of an unsequenced Human DNA read based of the result of Bowtie2 and other DNA analysis tools. This project is split up in to two parts, data generation and model training.

## Data Generation
All the functionality needed to generate data is under our `data` folder. 
In order to generate your own data using our functionality you will need the following dependencies.

1. [Bowtie2](https://github.com/BenLangmead/bowtie2/tree/bt2_cxx11) We used this branch which enables random sampling of SRA files. 
2. [NCLS](https://github.com/biocore-ntnu/ncls) This is the interval tree implementation we used to implement our gene annotation percentage.

After installing dependencies, you will be able to generate data using the following command.
 
>`python3 driver.py --index "location of your Bowtie index" --gtf "Location of your gene transfer format file" --mrna "List of your mRNA accessions" --srna "List of your sRNA accessions" --wgs "List of your WGS accessions"`

You can get prebuilt Bowtie indexes from the [Bowtie2 Manual](http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml) . We used *H. sapiens*, NCBI GRCh38 (Download link below) as our reference genome. We used this (Download link below) gene transfer format file, however as long as your gtf matches your reference genome, and gtf should lead to a correct gene annotation percentage. 

>(ftp://ftp.ncbi.nlm.nih.gov/genomes/archive/old_genbank/Eukaryotes/vertebrates_mammals/Homo_sapiens/GRCh38/seqs_for_alignment_pipelines/GCA_000001405.15_GRCh38_no_alt_analysis_set.fna.bowtie_index.tar.gz)

>(ftp://ftp.ensembl.org/pub/release-98/gtf/homo_sapiens/Homo_sapiens.GRCh38.98.gtf.gz)

Getting SRA accessions is a little bit harder than the index and gtf. We used [SRAdb](https://bioconductor.org/packages/release/bioc/html/SRAdb.html)
 to find accessions that we would want to use. We also included the accessions we used under `data/sample_accessions` folder in this repo. 

The output will be three files: `data_output_mrna.csv`, `data_output_srna.csv` and `data_output_wgs.csv`. These files contain data about the SRA accessions that it was passed. 

## Model 

There is an interactive version of our model available on the [bt2-ui](http://bit.ly/bt2ui-beta). Here you can input an accession and our model will predict the assay of the model. The model available on the UI is a random forest, and it achieved a test accuracy of 91%

Both a KNN and the random forest model available on the bt2-ui can be created by running the command:

> python3 main.py --wgs classifier_data/wgs2.csv --mrna classifier_data/mrna2.csv --srna classifier_data/srna2.csv

The output will be the scores of the two models, and a pickle file named forest containing the random forest, as well as a pickle file named knn containing the knn model.
