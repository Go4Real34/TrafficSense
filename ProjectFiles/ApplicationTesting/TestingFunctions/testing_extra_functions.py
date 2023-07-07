import os
import cv2


def handle_first_run(model_save_path, project_files_folder, application_testing_folder, icon_path):
    if not os.path.exists(model_save_path):
        print("No saved model detected.\n"
              "Please train or save a model first.\n")
        return False

    if not os.path.exists(icon_path):
        print("Window Icon file is missing.\n"
              f"'Please make sure that the icon file is in the following location: {icon_path}\n'.")
        return False

    photos_path = os.path.join(application_testing_folder, "Photos")
    if not os.path.exists(photos_path):
        os.chdir(application_testing_folder)
        os.mkdir("Photos")
        os.chdir(project_files_folder)

    return True


def get_menu_input():
    while True:
        option = input("Your choice: ")
        try:
            option = int(option)
            break

        except ValueError:
            print("\nPlease enter a valid option.")
            continue

    return option


def preprocess_image(image):
    grayed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(grayed)
    normalized = equalized / 255

    return normalized


def main():
    return 0


if __name__ == "__main__":
    main()
