from company import Company
from employee import Employee
from file_loader import FileLoader
from subsidiary import Subsidiary


def build_company(company_name: str, data: dict) -> Company:
    """Build the entire company based on the json data we read.
    Loop through every item in the dict to create Subsidiary objects and Employee Objects

    Args:
        company_name (str): the name of the overall company
        data (dict): the whole data we read from the json file

    Returns:
        Company: the Company object, filled with all Subsidiary and Employee objects
    """
    company = Company(company_name)
    for subsidiary_name, employees_data in data.items():
        subsidiary = Subsidiary(subsidiary_name)
        for emp_data in employees_data:
            employee = Employee(
                name=emp_data["name"],
                job=emp_data["job"],
                hourly_rate=emp_data["hourly_rate"],
                weekly_hours=emp_data["weekly_hours_worked"],
                contract_hours=emp_data["contract_hours"],
            )
            subsidiary.add_employee(employee)
        company.add_subsidiary(subsidiary)
    return company


def print_formated_data(company: Company) -> None:
    """Loop through all the objects present in Company, print in a nice format by calling str and repr class method

    Args:
        company (Company): the Company object we created before, contains everything
    """
    for subsidiary in company._subsidiaries:
        print(str(subsidiary))  # Name of the subsidiary
        for employee in subsidiary._employees:
            print(str(employee))  # Name | Job | Monthly salary of the employee
        subsidiary.get_subsidiary_salary_stats()
        print(repr(subsidiary))  # Repr of the stats for the subsidiary
    company.get_company_salary_stats()
    print(repr(company))  # Repr of the stats for the whole company


def main() -> None:
    file_path = "employees_data.json"
    # Create a FileLoader object
    loader = FileLoader()
    # Open the json file, validate the data is correct, and then return it
    company_data = loader.load(file_path)
    # Build the whole Company object
    company = build_company("MyCompanyName", company_data)
    # Print the data
    print_formated_data(company)


if __name__ == "__main__":
    main()
