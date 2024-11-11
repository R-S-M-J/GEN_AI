import os
import re
import csv
import json
import yaml
import xlrd
from bs4 import BeautifulSoup
from datetime import datetime
from xml.etree import ElementTree as ET
import PyPDF2
import docx

date_patterns = [
    r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b',
    r'\b\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s\d{2,4}\b',
    r'\b(?:\d{1,2}(?:st|nd|rd|th)?)\s(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}\b',  # e.g., 2nd November 1974
]

names = {"Steeb", "Jonny", "Alexa", "Alex"}
places = {"Jamtha", "Gurugaon", "Seoul", "Tokyo"}

def find_dates(line):
    for pattern in date_patterns:
        match = re.search(pattern, line)
        if match:
            return match.group(0)
    return None

def detect_entities(line):
    detected_info = {
        "names": set(),
        "places": set(),
        "dates": []
    }
    
    # names and places
    words = set(line.split())
    detected_info["names"] = names.intersection(words)
    detected_info["places"] = places.intersection(words)

    # dates
    date = find_dates(line)
    if date:
        detected_info["dates"].append(date)
    
    return detected_info

def process_text_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                entities = detect_entities(line)
                print(f"Line: {line}")
                print("Entities found:", entities)

def process_csv_file(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for cell in row:
                if cell.strip(): 
                    entities = detect_entities(cell)
                    print(f"Cell: {cell}")
                    print("Entities found:", entities)

def process_json_file(file_path):
    with open(file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
        for key, value in data.items():
            if isinstance(value, str):
                entities = detect_entities(value)
                print(f"Key: {key}, Value: {value}")
                print("Entities found:", entities)

def process_xml_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    for elem in root.iter():
        if elem.text:
            entities = detect_entities(elem.text)
            print(f"Tag: {elem.tag}, Text: {elem.text}")
            print("Entities found:", entities)

def process_excel_file(file_path):
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_index(0)
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            cell = sheet.cell_value(row, col)
            if isinstance(cell, str) and cell.strip():
                entities = detect_entities(cell)
                print(f"Cell: {cell}")
                print("Entities found:", entities)

def process_yaml_file(file_path):
    with open(file_path, 'r') as yamlfile:
        data = yaml.safe_load(yamlfile)
        for key, value in data.items():
            if isinstance(value, str):
                entities = detect_entities(value)
                print(f"Key: {key}, Value: {value}")
                print("Entities found:", entities)

def process_html_file(file_path):
    with open(file_path, 'r') as htmlfile:
        soup = BeautifulSoup(htmlfile, 'html.parser')
        for element in soup.find_all(text=True):
            if element.strip():
                entities = detect_entities(element)
                print(f"Element: {element.strip()}")
                print("Entities found:", entities)

def process_markdown_file(file_path):
    with open(file_path, 'r') as mdfile:
        for line in mdfile:
            line = line.strip()
            if line:
                entities = detect_entities(line)
                print(f"Line: {line}")
                print("Entities found:", entities)

def process_log_file(file_path):
    with open(file_path, 'r') as logfile:
        for line in logfile:
            line = line.strip()
            if line:
                entities = detect_entities(line)
                print(f"Line: {line}")
                print("Entities found:", entities)

def process_pdf_file(file_path):
    with open(file_path, 'rb') as pdffile:
        pdf_reader = PyPDF2.PdfReader(pdffile)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            if text:
                for line in text.split('\n'):
                    entities = detect_entities(line)
                    print(f"Line from PDF: {line}")
                    print("Entities found:", entities)

def process_word_file(file_path):
    doc = docx.Document(file_path)
    for para in doc.paragraphs:
        if para.text.strip():
            entities = detect_entities(para.text)
            print(f"Paragraph from Word: {para.text}")
            print("Entities found:", entities)

def process_file(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == '.txt':
        process_text_file(file_path)
    elif file_extension == '.csv':
        process_csv_file(file_path)
    elif file_extension == '.json':
        process_json_file(file_path)
    elif file_extension == '.xml':
        process_xml_file(file_path)
    elif file_extension == '.xlsx':
        process_excel_file(file_path)
    elif file_extension in ['.yaml', '.yml']:
        process_yaml_file(file_path)
    elif file_extension in ['.html', '.htm']:
        process_html_file(file_path)
    elif file_extension == '.md':
        process_markdown_file(file_path)
    elif file_extension == '.log':
        process_log_file(file_path)
    elif file_extension == '.pdf':
        process_pdf_file(file_path)
    elif file_extension == '.docx':
        process_word_file(file_path)
    else:
        print(f"Unsupported file type: {file_extension}")

file_path = './sample.pdf'  
process_file(file_path)
