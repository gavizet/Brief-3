class Subsidiary:
    """
    Class for a company's subsidiary
    Subclass is Employee
    """

    def __init__(self, name: str, employees: list[dict]) -> None:
        self.name = name
        self.employee_num = len(employees)
        print(f"{name}: {self.employee_num} employees")
        self.mean_salary = self.get_mean_salary(employees)
        self.highest_salary = self.get_highest_salary(employees)
        self.lowest_salary = self.get_lowest_salary(employees)

    """
    def _is_valid_dict(function):
        def wrapper(self, employees, *args, **kwargs):
            #Wrapper function for our _is_valid_dict decorator
            #Make sure the dict passed to our method is valid
            if not isinstance(employees, list):
                print("Not a valid list for subsidiary data")
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
                ):
                    print("coucou")
                    return KeyError(f"Missing a key in the employee {empl}dictionary")
            result = function(self, employees, *args, **kwargs)
            return result
        return wrapper
    """

    # @_is_valid_dict
    def get_mean_salary(self, employees) -> float:
        pass

    # @_is_valid_dict
    def get_highest_salary(self, employees) -> float:
        pass

    # @_is_valid_dict
    def get_lowest_salary(self, employees) -> float:
        pass

    # @_is_valid_dict
    def print_subsidiary_data(self, employees) -> None:
        pass
