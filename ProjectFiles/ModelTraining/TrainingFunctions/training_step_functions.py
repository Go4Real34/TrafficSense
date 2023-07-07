import pandas as pd
import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random
from keras.preprocessing.image import ImageDataGenerator
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers import Dropout, Flatten, Dense
from keras.optimizers import Adam
import tensorflow as tf
from tensorflow.python.client import device_lib
import math
import time

from .training_extra_functions import preprocess_image, get_menu_input, time_printer


def read_csv(file_path):
    print("--- Step 1: Reading CSV File ---\n")

    data = pd.read_csv(file_path)
    data_array = data.to_numpy()

    print(f"Read CSV Data Shape: {data.shape}, Type: {type(data)}")
    print(f"Read Data Array Shape: {data_array.shape}, Type: {type(data_array)}\n")

    print("--- Step 1: Reading Complete ---\n")
    return data, data_array


def read_dataset_images(dataset_path, data_array):
    print("--- Step 2: Reading Dataset Images ---\n")

    folder_list = os.listdir(dataset_path)
    number_of_folders = len(folder_list)

    print(f"Total of {number_of_folders} folders detected.")
    print("Saving images in folders for training.")

    images = []
    classes = []

    for folder_ID in range(number_of_folders):
        image_count_in_current_folder = 0

        current_folder_abs_path = os.path.join(dataset_path, str(folder_ID))
        current_folder_images = os.listdir(current_folder_abs_path)

        for image_name in current_folder_images:
            current_image_abs_path = os.path.join(current_folder_abs_path, image_name)
            current_image_data = cv2.imread(current_image_abs_path)

            images.append(current_image_data)
            classes.append(folder_ID)

            image_count_in_current_folder += 1

        print(f"Reading Folder: {folder_ID}\t" +
              f"Images Found: {image_count_in_current_folder}\t" +
              f"Total Images Found: {len(images)}\t" +
              (f"\t" if folder_ID < 1 else "") +
              f"Class Name: {data_array[folder_ID][1]}")

    print(f"Summary: Total of {len(images)} images found in {number_of_folders} folders.\n")

    print("--- Step 2: Reading Complete ---\n")
    return np.array(images), np.array(classes)


def split_dataset(images, classes, test_ratio, validation_ratio):
    print("--- Step 3: Splitting Dataset into Training, Testing and Validation Sets ---")

    x_train, x_test, y_train, y_test = train_test_split(images, classes, test_size=test_ratio)
    x_train, x_validation, y_train, y_validation = train_test_split(x_train, y_train, test_size=validation_ratio)

    print("--- Step 3: Splitting Complete ---\n")
    return x_train, x_test, x_validation, y_train, y_test, y_validation


