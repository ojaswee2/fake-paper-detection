import urllib.request
import os

def download_file(url, filename):
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"File downloaded successfully: {filename}")
    except urllib.error.URLError as e:
        print(f"Error occurred while downloading {filename}: {e}")

# Base URL for the FTP server
base_url = "ftp://anonymous:@ftp.ncbi.nlm.nih.gov/pubmed/baseline/"

file_url = base_url + "pubmed23n0001.xml.gz"
file_path = os.path.join(os.getcwd(), "./PubMed_Annual_Baseline/pubmed23n0001.xml.gz")
download_file(file_url, file_path)
