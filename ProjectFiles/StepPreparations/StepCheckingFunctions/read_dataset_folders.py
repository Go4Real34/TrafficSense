import os
import cv2
import pandas as pd


def read_dataset_folders():
    file_path = os.path.abspath(__file__)
    read_csv_files_and_folders_folder = file_path.rstrip("read_dataset_folders.py").rstrip("\\")
    step_preparations_folder = read_csv_files_and_folders_folder.rstrip("StepCheckingFunctions").rstrip("\\")
    project_files_folder = step_preparations_folder.rstrip("StepPreparations").rstrip("\\")

    dataset_files_folder = os.path.join(project_files_folder, "DatasetFiles")
    dataset_path = os.path.join(dataset_files_folder, "dataset")
    csv_path = os.path.join(dataset_files_folder, "labels.csv")

    images_array = []
    class_no_array = []

    my_list_folders_array = os.listdir(dataset_path)
    no_of_classes = len(my_list_folders_array)
    print("Total folders detected: " + str(no_of_classes))

    print("Saving folder ingredients to memory...")

    folder_names = pd.read_csv(csv_path)
    name_and_no_of_signs = folder_names.to_numpy()

    past_images_length = 0
    num_of_pics_in_each_folder = []
    for current_folder_no in range(0, no_of_classes):
        my_pic_in_folder_path = os.path.join(dataset_path, str(current_folder_no))
        my_pic_list_in_curr_folder_array = os.listdir(my_pic_in_folder_path)

        for pic_file_name in my_pic_list_in_curr_folder_array:
            curr_pic_path = os.path.join(my_pic_in_folder_path, pic_file_name)
            curr_picture = cv2.imread(curr_pic_path)

            images_array.append(curr_picture)
            class_no_array.append(current_folder_no)

        curr_images_length = len(images_array)
        data_diff = curr_images_length - past_images_length

        info = f"In folder {current_folder_no}: {data_diff} pictures found." \
               f"\t\tTotal Image Count: {curr_images_length}" \
               f"\t\tSign Name: {name_and_no_of_signs[current_folder_no][1]}"

        print(info)

        num_of_pics_in_each_folder.append(data_diff)

        past_images_length = curr_images_length

    print(f"\n{len(images_array)} Images in {no_of_classes} Folders.")

    index_text = "[  0,    1,    2,    3,    4,    5,   6,    7,    8,    9,   10,   11,   12,   " \
                 "13,  14,  15,  16,  17,   18,  19,  20,  21,  22,  23,  24,   25,  26,  27,  28,  29,  30,  31,  " \
                 "32,  33,  34,   35,  36,  37,   38,  39,  40,  41,  42]"

    print("\nAvailable image instance count in folders in total (Indexes above, Counts below):")

    print("         Indexes:", index_text)
    print("Number of Images:", num_of_pics_in_each_folder)


def main():
    return 0


if __name__ == "__main__":
    main()
