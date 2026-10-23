import json
from json import JSONDecodeError
from subsidiary import Subsidiary


class FileLoader:
    """Loads and displays a pandas dataframe"""

    def __init__(self):
        pass

    @staticmethod
    def load(path: str) -> None:
        try:
            with open(path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
            if isinstance(data, dict):
                all_subsidiaries = []
                print("Top-level keys:", list(data.keys()))
                for subsidiary, employees in data.items():
                    all_subsidiaries.append(Subsidiary(subsidiary, employees))
            elif isinstance(data, list):
                print("Top-level list length:", len(data))
        except (FileNotFoundError, ValueError) as error:
            print(f"File not found: {error}")
        except JSONDecodeError as e:
            print("Invalid JSON.")
            print(f"Line {e.lineno}, column {e.colno}: {e.msg}")
        else:
            print("Loaded JSON successfully.")

    @staticmethod
    def display(dataframe) -> None:
        """Dispays a json dataset passed as argument

        Args:
            dataframe (): a json dataset
        """
        if not isinstance(dataframe, dict):
            print("Not a valid dataframe, expected a dictionary")
        else:
            print(
                f"Data set of type: {type(dataframe)}, of top level length: {len(dataframe)}"
            )
            print(dataframe)


def tests():
    """Some simples tests for FileLoader class"""
    loader = FileLoader()
    print("==== TEST LOADER ====")
    print("--- Does not exist test ---")
    data = loader.load("does_not_exist.csv")
    print("--- Random string test ---")
    data = loader.load("lol")
    print("--- Valid CSV test ---")
    data = loader.load("employees_data.json")
    print()

    print("==== TEST DISPLAY ====")
    loader.display(data)


if __name__ == "__main__":
    tests()
