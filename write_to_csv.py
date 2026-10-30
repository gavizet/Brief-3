import csv


def write_dict_to_csv(company) -> None:
    """Takes company data, and write it into two separate formated csv files
    wage_statistics.csv: contains data for each employee
    salary_stats.csv: contains salary stats for each company/subsidiary

    Args:
        company (Company): Company object we generated previously, contains all data about subsidiaries and employees.
    """
    # Open employee csv file with write rights
    with (
        open("wage_statistics.csv", "w", newline="") as employee_csv_file,
        open("salary_stats.csv", "w", newline="") as company_csv_file,
    ):
        # Create list of fieldnames for employee csv
        employee_fieldnames = [
            "employee_id",
            "subsidiary_name",
            "employee_name",
            "job",
            "monthly_salary",
        ]
        # Create the csv writer object with given fieldnames
        employee_writer = csv.DictWriter(
            employee_csv_file, fieldnames=employee_fieldnames
        )
        # Write header in employee csv file
        employee_writer.writeheader()
        employee_id = 0

        # Create list of fieldnames for company csv
        company_fieldnames = [
            "company_id",
            "name",
            "mean_salary",
            "max_salary",
            "min_salary",
        ]
        # Create the company csv writer object with given fieldnames
        company_writer = csv.DictWriter(company_csv_file, fieldnames=company_fieldnames)
        # Write heaer in company csv file
        company_writer.writeheader()
        # Write first row in salary_stats.csv based on company data
        company_writer.writerow(
            {
                "company_id": 0,
                "name": company.name,
                "mean_salary": company.mean_salary,
                "max_salary": company.highest_salary,
                "min_salary": company.lowest_salary,
            }
        )
        company_id = 1
        for subsidiary in company._subsidiaries:
            # Write row in salary_stats.csv file based on each subsidiary's data
            company_writer.writerow(
                {
                    "company_id": company_id,
                    "name": subsidiary.name,
                    "mean_salary": subsidiary.mean_salary,
                    "max_salary": subsidiary.highest_salary,
                    "min_salary": subsidiary.lowest_salary,
                }
            )
            company_id += 1
            for employee in subsidiary._employees:
                # Write row into the wage_statistics.csv file
                employee_writer.writerow(
                    {
                        "employee_id": employee_id,
                        "subsidiary_name": subsidiary.name,
                        "employee_name": employee.name,
                        "job": employee.job,
                        "monthly_salary": employee.monthly_salary,
                    }
                )
                # Increment employee ID, so it can be used as primary key / identifier for each employees, since they can have the same name, salary, etc
                employee_id += 1
