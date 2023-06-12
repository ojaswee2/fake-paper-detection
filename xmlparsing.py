# open the file

# use library to parse xml file

import requests
import xml.etree.ElementTree as ET

def retrieve_pubmed_xml(pmid):
    url = f"https://pubmed2xl.com/xml/{pmid}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error retrieving XML file. Status code: {response.status_code}")
        return None

def parse_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

pmid = input("Enter the PMID: ")

# Retrieve and print the XML file
xml_data = retrieve_pubmed_xml(pmid)

if xml_data:
    print(xml_data)

"""
# Example usage
xml_file_path = "xmlfile.xml"  # Replace with the path to your XML file
xml_root = parse_xml_file(xml_file_path)

# You can now access the XML elements and attributes
if xml_root is not None:
    # Example: Accessing the root element's tag
    print("Root element tag:", xml_root.tag)
    
"""
