from employee import Employee


class Subsidiary:
    """Class for a company's subsidiary
    Subclass is Employee
    """

    """
    @staticmethod
    def __check_args(name, employees):
        if not isinstance(name, str):
            raise TypeError("Not a valid name for subsidiary, expected a string")
        if not isinstance(employees, list):
            raise TypeError("Not a valid list for subsidiary data")
        for empl in employees:
            if (
                not {
                    "name",
                    "job",
                    "hourly_rate",
                    "weekly_hours_worked",
                    "contract_hours",
                }
                <= empl.keys()
            )
                raise KeyError(f"Missing a key in the employee {empl}dictionary")
    """

    def __init__(self, name: str) -> None:
        """Init an empty subsidiary

        Args:
            name (str): the name of the subsidiary
        """
        self.name = name
        self._employees: list[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the subsidiary

        Args:
            employee (Employee): the object to add to the subsidiary

        Raises:
            TypeError: if the employee is not a Employee instance
        """
        if not isinstance(employee, Employee):
            raise TypeError(f"Expected an Employee, have {type(employee)} instead.")
        self._employees.append(employee)

    def get_subsidiary_salary_stats(self) -> None:
        """Gets all stats relevant for our subsidiary.
        Loops over all employees to get all salaries.
        Does a simple, mean, max and min over that data, sets class attributes accordingly
        """
        all_salaries = [employee.montly_salary for employee in self._employees]
        self.mean_salary = sum(all_salaries) / len(all_salaries)
        self.highest_salary = max(all_salaries)
        self.lowest_salary = min(all_salaries)

    def __str__(self):
        return f"Subsidiary: {self.name}\n"


"""
    def __repr__(self):
        return (
            f"\n===============================================\n\n"
            f"Salary statistics for subsidiary {self.name}:\n"
            f"Mean salary: {self.mean_salary:.2f}€\n"
            f"Highest salary: {self.highest_salary:.2f}€\n"
            f"Lowest salary: {self.lowest_salary:.2f}€\n\n"
            f"==============================================="
        )
    """
