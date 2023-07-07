import os
import numpy as np

from TrainingFunctions.training_extra_functions import handle_first_run, check_model_device_compatibility

from TrainingFunctions.training_settings import (
    VALIDATION_RATIO, TEST_RATIO, DATASET_IMAGE_DIMENSIONS, BATCH_SIZE, EPOCHS,
    COLUMN_COUNT_FOR_EXAMPLE_IMAGES_GRAPH, FIGURE_SIZE_FOR_EXAMPLE_IMAGES_GRAPH,
    FIGURE_SIZE_FOR_DATASET_DISTRIBUTION_GRAPH,
    FIGURE_SIZE_FOR_EXAMPLE_PROCESSED_IMAGE,
    WIDTH_SHIFT_RATIO_FOR_AUGMENTATION, HEIGHT_SHIFT_RATIO_FOR_AUGMENTATION, ZOOM_RATIO_FOR_AUGMENTATION,
    SHEAR_RATIO_FOR_AUGMENTATION, ROTATION_FOR_AUGMENTATION,
    ROWS_FOR_EXAMPLE_FOR_A_BATCH_OF_AUGMENTED_IMAGES, COLUMNS_FOR_EXAMPLE_FOR_A_BATCH_OF_AUGMENTED_IMAGES,
    FIGURE_SIZE_FOR_AUGMENTED_IMAGE_EXAMPLES, FONT_SIZE_FOR_AUGMENTED_IMAGE_EXAMPLES,
    NUMBER_OF_FILTERS_FOR_MODEL,
    SIZE_OF_FILTER_FOR_FIRST_2D_LAYERS_FOR_MODEL, SIZE_OF_FILTER_FOR_LAST_2D_LAYERS_FOR_MODEL,
    SIZE_OF_POOL_FOR_MODEL, NUMBER_OF_NODES_FOR_MODEL
)

from TrainingFunctions.training_step_functions import (
    read_csv, read_dataset_images,
    split_dataset, check_compatibility,
    show_dataset_examples_for_each_class,
    show_dataset_training_distribution,
    process_dataset_images, show_processed_image_example,
    add_depth_to_images,
    augment_images, show_augmented_image_examples, categorize_class_ids,
    create_model, get_selected_device_to_train, train_model,
    plot_model_accuracy_and_loss_history, score_model, save_model_and_device_type_as_files
)


def main():
    script_path = os.path.abspath(__file__)
    script_name = __file__.split("\\")[-1]

    training_folder = script_path.rstrip(script_name).rstrip("\\")
    training_folder_name = training_folder.split("\\")[-1]

    project_files_folder = training_folder.rstrip(training_folder_name).rstrip("\\")

    dataset_files_folder = os.path.join(project_files_folder, "DatasetFiles")

    dataset_path = os.path.join(dataset_files_folder, "dataset")
    csv_path = os.path.join(dataset_files_folder, "labels.csv")

    model_save_path = os.path.join(dataset_files_folder, "trained_model.h5")
    device_type_save_path = os.path.join(dataset_files_folder, "device_type.txt")

    files_are_saved = handle_first_run(project_files_folder, dataset_files_folder)
    if files_are_saved:
        check_model_device_compatibility(device_type_save_path)

        print("There is no need to continue for training phase.")
        print("Exiting...")

        return 0

    print("TRAINING PHASE STARTED.\n")

    data, data_array = read_csv(csv_path)

    images, classes = read_dataset_images(dataset_path, data_array)

    x_train, x_test, x_validation, y_train, y_test, y_validation = split_dataset(
        images, classes, VALIDATION_RATIO, TEST_RATIO
    )

    error = check_compatibility(x_train, x_test, x_validation, y_train, y_test, y_validation, DATASET_IMAGE_DIMENSIONS)
    if error:
        print("Please check the dataset or the source code for the issues or download them again.")
        exit(1)

    number_of_classes = len(os.listdir(dataset_path))

    number_of_images_in_each_folder = show_dataset_examples_for_each_class(
        number_of_classes,
        COLUMN_COUNT_FOR_EXAMPLE_IMAGES_GRAPH, FIGURE_SIZE_FOR_EXAMPLE_IMAGES_GRAPH,
        data_array, x_train, y_train
    )

    show_dataset_training_distribution(
        FIGURE_SIZE_FOR_DATASET_DISTRIBUTION_GRAPH, number_of_classes, number_of_images_in_each_folder
    )

    x_train_processed, x_validation_processed, x_test_processed = process_dataset_images(x_train, x_validation, x_test)

    processed_images_array = np.insert(x_train_processed, 0, x_validation_processed, axis=0)
    processed_images_array = np.insert(processed_images_array, 0, x_test_processed, axis=0)
    combined_classes_array = np.insert(y_train, 0, y_validation, axis=0)
    combined_classes_array = np.insert(combined_classes_array, 0, y_test, axis=0)
    class_names = [data_array[i][1] for i in range(number_of_classes)]
    show_processed_image_example(
        FIGURE_SIZE_FOR_EXAMPLE_PROCESSED_IMAGE, processed_images_array, combined_classes_array, class_names
    )

    x_train_deepened, x_validation_deepened, x_test_deepened = add_depth_to_images(
        x_train_processed, x_validation_processed, x_test_processed
    )

    batches, data_generator = augment_images(
        WIDTH_SHIFT_RATIO_FOR_AUGMENTATION, HEIGHT_SHIFT_RATIO_FOR_AUGMENTATION,
        ZOOM_RATIO_FOR_AUGMENTATION, SHEAR_RATIO_FOR_AUGMENTATION, ROTATION_FOR_AUGMENTATION,
        x_train_deepened, y_train, BATCH_SIZE
    )

    x_batch, y_batch = next(batches)
    show_augmented_image_examples(
        ROWS_FOR_EXAMPLE_FOR_A_BATCH_OF_AUGMENTED_IMAGES, COLUMNS_FOR_EXAMPLE_FOR_A_BATCH_OF_AUGMENTED_IMAGES,
        FIGURE_SIZE_FOR_AUGMENTED_IMAGE_EXAMPLES, FONT_SIZE_FOR_AUGMENTED_IMAGE_EXAMPLES,
        x_batch, DATASET_IMAGE_DIMENSIONS
    )

    y_train_categorized, y_validation_categorized, y_test_categorized = categorize_class_ids(
        y_train, y_validation, y_test, number_of_classes
    )

    model = create_model(
        NUMBER_OF_FILTERS_FOR_MODEL,
        SIZE_OF_FILTER_FOR_FIRST_2D_LAYERS_FOR_MODEL, SIZE_OF_FILTER_FOR_LAST_2D_LAYERS_FOR_MODEL,
        SIZE_OF_POOL_FOR_MODEL, NUMBER_OF_NODES_FOR_MODEL,
        DATASET_IMAGE_DIMENSIONS, number_of_classes
    )

    device_type, device_index = get_selected_device_to_train()

    device = f"/{device_type}:{device_index}"
    history = train_model(
        device, model, data_generator, x_train_deepened, y_train_categorized, BATCH_SIZE, EPOCHS,
        x_validation_deepened, y_validation_categorized,
    )

    plot_model_accuracy_and_loss_history(history)

    score_model(model, x_test_deepened, y_test_categorized)

    save_model_and_device_type_as_files(model, model_save_path, device_type, device_type_save_path)

    print("TRAINING PHASE FINISHED.\n")
    return 0


if __name__ == "__main__":
    main()
