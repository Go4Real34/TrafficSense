import os
import sys
import subprocess

from ProjectFiles.ModelTraining.TrainingFunctions.training_extra_functions import get_menu_input


def main():
    print("Please select a option.\n"
          "[1] - Check Steps\n"
          "[2] - Start Training\n"
          "[3] - Test Application\n"
          "[0] - Exit\n")

    option = get_menu_input([1, 2, 3, 0])

    current_cwd = os.getcwd()
    python_interpreter = sys.executable
    script_path = os.path.join(current_cwd, "ProjectFiles")

    if option == 1:
        script_path = os.path.join(script_path, "StepPreparations")
        script_path = os.path.join(script_path, "check_steps.py")

    elif option == 2:
        script_path = os.path.join(script_path, "ModelTraining")
        script_path = os.path.join(script_path, "train_model.py")

    elif option == 3:
        script_path = os.path.join(script_path, "ApplicationTesting")
        script_path = os.path.join(script_path, "test_model.py")

    elif option == 0:
        print("Exiting...")
        return 0

    subprocess.run([python_interpreter, script_path])


if __name__ == "__main__":
    main()