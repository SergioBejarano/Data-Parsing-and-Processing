import unittest
import pandas as pd
import os
from pathlib import Path
from scripts.data_visualizer import (
    plot_salary_vs_days_service,
    plot_salary_vs_age,
    plot_bonus_vs_performance,
    plot_days_service_vs_vacation,
    plot_salary_distribution
)

class TestDataVisualizer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up a temporary DataFrame and output directory for testing.
        """
        # Crear un DataFrame completo con todas las columnas necesarias
        cls.test_data = pd.DataFrame({
            'days_service': [100, 200, 300, 400, 500],
            'base_salary': [50000, 60000, 70000, 80000, 90000],
            'birth_date': ['1980-01-01', '1990-01-01', '1985-01-01', '1995-01-01', '2000-01-01'],
            'performance_score': [80, 85, 90, 95, 100],
            'bonus_percentage': [5, 10, 15, 20, 25],
            'vacation_days': [10, 15, 20, 25, 30],
            'gender': ['M', 'F', 'M', 'F', 'Other'],
            'department': ['IT', 'HR', 'Engineering', 'Sales', 'Marketing'],
            'job_title': ['Developer', 'HR Manager', 'Engineer', 'Sales Rep', 'Marketer']
        })
        cls.output_dir = Path("tests/plots")
        cls.output_dir.mkdir(parents=True, exist_ok=True)

    def test_plot_salary_vs_days_service(self):
        """
        Test the plot_salary_vs_days_service function.
        """
        plot_salary_vs_days_service(self.test_data, output_dir=self.output_dir)
        plot_path = self.output_dir / "salary_vs_days_service.png"
        self.assertTrue(plot_path.exists(), "The plot salary_vs_days_service.png was not created.")
        self.assertGreater(plot_path.stat().st_size, 0, "The plot file is empty.")

    def test_plot_salary_vs_age(self):
        """
        Test the plot_salary_vs_age function.
        """
        plot_salary_vs_age(self.test_data, output_dir=self.output_dir)
        plot_path = self.output_dir / "salary_vs_age.png"
        self.assertTrue(plot_path.exists(), "The plot salary_vs_age.png was not created.")
        self.assertGreater(plot_path.stat().st_size, 0, "The plot file is empty.")

    def test_plot_bonus_vs_performance(self):
        """
        Test the plot_bonus_vs_performance function.
        """
        plot_bonus_vs_performance(self.test_data, output_dir=self.output_dir)
        plot_path = self.output_dir / "bonus_vs_performance.png"
        self.assertTrue(plot_path.exists(), "The plot bonus_vs_performance.png was not created.")
        self.assertGreater(plot_path.stat().st_size, 0, "The plot file is empty.")

    def test_plot_days_service_vs_vacation(self):
        """
        Test the plot_days_service_vs_vacation function.
        """
        plot_days_service_vs_vacation(self.test_data, output_dir=self.output_dir)
        plot_path = self.output_dir / "days_service_vs_vacation.png"
        self.assertTrue(plot_path.exists(), "The plot days_service_vs_vacation.png was not created.")
        self.assertGreater(plot_path.stat().st_size, 0, "The plot file is empty.")

    def test_plot_salary_distribution(self):
        """
        Test the plot_salary_distribution function.
        """
        plot_salary_distribution(self.test_data, output_dir=self.output_dir)
        plot_path = self.output_dir / "salary_distribution.png"
        self.assertTrue(plot_path.exists(), "The plot salary_distribution.png was not created.")
        self.assertGreater(plot_path.stat().st_size, 0, "The plot file is empty.")

    @classmethod
    def tearDownClass(cls):
        """
        Clean up the generated plots after tests.
        """
        for file in cls.output_dir.iterdir():
            file.unlink()
        cls.output_dir.rmdir()

if __name__ == "__main__":
    unittest.main()