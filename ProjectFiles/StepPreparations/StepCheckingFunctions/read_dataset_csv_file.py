import os
import pandas as pd


def read_dataset_csv_file():
    file_path = os.path.abspath(__file__)
    read_csv_files_and_folders_folder = file_path.rstrip("read_dataset_csv_file.py").rstrip("\\")
    step_preparations_folder = read_csv_files_and_folders_folder.rstrip("StepCheckingFunctions").rstrip("\\")
    project_files_folder = step_preparations_folder.rstrip("StepPreparations").rstrip("\\")

    dataset_files_folder = os.path.join(project_files_folder, "DatasetFiles")
    csv_path = os.path.join(dataset_files_folder, "labels.csv")

    data = pd.read_csv(csv_path)
    print(f"Read File Type: {type(data)}")
    print("Data inside of the file: ")
    print(data, end="\n" * 2)

    file_array = data.to_numpy()
    print("Printing file as an array:")
    for ri, row in enumerate(file_array):
        for ci, column in enumerate(row):
            if ci != len(row) - 1:
                print(column, end=", ")
            else:
                print(column, end=".\t\t\t\tend_of_row")

        print("", end="\n")


def main():
    return 0


if __name__ == "__main__":
    main()
