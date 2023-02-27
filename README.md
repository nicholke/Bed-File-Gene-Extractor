## Bed-File-Gene-Extractor

This script compares a list of genes in a text file to a large bed file and outputs a CSV file containing only the genes that are in both files.

## Requirements
-Python 3
-pandas
## Usage
-Place the script in a directory with the gene list file and bed file.
-Open a terminal window in that directory.
-Run the script with the following command: python gene_bed_comparison.py <gene_list_file> <bed_file> <output_file>
-The output CSV file will be created in the same directory.
## Arguments
-<gene_list_file>: A text file containing a list of genes, with one gene per line.
-<bed_file>: A large bed file containing genomic regions, with one region per line.
-<output_file>: The name of the output CSV file.
