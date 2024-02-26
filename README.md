# Extraction-of-details-of-FASTA-files

## File: `extract_accession_numbers.py`

This Python script extracts NCBI (National Center for Biotechnology Information) Accession Numbers from PDF files and downloads corresponding FASTA sequences from NCBI database.

#### Functions:
1. **extract_accession_numbers(pdf_file_path):**
   - Extracts NCBI Accession Numbers from a given PDF file.
   
2. **download_files(accession_numbers, pdf_filename):**
   - Downloads FASTA files from NCBI for the given Accession Numbers.
   
3. **process_folder(pdf_folder):**
   - Processes all PDF files in a specified folder, extracting Accession Numbers and downloading corresponding FASTA sequences.

### File: `automate_website.py`

This Python script automates a website to upload a fasta file, submit it, and download the result.

#### Functions:
1. **extract_text_from_file(file_path):**
   - Extracts text from a given file.
   
2. **automate_website(file_path, website_url):**
   - Automates the specified website to upload a file, submit it, and download the result.
  
### How to run?

First run extract_accession_numbers.py in the terminal and a new folder named downloads will be created that will contain the FASTA files based on different accession numbers.
Then run the automate_webite.py to get details of each FASTA sequence.

### Purpose of the project:

This project would help easily extract accession numbers from research papers and FASTA sequences simulataneously with ease which would help biological industries to ease out their work and automate this process.


### Accession Numbers:

Accession Numbers are unique identifiers assigned by biological databases, particularly NCBI, to biological sequences such as nucleotide sequences (DNA or RNA) or protein sequences. These identifiers are used to uniquely identify and reference specific biological sequences in various databases and publications. Accession Numbers are essential for retrieving and sharing biological data across different platforms and research studies.

### FASTA Sequence:

FASTA is a text-based format for representing either nucleotide sequences (DNA or RNA) or protein sequences. Each sequence in a FASTA file begins with a single-line description, followed by lines of sequence data. The description line starts with a ">" character and typically contains information about the sequence, such as its name or source. The sequence data consists of letters representing the nucleotides (A, T, C, G for DNA; A, U, C, G for RNA) or amino acids (single-letter codes) for proteins.


### Use in Biology and Industries:

1. **Biological Research:**
   - FASTA sequences are fundamental for storing, sharing, and analyzing biological data in fields such as genomics, proteomics, and bioinformatics.
   - Researchers use FASTA files to study DNA, RNA, and protein sequences, perform sequence alignments, identify genes, predict protein structures, and conduct evolutionary analysis.

2. **Medical and Pharmaceutical Industries:**
   - In medical research and pharmaceutical industries, FASTA sequences are crucial for studying genetic variations, identifying disease-causing mutations, and developing targeted therapies.
   - FASTA sequences are used in drug discovery, vaccine development, and personalized medicine to understand the molecular basis of diseases and design effective treatments.

3. **Agricultural Biotechnology:**
   - In agriculture, FASTA sequences are utilized for crop improvement, genetic engineering, and breeding programs to enhance crop yields, improve resistance to pests and diseases, and develop stress-tolerant varieties.
   - Researchers use FASTA sequences to study the genetic diversity of crops, identify desirable traits, and develop molecular markers for marker-assisted selection.

4. **Environmental and Industrial Applications:**
   - FASTA sequences play a role in environmental research, biodiversity conservation, and bioremediation by studying microbial communities, ecological interactions, and genetic adaptations to environmental changes.
   - In industrial biotechnology, FASTA sequences are used for enzyme discovery, metabolic engineering, and biofuel production to develop sustainable bioprocesses and renewable energy sources.
