import os
import time
import subprocess

from ProjectFiles.StepPreparations.CheckingSteps import detect_camera, process_images, read_dataset_csv_file, \
    read_dataset_folders, create_graphs


def main():
    done_and_passed = {
        "done": [False, False, False, False, False],
        "pass": [False, False, False, False, False]
    }

    file_path = os.path.abspath(__file__)
    step_preparations_folder = file_path.rstrip("check_steps.py").rstrip("\\")
    project_files_folder = step_preparations_folder.rstrip("StepPreparations").rstrip("\\")
    dataset_files_folder = os.path.join(project_files_folder, "DatasetFiles")

    original_cwd = os.getcwd()
    if not os.path.exists(dataset_files_folder):
        print("DatasetFiles folder does not found. Extracting DatasetFiles.rar in 5 seconds.")
        time.sleep(5)

        os.chdir(project_files_folder)
        subprocess.run(["tar", "-xvf", "DatasetFiles.rar"])
        os.chdir(original_cwd)

    while True:
        print("\nSelect the step you want to check.")
        print("[1] - Detect Camera")
        print("[2] - Process Images")
        print("[3] - Read CSV File")
        print("[4] - Read Folders")
        print("[5] - Create Graphs")
        print("[-1] - Show Current Check Status")
        print("[0] - Exit")

        while True:
            option = input("Your choice: ")
            try:
                option = int(option)
                if option not in [1, 2, 3, 4, 5, -1, 0]:
                    print("\nPlease select a valid option.")
                    continue
                else:
                    print()
                    break
            except ValueError:
                print("\nPlease enter a valid number.")
                continue

        if option == 1:
            detect_camera.detect_camera()
            if not done_and_passed["done"][0]:
                done_and_passed["done"][0] = True
            if not done_and_passed["pass"][0]:
                done_and_passed["pass"][0] = True
            print(f"\nPassed Detect Camera Test: {done_and_passed['pass'][0]}")

        elif option == 2:
            process_images.process_images()

            if not done_and_passed["done"][1]:
                done_and_passed["done"][1] = True
            if not done_and_passed["pass"][1]:
                done_and_passed["pass"][1] = True

            print(f"\nPassed Process Images Test: {done_and_passed['pass'][1]}")

        elif option == 3:
            read_dataset_csv_file.read_dataset_csv_file()

            if not done_and_passed["done"][2]:
                done_and_passed["done"][2] = True
            if not done_and_passed["pass"][2]:
                done_and_passed["pass"][2] = True
            print(f"\nPassed Read Dataset CSV File Test: {done_and_passed['pass'][2]}")

        elif option == 4:
            read_dataset_folders.read_dataset_folders()

            if not done_and_passed["done"][3]:
                done_and_passed["done"][3] = True
            if not done_and_passed["pass"][3]:
                done_and_passed["pass"][3] = True
            print(f"\nPassed Read Dataset Folders Test: {done_and_passed['pass'][3]}")

        elif option == 5:
            create_graphs.create_graphs()

            if not done_and_passed["done"][4]:
                done_and_passed["done"][4] = True
            if not done_and_passed["pass"][4]:
                done_and_passed["pass"][4] = True
            print(f"\nPassed Create Graphs Test: {done_and_passed['pass'][4]}")

        elif option in [-1, 0]:
            if option == 0:
                if done_and_passed['done'].count(False) > 0 and done_and_passed['pass'].count(False) > 0:
                    print("\nYou still had some test either not done or not passed.")

            print(f"Done Detect Camera Test: {done_and_passed['done'][0]}"
                  f"\tPassed Detect Camera Test: {done_and_passed['pass'][0]}")

            print(f"Done Process Images Test: {done_and_passed['done'][1]}"
                  f"\tPassed Process Images Test: {done_and_passed['pass'][1]}")

            print(f"Done Read CSV File Test: {done_and_passed['done'][2]}"
                  f"\tPassed Read CSV File Test: {done_and_passed['pass'][2]}")

            print(f"Done Read Folders Test: {done_and_passed['done'][3]}"
                  f"\tPassed Read Folders Test: {done_and_passed['pass'][3]}")

            print(f"Done Create Graphs Test: {done_and_passed['done'][4]}"
                  f"\tPassed Create Graphs Test: {done_and_passed['pass'][4]}")

            print(f"\nDone Tests: {done_and_passed['done'].count(True)}/{len(done_and_passed['done'])} "
                  f"({round((done_and_passed['done'].count(True) / len(done_and_passed['done'])) * 100, 2)}%)"

                  f"\tPassed Tests: {done_and_passed['pass'].count(True)}/{len(done_and_passed['pass'])} "
                  f"({round((done_and_passed['pass'].count(True) / len(done_and_passed['pass'])) * 100, 2)}%)")

            if option == 0:
                print("\nExiting from checking system.")
                break

        if all([all(done_and_passed["done"]), all(done_and_passed["pass"])]):
            print("\nAll steps are done and passed.")
            print("\nExiting from the checking system.")
            break


if __name__ == "__main__":
    main()