def check_compatibility(x_train, x_test, x_validation, y_train, y_test, y_validation, image_dimensions):
    print("--- Step 4: Checking Compatibility ---\n")

    error_detected = False

    print("Image Count Control of x_train\n"
          f"\t\t\tx_train.shape[0]: {x_train.shape[0]}\n"
          f"  REQUIRED: y_train.shape[0]: {y_train.shape[0]}")
    if x_train.shape[0] != y_train.shape[0]:
        print("COMPATIBILITY ISSUE DETECTED: "
              "The number of images is not equal to number of labels in the training set.\n"
              "\t\t\t\t\t  Result: ERROR\n")
        error_detected = True
    else:
        print("\t\t\t\t\t  Result: OK\n")

    print("Image Dimension Control of x_train\n"
          f"\t\t   x_train.shape[1:]: {x_train.shape[1:]}\n"
          f"  REQUIRED: Image Dimensions: {image_dimensions}")
    if x_train.shape[1:] != image_dimensions:
        print("COMPATIBILITY ISSUE DETECTED: "
              "The dimensions of the training images are not compatible with the required image dimension.\n"
              "\t\t\t\t\t  Result: ERROR\n")
        error_detected = True
    else:
        print("\t\t\t\t\t  Result: OK\n")

    print("Image Count Control of x_validation\n"
          f"\t\t\tX_validation.shape[0]: {x_validation.shape[0]}\n"
          f"  REQUIRED: y_validation.shape[0]: {y_validation.shape[0]}")
    if x_validation.shape[0] != y_validation.shape[0]:
        print("COMPATIBILITY ISSUE DETECTED: "
              "The number of images is not equal to the number of labels in validation set.\n"
              "\t\t\t\t\t\t   Result: ERROR\n")
    else:
        print("\t\t\t\t\t\t   Result: OK\n")

    print("Image Dimension Control of x_validation\n"
          f"\t\t   x_validation.shape[1:]: {x_validation.shape[1:]}\n"
          f"\t   REQUIRED: Image Dimensions: {image_dimensions}")
    if x_validation.shape[1:] != image_dimensions:
        print("COMPATIBILITY ISSUE DETECTED: "
              "The dimensions of the validation images are not compatible with the required image dimension.\n"
              "\t\t\t\t\t\t  Result: ERROR\n")
    else:
        print("\t\t\t\t\t\t  Result: OK\n")

    print("Image Count Control of x_test\n"
          f"\t\t\t    x_test.shape[0]: {x_test.shape[0]}\n"
          f"\t  REQUIRED: y_test.shape[0]: {y_test.shape[0]}")
    if x_test.shape[0] != y_test.shape[0]:
        print("COMPATIBILITY ISSUE DETECTED: "
              "The number of images is not equal to the number of labels in the test set.\n"
              "\t\t\t\t\t\t Result: ERROR\n")
    else:
        print("\t\t\t\t\t\t Result: OK\n")

    print("Image Dimension Control of x_test\n"
          f"\t\t   x_test.shape[1:]: {x_test.shape[1:]}\n"
          f" REQUIRED: Image Dimensions: {image_dimensions}")
    if x_test.shape[1:] != image_dimensions:
        print("COMPATIBILITY ISSUE DETECTED: "
              "The dimensions of the test images are not compatible with the required image dimension.\n"
              "\t\t\t\t\t Result: ERROR\n")
    else:
        print("\t\t\t\t\t Result: OK\n")

    print("--- Step 4: Checking Complete ---\n")
    return error_detected


def show_dataset_examples_for_each_class(number_of_classes, columns, figure_size, data_array, x_train, y_train):
    print("--- Step 5: Showing Dataset Examples ---\n")
    number_of_images_in_each_folder = []
    figure, axis = plt.subplots(
        num="Example Images from Dataset", nrows=number_of_classes + 1, ncols=columns, figsize=figure_size
    )
    for column in range(columns):
        for row, name in data_array:
            x_selected = x_train[y_train == row]

            random_image = x_selected[random.randint(0, len(x_selected) - 1), :, :]
            axis[row][column].imshow(random_image, cmap=plt.get_cmap("gray"))
            axis[row][column].axis("off")

            if column == 2:
                axis[row][column].set_title(f"{row - 1} - {data_array[row - 1][1]}")
                number_of_images_in_each_folder.append(len(x_selected))

                if row == 42:
                    axis[row + 1][column].set_title(f"{row} - {data_array[row][1]}")

    index_text = "[  0,    1,    2,   3,    4,    5,   6,   7,   8,   9,   10,  11,   12,   13,  " \
                 "14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,  27,  28,  29,  30,  31,  32,  " \
                 "33,  34,  35,  36,  37,   38,  39,  40,  41,  42]"

    print("Available number of images for each class for training:")
    print(f"         Indexes: {index_text}")
    print(f"Number of Images: {number_of_images_in_each_folder}\n")

    figure.tight_layout()
    plt.title("Example Images from Dataset for Each Class")
    plt.show()

    print("--- Step 5: Showing Dataset Examples Complete ---\n")
    return number_of_images_in_each_folder


def show_dataset_training_distribution(figure_size, number_of_classes, number_of_images_in_each_folder):
    print("--- Step 6: Showing Dataset Training Distribution ---")

    plt.figure(num="Dataset Distribution", figsize=figure_size)
    plt.bar(range(number_of_classes), number_of_images_in_each_folder)
    plt.title("Distribution of the Dataset")
    plt.xlabel("Class Number")
    plt.ylabel("Number of Images")
    plt.show()

    print("--- Step 6: Showing Dataset Training Distribution Complete ---\n")
    return


def process_dataset_images(x_train, x_validation, x_test):
    print("--- Step 7: Processing Dataset Images ---")

    x_train = np.array(list(map(preprocess_image, x_train)))
    x_validation = np.array(list(map(preprocess_image, x_validation)))
    x_test = np.array(list(map(preprocess_image, x_test)))

    print("--- Step 7: Processing Dataset Images Complete ---\n")
    return x_train, x_validation, x_test


