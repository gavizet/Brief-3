import csv
# employee_wages.csv
# employee_id, name, job, monthly_salary

# salary_stats.csv
# name, employee_count, mean_salary, highest_salary, lowest_salary


def write_dict_to_csv(data) -> None:
    with open("wage_statistics.csv", "w", newline="") as csvfile:
        fieldnames = ["employee_id", "name", "job", "monthly_salary"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        # Do I check data types before writing ? Think it has no value here, shoudl be checked when we read/store the JSON input data
        # Exemple row
        writer.writerow(
            {"id": 1, "name": "test_name", "job": "pleb", "monthly_salary": 1234.56}
        )
