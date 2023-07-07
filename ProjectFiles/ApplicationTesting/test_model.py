import os
import time
import cv2

from TestingFunctions.testing_extra_functions import handle_first_run

from TestingFunctions.testing_step_functions import (
    check_set_and_get_camera, create_tkinter_window, create_labels_in_window, load_model,
    analyze_sign, update_results_frame, update_fps_frame
)

from TestingFunctions.background_functions import Variables, Images

from TestingFunctions.testing_settings import DETECTION_THRESHOLD, DETECTION_AREA_COORDINATES


def main():
    script_path = os.path.abspath(__file__)
    script_name = __file__.split("\\")[-1]

    application_testing_folder = script_path.rstrip(script_name).rstrip("\\")
    application_testing_folder_name = application_testing_folder.split("\\")[-1]

    icon_folder = os.path.join(application_testing_folder, "Icon")
    icon_path = os.path.join(icon_folder, "icon.ico")

    project_files_folder = application_testing_folder.rstrip(application_testing_folder_name).rstrip("\\")
    dataset_files_folder = os.path.join(project_files_folder, "DatasetFiles")
    model_save_path = os.path.join(dataset_files_folder, "trained_model.h5")

    testing_can_start = handle_first_run(model_save_path, project_files_folder, application_testing_folder, icon_path)
    if not testing_can_start:
        print("Exiting...")
        return 0

    valid, cap = check_set_and_get_camera()
    if not valid and cap is None:
        return 0

    variables_object = Variables()
    variables_object.set_corresponding_variable("stop", False)
    window = create_tkinter_window(variables_object, cap)

    photos_folder = os.path.join(application_testing_folder, "Photos")

    camera_image_object = Images()
    camera_image_object.set_image_frame(None, True)
    results_image_object = Images()
    results_image_object.set_image_frame(None, False)

    window_with_objects, objects = create_labels_in_window(
        window, application_testing_folder,
        results_image_object, variables_object, camera_image_object,
        DETECTION_THRESHOLD, DETECTION_AREA_COORDINATES,
        cap, photos_folder
    )

    l_traffic_sign_id_text = objects["l_traffic_sign_id_text"]
    l_traffic_sign_name_text = objects["l_traffic_sign_name_text"]
    l_traffic_sign_accuracy_text = objects["l_traffic_sign_accuracy_text"]
    l_traffic_sign_id_value = objects["l_traffic_sign_id_value"]
    l_traffic_sign_name_value = objects["l_traffic_sign_name_value"]
    l_traffic_sign_accuracy_value = objects["l_traffic_sign_accuracy_value"]

    l_camera_image = objects["l_camera_image"]
    l_taken_photo_frame = objects["l_taken_photo_frame"]
    l_fps = objects["l_fps"]

    variables_object.set_corresponding_variable("passed_iterations", 0)
    variables_object.set_corresponding_variable("current_time", time.perf_counter())
    variables_object.set_corresponding_variable("previous_time", time.perf_counter())

    model = load_model(model_save_path)
    while True:
        if variables_object.get_corresponding_variable("stop"):
            break

        success, image = cap.read()
        if not success:
            print("Camera image could not read.\n"
                  "Exiting...")
            break
        analyze_sign(
            image, model, variables_object, DETECTION_AREA_COORDINATES, DETECTION_THRESHOLD,
            l_traffic_sign_id_text, l_traffic_sign_name_text, l_traffic_sign_accuracy_text,
            l_traffic_sign_id_value, l_traffic_sign_name_value, l_traffic_sign_accuracy_value
        )

        fitting_camera_image = cv2.resize(image, (640, 480))
        image_without_black_bars = fitting_camera_image[60:420]
        camera_image_object.set_image_frame(image_without_black_bars, True)
        camera_frame = camera_image_object.get_corresponding_image_frame("image_frame")
        l_camera_image['image'] = camera_frame

        is_results_frame_ready_to_be_updated = variables_object.get_corresponding_variable("is_results_frame_ready_to_be_updated")
        if is_results_frame_ready_to_be_updated:
            update_results_frame(results_image_object, l_taken_photo_frame, variables_object)

        variables_object.set_corresponding_variable("current_time", time.perf_counter())
        is_fps_ready_to_be_updated = variables_object.get_corresponding_variable("is_fps_ready_to_be_updated")
        if is_fps_ready_to_be_updated:
            current_time, fps = update_fps_frame(variables_object, l_fps)

            variables_object.set_corresponding_variable("passed_iterations", 0)
            variables_object.set_corresponding_variable("previous_time", current_time)
            variables_object.set_corresponding_variable("last_fps", fps)
        else:
            passed_iterations = variables_object.get_corresponding_variable("passed_iterations")
            passed_iterations += 1
            variables_object.set_corresponding_variable("passed_iterations", passed_iterations)

        window.update()

    return 0


if __name__ == "__main__":
    main()
