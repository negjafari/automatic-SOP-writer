# Automatic SOP Writer

## Overview

The **Automatic SOP Writer** is a data mining project designed to generate personalized Statement of Purpose (SOP) documents based on user input and information extracted from a university dataset. The project utilizes data preprocessing, keyword extraction, and external tools to automate the SOP writing process.

## How It Works

1. **User Input:**
   - Users provide the target university, desired field of study, and personal keywords.
  
2. **Text Preprocessing and Keyword Extraction:**
   - Text preprocessing includes cleaning, stop word removal, and tokenization.
   - Keywords related to the user's university and field of study are extracted.

3. **Motivation Letter Generation:**
   - Extracted keywords are sent to [www.gomoonbeam.com](www.gomoonbeam.com) to generate a motivation letter.

4. **Results Visualization:**
   - The extracted keywords are saved in a 'extracted_keywords' column.
   - A word cloud visualizes the extracted keywords.

## Project Structure

- **`preprocessing`:**
   - Includes text preprocessing and keyword extraction.

- **`crawling`:**
   - Scripts for crawling [www.gomoonbeam.com](www.gomoonbeam.com) using the Selenium library.
 
## Dataset

The dataset used in this project is sourced from [Dataset Name/Source]. It includes information about various universities, which is preprocessed to extract relevant keywords.

### Dataset Source

The dataset used in this project was obtained from [masters_portal]. This dataset contains 60425 master degree programs from around the world.
link to the dataset provided below : 
[masters_portal.csv.zip](https://github.com/negjafari/automatic-SOP-writer/files/13322143/masters_portal.csv.zip)

## Data Preprocessing

Before usage, the dataset undergoes preprocessing to ensure the extraction of relevant keywords. The preprocessing steps include:

1. Cleaning the dataset.
2. Handling missing values. (Efforts have been made to address missing values in the dataset, employing tailored methods for each relevant column)
3. Structuring the data for efficient keyword extraction.

## Usage

The dataset is employed during the text preprocessing phase to extract keywords related to the user's specified university and field of study. These keywords contribute to the generation of personalized motivation letters.

## Code Files

This repository includes both Jupyter Notebook and Python script files:

- **`datamining_proj1_phase1.ipynb`:**
  - Jupyter Notebook file containing the main implementation.

- **`datamining_proj1_phase1.py`:**
  - Python script file with the same functionality as the Jupyter Notebook.

## Sample Output

A sample output, including extracted keywords and a generated SOP, is available in the output directory. You can refer to this example to understand the structure of the output and the effectiveness of the SOP generation process.
