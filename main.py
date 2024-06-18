import pandas as pd
from employee_analysis import (
    load_data, clean_data, calculate_average_salary,
    find_employees_with_experience, get_department_statistics,
    plot_salary_distribution, plot_average_salary_by_department,
    plot_salary_vs_experience, plot_age_distribution_by_department
)

if __name__ == "__main__":
    file_path = './employees.csv'  # Updated file path
    
    #Task1
    # Load and clean data
    df = load_data(file_path)
    print("dataframe withouting cleaning")
    print(df.head())
    print()

    cleaned_df = clean_data(df)
    print("cleaned dataframe")
    print(cleaned_df.head())
    print()

    #Task2
    # Calculate average salary for IT department
    average_salary_it = calculate_average_salary(cleaned_df, 'IT')
    print(f"Average salary in IT department: {average_salary_it}")
    print()

    # Find employees with more than 5 years of experience
    experienced_employees = find_employees_with_experience(cleaned_df, 5)
    print(f"Employees with more than 5 years of experience: {experienced_employees}")
    print()

    #Task3
    # Get department statistics
    department_stats = get_department_statistics(cleaned_df)
    print(f"Department statistics: {department_stats}")
    print()

    #Task4
    # Plot salary distribution
    plot_salary_distribution(cleaned_df)
    
    # Plot average salary by department
    plot_average_salary_by_department(cleaned_df)
    
    #Task5
    # Plot salary vs. experience
    plot_salary_vs_experience(cleaned_df)
    
    # Plot age distribution by department
    plot_age_distribution_by_department(cleaned_df)
    