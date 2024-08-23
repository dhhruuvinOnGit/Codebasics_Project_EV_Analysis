# CodeBasics Data Analysis Project: "Provide Insights to an Automotive company on Electric vehicles launch in India"

## Problem Statement

AtliQ Motors is an automotive giant from the USA specializing in electric vehicles (EV). In the last 5 years, their market share rose to 25% in electric and hybrid vehicles segment in North America. As a part of their expansion plans, they wanted to launch their bestselling models in India where their market share is less than 2%. Bruce Haryali, the chief of AtliQ Motors India wanted to do a detailed market study of existing EV/Hybrid market in India before proceeding further. Bruce gave this task to the data analytics team of AtliQ motors and Peter Pandey is the data analyst working in this team.

## Overview

This project involves analyzing electric vehicle (EV) sales across different states in India, focusing on the sales trends for 2-wheelers and 4-wheelers. The project includes calculating the Compound Annual Growth Rate (CAGR) for projected EV sales by 2030 and estimating revenue growth rates from 2022 to 2024.

## Dataset

**electric_vehicle_sales_by_state.csv**

- date: The date on which the data was recorded. Format: DD-MMM-YY. (Data is recorded on a monthly basis)
- state: The name of the state where the sales data is recorded. This indicates the geographical location within India.
- vehicle_category: The category of the vehicle, specifying whether it is a 2-Wheeler or a 4-Wheeler.
- electric_vehicles_sold: The number of electric vehicles sold in the specified state and category on the given date.
- total_vehicles_sold: The total number of vehicles (including both electric and non-electric) sold in the specified state and category on the given date.


**electric_vehicle_sales_by_makers.csv**

- date: The date on which the sales data was recorded. Format: DD-MMM-YY. (Data is recorded on a monthly basis)
- vehicle_category: The category of the vehicle, specifying whether it is a 2-Wheeler or a 4-Wheeler.
- maker: The name of the manufacturer or brand of the electric vehicle.
- electric_vehicles_sold: The number of electric vehicles sold by the specified maker in the given category on the given date.

**dim_date.csv**

- date: The specific date for which the data is relevant. Format: DD-MMM-YY. (Data is recorded on a monthly basis)
- fiscal_year: The fiscal year to which the date belongs. This is useful for financial and business analysis.
- quarter: The fiscal quarter to which the date belongs. Fiscal quarters are typically divided as Q1, Q2, Q3, and Q4.

## Few Key Points:

1. **Fiscal Year**: The fiscal year is a one-year period used for financial reporting and budgeting, starting on April 1st and ending on March 31st of the following year in India.

2. **Penetration Rate**: This metric represents the percentage of total vehicles that are electric within a specific region or category. It is calculated as:
		Penetration Rate =  (Electric Vehicles Sold / Total Vehicles Sold) * 100  
   This indicates the adoption level of electric vehicles.

3. **Compound Annual Growth Rate (CAGR)**: CAGR measures the mean annual growth rate over a specified period longer than one year. It is calculated as:
		
        CAGR = [(Ending Value / Beginning Value) ** 1/n] -1

## Project Structure

The project consists of the following key files:

### 1. `data_preparation.ipynb`
- **Purpose:** The goal of this notebook is to streamline data access by dividing the original dataset into distinct groups.
- **Key Components:**
  - Segregating data on basis of states and makers.
  - Dividing data based on vehicle category: two-wheelers and four-wheelers.
  - Data cleaning.

### 2. `primary_analysis.ipynb`
- **Purpose:** This notebook contains the analysis of EV sales trends for the primary questions based on the problem statement.
- **Key Components:**
  - Data pre-processing and feature engineering.
  - Calculation of variuos metrics.
  - Analysis and Visualization of the trends.

### 3. `generate_report.py`
- **Purpose:** To create a markdown file for making a report of the analysis performed.
- **Key Components:**
  - Summarization of Primary and Secondary Analysis to represent the insights in form of a report.

### 4. `Codebasic_EV_Analysis_Report.pdf`
- **Purpose:** To represent the report in PDF format.
- **Key Components:**
  - PDF file to interpret the report.

### 5. `index.html` (was earlier `Codebasic_EV_Analysis_Report.html`)
- **Purpose:** To represent the report on a webpage using html.
- **Key Components:**
  - HTML code file to interpret the report over a webpage.

## Prerequisites

Before running the notebooks, ensure you have the following installed:

- Python 3.x
- Jupyter Notebook
- Required Python libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn

You can install the required libraries using pip:

```sh
pip install pandas numpy matplotlib seaborn
```

## Running the Notebooks

1. **Clone the repository** (if hosted on a version control platform like GitHub):

```sh
git clone <repository_url>
```

2. **Navigate to the project directory**:

```sh
cd <project_directory>
```

3. **Launch Jupyter Notebook**:

```sh
jupyter notebook
```

4. **Open `data_preparation.ipynb`** to run the EV sales trend analysis.

5. **Open `primary_analysis.ipynb`** to run the revenue growth rate analysis.