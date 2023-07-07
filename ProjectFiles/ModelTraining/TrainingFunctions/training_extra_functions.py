import os
import subprocess
import time
import cv2
import tensorflow as tf


def get_device_from_file(device_type_file_path):
    with open(device_type_file_path, "r") as f:
        device_type = f.read()
    return device_type


def get_menu_input(valids):
    while True:
        option = input("Your choice: ")
        try:
            option = int(option)
            if option not in valids:
                print("\nPlease select a valid option.")
                continue

            else:
                return option

        except ValueError:
            print("\nPlease select a valid option.")
            continue

    return option


def handle_first_run(project_files_folder, dataset_files_folder):
    model_save_path = os.path.join(dataset_files_folder, "trained_model.h5")
    device_type_save_path = os.path.join(dataset_files_folder, "device_type.txt")
    pre_trained_cpu_model_path = os.path.join(dataset_files_folder, "pre_trained_cpu_model.h5")
    pre_trained_gpu_model_path = os.path.join(dataset_files_folder, "pre_trained_gpu_model.h5")

    if not os.path.exists(dataset_files_folder):
        print("DatasetFiles folder does not detected. Extracting DatasetFiles.rar in 5 seconds.\n")
        time.sleep(5)
        main_cwd = os.getcwd()
        os.chdir(project_files_folder)
        subprocess.run(["tar", "-xvf", "DatasetFiles.rar"])
        os.chdir(main_cwd)

        print("\nDatasetFiles.rar is extracted successfully.\n"
              "Pre-trained CPU & GPU models exists.\n"
              "Please select an option from the menu below:\n"
              "[1] - Use pre-trained CPU model.\n"
              "[2] - Use pre-trained GPU model.\n"
              "[0] - Don't use pre-trained model. I want to manually train it.\n")
        option = get_menu_input([1, 2, 0])

        if option == 1:
            os.remove(pre_trained_gpu_model_path)

            os.rename(pre_trained_cpu_model_path, model_save_path)
            with open(device_type_save_path, "w") as f:
                f.write("CPU")

            print("Pre-trained CPU trained model is successfully saved.\n")
            return True

        elif option == 2:
            os.remove(pre_trained_cpu_model_path)

            os.rename(pre_trained_gpu_model_path, model_save_path)
            with open(device_type_save_path, "w") as f:
                f.write("GPU")

            print("Pre-trained GPU trained model is successfully saved.\n")
            return True

        elif option == 0:
            os.remove(pre_trained_cpu_model_path)
            os.remove(pre_trained_gpu_model_path)

            print("Both pre-trained models are deleted.\n"
                  "Preparing files for training.\n")
            return False

    else:
        if os.path.exists(model_save_path) and os.path.exists(device_type_save_path):
            print("Saved model file and device type file are detected.\n"
                  "Continuing will delete the current files.\n"
                  "Do you want to exit or continue? (0/1)\n")
            option = get_menu_input([1, 0])

            if option == 0:
                print("\nSaved model file and device type file are not deleted.\n")
                return True

            elif option == 1:
                os.remove(model_save_path)
                os.remove(device_type_save_path)
                print("\nSaved model file and device type file are deleted.\n"
                      "Preparing files for training...\n")
                return False

        if os.path.exists(model_save_path) and not os.path.exists(device_type_save_path):
            os.remove(model_save_path)
            print("Model file detected but device type file does not detected.\n"
                  "Deleting the model file for preventing file corruption.\n"
                  "Preparing files for training...\n")
            return False

        if not os.path.exists(model_save_path) and os.path.exists(device_type_save_path):
            os.remove(device_type_save_path)
            print("Device type file detected but model file does not detected.\n"
                  "Deleting the device type file for preventing file corruption.\n"
                  "Preparing files for training...\n")
            return False

        if not os.path.exists(model_save_path) and not os.path.exists(device_type_save_path):
            print("Neither of the model file and device type file detected.\n"
                  "Preparing files for training...\n")
            return False


def check_model_device_compatibility(device_type_save_path):
    with open(device_type_save_path, "r", encoding="UTF-8") as f:
        device_type = f.read()

    if device_type == "GPU":
        gpu_list = tf.config.list_physical_devices("GPU")

        if len(gpu_list) == 0:
            print("This model is trained using NVIDIA CUDA supported GPU but, "
                  "there is no NVIDIA CUDA supported GPU detected on your system.\n"
                  "This model may not work as intended since it uses another type of source to run on, "
                  "resulting in wrong predictions.\n"
                  "Please be reminded that the CPU trained model works no matter what device you have.\n")

    return


def preprocess_image(image):
    grayed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(grayed)
    normalized = equalized / 255

    return normalized


def divide_with_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return int(quotient), int(remainder)


def time_printer(time_in_seconds):
    if time_in_seconds == 0:
        return "00:00:00:00 (Warning: An error could have occurred!)"

    second_in_milliseconds = 100
    minute_in_seconds = 60
    hour_in_minutes = 60

    milliseconds = round(time_in_seconds * second_in_milliseconds, 2)

    hour_in_milliseconds = hour_in_minutes * minute_in_seconds * second_in_milliseconds
    hours, milliseconds = divide_with_remainder(milliseconds, hour_in_milliseconds)

    minute_in_milliseconds = minute_in_seconds * second_in_milliseconds
    minutes, milliseconds = divide_with_remainder(milliseconds, minute_in_milliseconds)

    seconds, milliseconds = divide_with_remainder(milliseconds, second_in_milliseconds)

    time_text = ""

    time_text += f"{hours}:" if hours >= 10 else f"0{hours}:"
    time_text += f"{minutes}:" if minutes >= 10 else f"0{minutes}:"
    time_text += f"{seconds}:" if seconds >= 10 else f"0{seconds}:"
    time_text += f"{milliseconds}" if milliseconds >= 10 else f"0{milliseconds}"

    return time_text


def main():
    return 0


if __name__ == "__main__":
    main()