import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def ensure_plot_directory(directory="plots"):
    """
    Ensure that the directory for saving plots exists.

    Args:
        directory (str): Path to the directory.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def plot_salary_vs_days_service(data, output_dir="plots"):
    """
    Plot the relationship between salary and days of service.

    Args:
        data (pd.DataFrame): The employee data.
        output_dir (str): Directory to save the plot.
    """
    ensure_plot_directory(output_dir)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='days_service', y='base_salary', data=data, alpha=0.6, color='purple')
    plt.title("Salary vs. Days of Service", fontsize=16)
    plt.xlabel("Days of Service", fontsize=12)
    plt.ylabel("Base Salary", fontsize=12)
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "salary_vs_days_service.png"))
    plt.close()

def plot_salary_vs_age(data, output_dir="plots"):
    """
    Plot the relationship between salary and age.

    Args:
        data (pd.DataFrame): The employee data.
        output_dir (str): Directory to save the plot.
    """
    ensure_plot_directory(output_dir)
    data['age'] = pd.to_datetime('today').year - pd.to_datetime(data['birth_date']).dt.year
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='age', y='base_salary', data=data, alpha=0.6, color='blue')
    plt.title("Salary vs. Age", fontsize=16)
    plt.xlabel("Age", fontsize=12)
    plt.ylabel("Base Salary", fontsize=12)
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "salary_vs_age.png"))
    plt.close()

def plot_bonus_vs_performance(data, output_dir="plots"):
    """
    Plot the relationship between bonus percentage and performance score.

    Args:
        data (pd.DataFrame): The employee data.
        output_dir (str): Directory to save the plot.
    """
    ensure_plot_directory(output_dir)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='performance_score', y='bonus_percentage', data=data, alpha=0.6, color='green')
    plt.title("Bonus Percentage vs. Performance Score", fontsize=16)
    plt.xlabel("Performance Score", fontsize=12)
    plt.ylabel("Bonus Percentage", fontsize=12)
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "bonus_vs_performance.png"))
    plt.close()


def plot_days_service_vs_vacation(data, output_dir="plots"):
    """
    Plot the relationship between days of service and vacation days.

    Args:
        data (pd.DataFrame): The employee data.
        output_dir (str): Directory to save the plot.
    """
    ensure_plot_directory(output_dir)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='days_service', y='vacation_days', data=data, alpha=0.6, color='orange')
    plt.title("Days of Service vs. Vacation Days", fontsize=16)
    plt.xlabel("Days of Service", fontsize=12)
    plt.ylabel("Vacation Days", fontsize=12)
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "days_service_vs_vacation.png"))
    plt.close()

def plot_salary_distribution(data, output_dir="plots"):
    """
    Plot the distribution of employee salaries.

    Args:
        data (pd.DataFrame): The employee data.
        output_dir (str): Directory to save the plot.
    """
    ensure_plot_directory(output_dir)
    plt.figure(figsize=(10, 6))
    sns.histplot(data['base_salary'], kde=True, color='blue', bins=50)
    plt.title("Salary Distribution", fontsize=16)
    plt.xlabel("Base Salary", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "salary_distribution.png"))
    plt.close()