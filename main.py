from file_loader import FileLoader


def main() -> None:
    file_path = "employees_data.json"
    loader = FileLoader()
    loader.load(file_path)


if __name__ == "__main__":
    main()
