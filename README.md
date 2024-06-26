Overview
----------------------------------------
This project analyzes employee data to derive insights such as average salary by department, salary distribution, and age distribution. 
It includes data cleaning, statistical analysis, and visualization using Python libraries like Pandas, Matplotlib, Seaborn, and Plotly.


Files
----------------------------------------
'main.py': Python script to execute data loading, cleaning, analysis, and visualization functions.
'employee_analysis.py': Python module containing functions for data loading, cleaning, analysis, and visualization.
'employees.csv': Sample CSV file containing employee data.

Requirements
----------------------------------------
Python 3.x
Libraries:
pandas
matplotlib
seaborn
plotly
(These can be installed via pip if not already installed: pip install pandas matplotlib seaborn plotly)


Usage
----------------------------------------
1. unzip project1_HR

2. Navigate to the project directing
	cd /path/to/project1_HR

3. install the required dependencies using pip. This step isn't needed if you have the required dependencies.
	pip install -r requirements.txt

4. open 'main.py' and change the file path to the location of the employee.csv file you want to analyze. Open 
	    file_path = '/path/to/employees.csv'  	

5. Run the analysis by executing the main.py script
	python main.py
   This script will import the employees.csv file, clean the data, and perform various analyses on the csv file choose.

6. View the generated outputs in the path you extraced the project to. The files created are 
	salary_distribution.png: Histogram showing salary distribution.
	average_salary_by_department.png: Bar chart displaying average salary by department.
	salary_vs_experience.png: Scatter plot depicting salary versus experience.
	age_distribution_by_department.png: Box plot illustrating age distribution by department.
