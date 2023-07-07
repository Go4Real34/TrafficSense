import pandas as pd
import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
import random
import matplotlib.pyplot as plt


def create_graphs():
    file_path = os.path.abspath(__file__)
    graph_creation_folder = file_path.rstrip("create_graphs.py").rstrip("\\")
    step_preparations_folder = graph_creation_folder.rstrip("StepCheckingFunctions").rstrip("\\")
    project_files_folder = step_preparations_folder.rstrip("StepPreparations").rstrip("\\")

    dataset_files_folder = os.path.join(project_files_folder, "DatasetFiles")

    dataset_path = os.path.join(dataset_files_folder, "dataset")
    csv_path = os.path.join(dataset_files_folder, "labels.csv")

    data = pd.read_csv(csv_path)
    traffic_sign_names_array = data.to_numpy()

    img_array = []
    class_no_array = []

    image_main_folder_path = os.listdir(dataset_path)
    no_of_classes = len(image_main_folder_path)

    past_images_length = 0
    for current_folder_no in range(0, no_of_classes):
        pics_in_folder_path = os.path.join(dataset_path, str(current_folder_no))
        pics_in_folder = os.listdir(pics_in_folder_path)

        for pic_name in pics_in_folder:
            curr_pic_path = os.path.join(pics_in_folder_path, pic_name)
            curr_pic = cv2.imread(curr_pic_path)

            img_array.append(curr_pic)
            class_no_array.append(current_folder_no)

        curr_images_length = len(img_array)
        data_diff = curr_images_length - past_images_length

        info = f"In folder {current_folder_no}: {data_diff} pictures found." \
               f"\t\tTotal Image Count: {curr_images_length}" \
               f"\t\tSign Name: {traffic_sign_names_array[current_folder_no][1]}"

        print(info)

        past_images_length = curr_images_length

    print(f"\n{len(img_array)} Images in {no_of_classes} Folders.")

    images = np.array(img_array)
    class_numbers = np.array(class_no_array)

    x_train, x_test, y_train, y_test = train_test_split(images, class_numbers, test_size=0.2)
    x_train, x_validation, y_train, y_validation = train_test_split(x_train, y_train, test_size=0.2)

    num_of_pics_in_each_folder = []
    col_count = 5
    num_of_classes = len(image_main_folder_path)

    fig, axs = plt.subplots(nrows=num_of_classes + 1, ncols=col_count, figsize=(5, 300))
    fig.tight_layout()

    for column in range(col_count):
        for row in range(0, no_of_classes):
            x_selected = x_train[y_train == row]

            axs[row][column].imshow(x_selected[random.randint(0, len(x_selected) - 1), :, :], cmap=plt.get_cmap("gray"))
            axs[row][column].axis("off")

            if column == 2:
                axs[row][column].set_title(str(row - 1) + "-" + traffic_sign_names_array[row - 1][1])
                num_of_pics_in_each_folder.append(len(x_selected))

                if row == 42:
                    axs[row+1][column].set_title(str(row) + "-" + traffic_sign_names_array[row][1])

    print("\nAvailable image instance count in folders for training (Indexes above, Counts below):")
    index_text = "[  0,    1,    2,   3,    4,    5,   6,   7,   8,   9,   10,  11,   12,   13,  " \
                 "14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,  27,  28,  29,  30,  31,  32,  " \
                 "33,  34,  35,  36,  37,   38,  39,  40,  41,  42]"

    print("         Indexes:", index_text)
    print("Number of Images:", num_of_pics_in_each_folder)

    plt.figure(figsize=(12, 4))
    plt.bar(range(0, num_of_classes), num_of_pics_in_each_folder)
    plt.title("Training Dataset in Folders")
    plt.xlabel("Index Number")
    plt.ylabel("Image Count")

    plt.show()


def main():
    return 0


if __name__ == "__main__":
    main()
