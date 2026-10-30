class Employee:
    """An employee at a subsidiary"""

    def __init__(
        self,
        name: str,
        job: str,
        hourly_rate: int,
        weekly_hours: int,
        contract_hours: int,
    ) -> None:
        """Init an employee

        Args:
            name: employee name.
            job: job title of the employee.
            hourly_rate: hourly wage, must be positive.
            hours_worked: weekly hours worked, must be zero or more.
            contract_hours: weekly contract hours, must be positive.
        """
        self.name = name
        self.job = job
        self.hourly_rate = hourly_rate
        self.weekly_hours = weekly_hours
        self.contract_hours = contract_hours
        self.monthly_salary = self.get_montly_salary()

    def get_montly_salary(self) -> float:
        """Get monthly salary for the employee, overtime is paid x1.5 of hourly_rate.
        Everything is computed per week, and then multiplied by 4 to get monthly salary.

        Returns:
            float: the average monthly salary, rounded to the 2nd decimal.
        """
        overtime_hours = max(0, self.weekly_hours - self.contract_hours)
        weekly_salary = (self.hourly_rate * self.weekly_hours) + (
            (self.hourly_rate * 0.5) * overtime_hours
        )
        return round((weekly_salary * 4), 2)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.name}\t\t| {self.job}\t | Monthly salary: {self.monthly_salary:.2f}€"
