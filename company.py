from subsidiary import Subsidiary


class Company:
    """Class for a company, made up of subclass Subsidiary

    Attributes:
        name: Name of the company.
        _subsidiaries: Protected list of the company's subsidiaries.
    """

    def __init__(self, name: str) -> None:
        """Init an empty company

        Args:
            name (str): name of the company
        """
        self.name = name
        self._subsidiaries: list[Subsidiary] = []

    def add_subsidiary(self, subsidiary: Subsidiary) -> None:
        """Add a subsidiary to the company

        Args:
            subsidiary (Subsidiary): the object to add to the company

        Raises:
            TypeError: if the subsidiary is not a Subsidiary instance
        """
        if not isinstance(subsidiary, Subsidiary):
            raise TypeError(f"Expected a Subsidiary, have {type(subsidiary)} instead.")
        self._subsidiaries.append(subsidiary)

    def get_company_salary_stats(self) -> None:
        """Gets all stats relevant for our company.
        Loops over all subsidiaries and employees to get all salaries.
        Does a simple, mean, max and min over that data, sets class attributes accordingly
        """
        all_salaries = [
            employee.montly_salary
            for subsidiary in self._subsidiaries
            for employee in subsidiary._employees
        ]
        self.mean_salary = sum(all_salaries) / len(all_salaries)
        self.highest_salary = max(all_salaries)
        self.lowest_salary = min(all_salaries)

    def __str__(self):
        return f"Company: {self.name}\n"

    def __repr__(self):
        return (
            f"\nOverall salary statistics for company {self.name}:\n"
            f"Mean salary: {self.mean_salary:.2f}€\n"
            f"Highest salary: {self.highest_salary:.2f}€\n"
            f"Lowest salary: {self.lowest_salary:.2f}€"
        )