def show_processed_image_example(figure_size, processed_images_array, classes, names):
    print("--- Step 8: Showing Processed Image Example ---")

    plt.figure(num="Processed Image Example", figsize=figure_size)
    random_index = random.randint(0, len(processed_images_array) - 1)
    random_processed_image = processed_images_array[random_index]
    image_class_number = classes[random_index]
    image_class_name = names[image_class_number]
    plt.imshow(random_processed_image)
    plt.title(f"Class: {image_class_number}, Name: {image_class_name}")
    plt.axis("off")
    plt.show()

    print("--- Step 8: Showing Processed Image Example Complete ---\n")
    return


def add_depth_to_images(x_train, x_validation, x_test):
    print("--- Step 9: Adding Depth to Images ---\n")

    x_train_depth = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1)
    x_validation_depth = x_validation.reshape(x_validation.shape[0], x_validation.shape[1], x_validation.shape[2], 1)
    x_test_depth = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)

    print(f"x_train_depth.shape: {x_train_depth.shape}\n")

    print("--- Step 9: Adding Depth to Images Complete ---\n")
    return x_train_depth, x_validation_depth, x_test_depth


def augment_images(width_shift, height_shift, zoom, shear, rotation, x_train, y_train, batch_size):
    print("--- Step 10: Augmenting Images ---")

    data_generator = ImageDataGenerator(
        width_shift_range=width_shift,
        height_shift_range=height_shift,
        zoom_range=zoom,
        shear_range=shear,
        rotation_range=rotation,
    )

    data_generator.fit(x_train)
    batches = data_generator.flow(x_train, y_train, batch_size=batch_size)

    print("--- Step 10: Augmenting Images Complete ---\n")
    return batches, data_generator


def show_augmented_image_examples(rows, columns, figure_size, font_size, x_batch, image_dimensions):
    print("--- Step 11: Showing Augmented Image Examples ---")

    figure, axis = plt.subplots(num="Augmented Image Examples", nrows=rows, ncols=columns, figsize=figure_size)
    figure.suptitle("Some Example of a Batch of Augmented Images", fontsize=font_size)
    figure.tight_layout()

    for i in range(columns):
        axis[i].imshow(x_batch[i].reshape(image_dimensions[0], image_dimensions[1]))
        axis[i].axis("off")

    plt.show()

    print("--- Step 11: Showing Augmented Image Examples Complete ---\n")
    return


def categorize_class_ids(y_train, y_validation, y_test, number_of_classes):
    print("--- Step 12: Categorizing Class IDs ---")

    y_train = to_categorical(y_train, number_of_classes)
    y_validation = to_categorical(y_validation, number_of_classes)
    y_test = to_categorical(y_test, number_of_classes)

    print("--- Step 12: Categorizing Class IDs Complete ---\n")
    return y_train, y_validation, y_test


