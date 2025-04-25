from pathlib import Path
from data_loader import load_employee_data
from data_visualizer import (
    plot_salary_vs_days_service,
    plot_salary_vs_age,
    plot_bonus_vs_performance,
    plot_days_service_vs_vacation,
    plot_salary_distribution
)

def main():
    """
    Main function to load data and generate visualizations.
    """
    # Resolve the path to the CSV file
    base_dir = Path(__file__).resolve().parent.parent  # Navigate to the project root
    file_path = base_dir / "data" / "employee_data_1_millon_sebastian_cardona.csv"
    
    # Load the data
    print("Loading data...")
    data = load_employee_data(file_path)
    
    # Generate visualizations
    print("Generating visualizations...")
    plot_salary_vs_days_service(data)
    plot_salary_vs_age(data)
    plot_bonus_vs_performance(data)
    plot_days_service_vs_vacation(data)
    plot_salary_distribution(data)
    print("All visualizations have been saved in the 'plots' directory.")

if __name__ == "__main__":
    main()