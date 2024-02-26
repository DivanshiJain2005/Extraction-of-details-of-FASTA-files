import os
import PyPDF2
import re
import requests


def extract_accession_numbers(pdf_file_path):
    """Extracts NCBI Accession No from the given PDF file."""
    accession_number_pattern = r"(?i)[A-Z]{1,2}_?\d{5,}"
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        accession_numbers = set()
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            extracted_numbers = re.findall(accession_number_pattern, text)
            accession_numbers.update(extracted_numbers)
    return list(accession_numbers)

def download_files(accession_numbers, pdf_filename):
    """Downloads files from NCBI for the given accession numbers."""
    successful_downloads = set()

    for accession_number in accession_numbers:
        print(f"Found accession number: {accession_number} in {pdf_filename}")
        base_url = f"https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?tool=portal&save=file&log$=seqview&db=nuccore&report=fasta&id={accession_number}"
        print(f"Downloading from: {base_url}")
        try:
            response = requests.get(base_url, allow_redirects=True)
            response.raise_for_status()
            filename = f"{accession_number}.fasta"
            accession_folder = os.path.join("downloads", accession_number)
            pdf_output_folder = os.path.join(accession_folder, pdf_filename)
            os.makedirs(pdf_output_folder, exist_ok=True)  # Create nested folders
            file_path = os.path.join(pdf_output_folder, filename)

            # Skip download if the file already exists
            if os.path.exists(file_path):
                print(f"File {filename} already exists. Skipping download.")
                successful_downloads.add(accession_number)
                continue

            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded {filename} to {pdf_output_folder}")
            successful_downloads.add(accession_number)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {accession_number}: {e}")

    return successful_downloads

def process_folder(pdf_folder):
    """Processes all PDF files in the specified folder."""
    for pdf_filename in os.listdir(pdf_folder):
        if pdf_filename.endswith(".pdf"):
            pdf_filepath = os.path.join(pdf_folder, pdf_filename)
            accession_numbers = extract_accession_numbers(pdf_filepath)

            if accession_numbers:
                print(f"Accession numbers found in {pdf_filepath}:")
                print(*accession_numbers, sep="\n")
                successful_downloads = download_files(accession_numbers, pdf_filename)
                # Exclude successfully downloaded accession numbers from future attempts
                accession_numbers = list(set(accession_numbers) - successful_downloads)
            else:
                print(f"No accession numbers found in {pdf_filepath}.")

if __name__ == "__main__":
    # Specify the path of the folder containing your PDF files
    pdf_folder = r"C:\AIML\folder"

    process_folder(pdf_folder)