def create_model(number_of_filters, size_of_filter_for_first_2d_layers, size_of_filter_for_second_2d_layers,
                 size_of_pool, number_of_nodes, image_dimensions, number_of_classes):
    print("--- Step 13: Creating Model ---\n")
    model = Sequential()
    model.add(
        Conv2D(
            number_of_filters, size_of_filter_for_first_2d_layers,
            input_shape=(image_dimensions[0], image_dimensions[1], 1), activation="relu"
        )
    )
    model.add(Conv2D(number_of_filters, size_of_filter_for_second_2d_layers, activation="relu"))
    model.add(MaxPooling2D(pool_size=size_of_pool))

    model.add(Conv2D(number_of_filters // 2, size_of_filter_for_second_2d_layers, activation="relu"))
    model.add(Conv2D(number_of_filters // 2, size_of_filter_for_second_2d_layers, activation="relu"))
    model.add(MaxPooling2D(pool_size=size_of_pool))
    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(number_of_nodes, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(number_of_classes, activation="softmax"))

    model.compile(Adam(learning_rate=0.001), loss="categorical_crossentropy", metrics=["accuracy"])
    print(f"{model.summary()}\n")
    print("--- Step 13: Creating Model Complete ---\n")

    return model


def get_selected_device_to_train():
    print("--- Step 14: Detecting Devices to Select Device to Train ---\n")

    gpus = tf.config.list_physical_devices("GPU")
    if len(gpus) == 0:
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

        print("No NVIDIA CUDA supported GPU detected or installation not completed on your system.\n"
              "Training will be performed on CPU.\n")

        print("--- Step 14: Getting Selected Device to Train Complete ---\n")
        return "CPU", 0

    else:
        os.environ["CUDA_VISIBLE_DEVICES"] = f"{len(tf.config.list_physical_devices('GPU'))}"

        detected_devices_details = device_lib.list_local_devices()
        detected_gpus = [device for device in detected_devices_details if device.device_type == "GPU"]
        if len(detected_gpus) == 1:
            print("NVIDIA CUDA supported GPU detected on your system.")
            gpu = detected_gpus[0]
            gpu_description = gpu.physical_device_desc
            gpu_name = gpu_description.split("name: ")[1].split(",")[0]
            print(f"GPU Name: {gpu_name}\n")
            gpu_index = 0

        else:
            print("NVIDIA CUDA supported GPUs detected on your system.\n"
                  "Detected GPUs:")
            for g, gpu in enumerate(detected_gpus):
                gpu_description = gpu.physical_device_desc
                gpu_name = gpu_description.split("name: ")[1].split(",")[0]
                print(f"[{g + 1}] - {gpu_name}")
            print("Please select the GPU you want to use for training.\n")
            option = get_menu_input(range(len(detected_gpus) + 1)[1:])
            gpu_index = option - 1
            print(f"GPU Selected: {detected_gpus[gpu_index].physical_device_desc.split('name: ')[1].split(',')[0]}\n")

        print("--- Step 14: Getting Selected Device to Train Complete ---\n")
        return "GPU", gpu_index


def train_model(device, model, data_generator, x_train, y_train, batch_size, epochs, x_validation, y_validation):
    print("--- Step 15: Training Model ---\n")

    start_time = time.perf_counter()
    with tf.device(device):
        history = model.fit(
            data_generator.flow(x_train, y_train, batch_size=batch_size),
            steps_per_epoch=math.floor(len(x_train) / batch_size) - 1, epochs=epochs,
            validation_data=(x_validation, y_validation),
            validation_steps=math.floor(len(x_validation) // batch_size) - 1, shuffle=1
        )
    end_time = time.perf_counter()

    training_time_diff = end_time - start_time
    average_time_per_epoch = training_time_diff / epochs

    training_time_elapsed = time_printer(training_time_diff)
    average_time_elapsed_per_epoch = time_printer(average_time_per_epoch)
    print(f"\nTime elapsed on training (HH:MM:SS:MS): {training_time_elapsed}.")
    print(f"Average time per epoch (HH:MM:SS:MS): {average_time_elapsed_per_epoch}.\n")

    print("--- Step 15: Training Model Complete ---\n")
    return history


def plot_model_accuracy_and_loss_history(history):
    print("--- Step 16: Plotting Model Accuracy and Loss History ---")

    plt.figure(num="Model Accuracy")
    plt.plot(history.history["accuracy"])
    plt.plot(history.history["val_accuracy"])
    plt.legend(["Training Accuracy", "Validation Accuracy"])
    plt.title("Model Accuracy")
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")

    plt.figure(num="Model Loss")
    plt.plot(history.history["loss"])
    plt.plot(history.history["val_loss"])
    plt.legend(["Training Loss", "Validation Loss"])
    plt.title("Model Loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")

    plt.show()

    print("--- Step 16: Plotting Model Accuracy and Loss History Complete ---\n")
    return


def score_model(model, x_test, y_test):
    print("--- Step 17: Scoring Model ---\n")
    score = model.evaluate(x_test, y_test, verbose=0)
    print(f"Test Score: {score[0]}\n"
          f"Test Accuracy: {score[1]}\n")

    print("--- Step 17: Scoring Model Complete ---\n")
    return


def save_model_and_device_type_as_files(model, model_save_path, device_type, device_type_save_path):
    print("--- Step 18: Saving Model as a File ---\n")

    tf.keras.models.save_model(model, model_save_path)
    if os.path.exists(device_type_save_path):
        print(f"Model is successfully saved in {model_save_path}.\n")

    with open(device_type_save_path, "w", encoding="UTF-8") as f:
        f.write(device_type)
    if os.path.exists(device_type_save_path):
        print(f"Selected device type file saved in {device_type_save_path}.\n")

    print("--- Step 18: Saving Model as a File Complete ---\n")


def main():
    return 0


if __name__ == "__main__":
    main()
