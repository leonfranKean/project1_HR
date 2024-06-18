import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data(file_path):
    columns = ['EmployeeID', 'FirstName', 'LastName', 'Department', 'DateOfHire', 'Salary', 'EmploymentType']
    
    df = pd.read_csv(file_path, names=columns, header=None)
    
    return df

def clean_data(df):
    
    # Combine first and last name into a single column with a single space between them
    df['Name'] = df['FirstName'].str.strip() + ' ' + df['LastName'].str.strip()
    
    # Select the required columns
    required_columns = ['EmployeeID', 'Name', 'DateOfHire', 'Department', 'Salary']
    df = df[required_columns].copy()
    
    # Convert Salary to numeric
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    
    # Convert DateOfHire to datetime
    df['DateOfHire'] = pd.to_datetime(df['DateOfHire'], errors='coerce')
    
    # Strip leading/trailing spaces from Department names
    df['Department'] = df['Department'].str.strip().str.upper()

    # Drop rows with any missing values
    df = df.dropna()
    
    # Calculate Experience as the number of years since DateOfHire
    current_date = pd.to_datetime('today')
    df['Experience'] = (current_date - df['DateOfHire']).dt.days / 365.25
    
    return df

def calculate_average_salary(df, department):
    department_df = df[df['Department'].str.lower() == department.lower().strip()]
    average_salary = department_df['Salary'].mean()
    return average_salary

def find_employees_with_experience(df, years):
    experienced_employees_df = df[df['Experience'] >= years]
    employee_names = experienced_employees_df['Name'].tolist()
    return employee_names

def get_department_statistics(df):
    departments = df['Department'].unique()
    stats = {}
    
    for department in departments:
        department_df = df[df['Department'] == department]
        average_salary = department_df['Salary'].mean()
        average_experience = department_df['Experience'].mean()
        stats[department] = {
            'Average Salary': average_salary,
            'Average Age': average_experience
        }
    return stats


def plot_salary_distribution(df):

    plt.figure(figsize=(14, 8))  
    plt.hist(df['Salary'], bins=30, edgecolor='black')  
    plt.title('Salary Distribution')
    plt.xlabel('Salary')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig('salary_distribution.png')
    plt.show()

def plot_average_salary_by_department(df):

    # Calculate average salary by department
    average_salary_by_department = df.groupby('Department')['Salary'].mean().sort_values()

    # Plot the bar chart
    plt.figure(figsize=(14, 8))  # Adjusted figure size to 14 inches by 8 inches
    average_salary_by_department.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Average Salary by Department')
    plt.xlabel('Department')
    plt.ylabel('Average Salary')
    plt.xticks(rotation=45)
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.savefig('average_salary_by_department.png')
    plt.show()

def plot_salary_vs_experience(df):
    plt.figure(figsize=(14, 8))  
    sns.scatterplot(data=df, x='Experience', y='Salary', hue='Department', palette='deep', s=100, edgecolor='black')
    plt.title('Salary vs. Experience')
    plt.xlabel('Experience (Years)')
    plt.ylabel('Salary')
    plt.grid(True)
    
    # Save the plot
    plt.savefig('salary_vs_experience.png')
    plt.show()

def plot_age_distribution_by_department(df):
    # Create the box plot
    fig = px.box(df, x='Department', y='Experience', title='Age Distribution by Department',
                 labels={'Experience': 'Experience (Years)'}, points="all")

    fig.update_layout(
        xaxis_title="Department",
        yaxis_title="Experience (Years)",
        title="Age Distribution by Department",
        showlegend=False
    )
    
    fig.write_image("age_distribution_by_department.png")
    fig.show()

