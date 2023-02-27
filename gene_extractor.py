import csv

# Read gene list from file
with open('gene_list.txt') as f:
    gene_list = set([line.strip() for line in f])

# Open bed file for reading and output file for writing
with open('bed_file.bed') as bed_file, open('output.csv', 'w', newline='') as output_file:
    # Create CSV writer
    writer = csv.writer(output_file)
    
    # Loop through bed file and check if each gene is in gene_list
    for line in bed_file:
        fields = line.strip().split('\t')
        gene_name = fields[3]
        if gene_name in gene_list:
            # If gene is in gene_list, write it to output CSV file
            writer.writerow(fields)
