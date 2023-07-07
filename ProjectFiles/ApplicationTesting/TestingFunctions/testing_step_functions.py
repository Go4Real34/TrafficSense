import cv2
import os
import tkinter as tk
import tensorflow as tf
import numpy as np
import time

from .testing_extra_functions import get_menu_input, preprocess_image
from .background_functions import on_closing, clear_results_tab, clear_photos, analyze_state, take_and_update_photo
from .traffic_sign_names import get_traffic_sign_information


def check_set_and_get_camera():
    print("\nThe cameras connected to your system will be checked for using for detection.\n")
    print("Press enter the number of cameras that is connected to your computer or, 0 or lower to exit.")
    connected_maximum_camera_count = get_menu_input()
    if connected_maximum_camera_count < 0:
        print("\nCamera count cannot be negative.\n"
              "Exiting...\n")
        return False, None

    elif connected_maximum_camera_count == 0:
        print("\nExiting...\n")
        return False, None

    elif connected_maximum_camera_count == 1:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Camera is not available.\n")
            return False, None

        else:
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            print("\nCamera detected successfully.")
            return True, cap

    selected_camera_index = -1
    for index in range(connected_maximum_camera_count + 1):
        try:
            print(f"\nTrying camera with index {index}.")
            cap = cv2.VideoCapture(index)
            if not cap.isOpened():
                print(f"Camera with index {index} is not available.")
                continue

            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

            print(f"Camera detected with index {index}.")
            print("Press Q on the camera screen to select this camera, any other key to try another.")
            while True:
                success, image = cap.read()
                if not success:
                    print(f"Camera with index {index} is available but image could not be read from the camera.\n")
                    break

                cv2.imshow(f"Camera with Index {index}", image)
                key = cv2.waitKey(1)

                if key != -1:
                    if key == ord("q") or key == ord("Q"):
                        selected_camera_index = index
                        print(f"\nCamera with index {index} is selected.\n")

                    else:
                        print(f"\nCamera with index {index} is not selected.\n")

                    cap.release()
                    cv2.destroyAllWindows()
                    break

            if selected_camera_index != -1:
                break

        except Exception as e:
            print(f"Critical error occurred while trying to access camera with index {index}.\n"
                  f"Error code: {e}.\n")

    cv2.destroyAllWindows()
    if selected_camera_index == -1:
        print("No camera is selected.\n")
        return False, None

    cap = cv2.VideoCapture(selected_camera_index)
    if not cap.isOpened():
        print(f"Selected camera with index {selected_camera_index} is not available.\n")
        return False, None

    else:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        print("\nCamera detected successfully.")
        return True, cap


def create_tkinter_window(variable_object, cap):
    window = tk.Tk()

    file_path = os.path.abspath(__file__)
    file_name = file_path.split("\\")[-1]

    testing_functions_folder = file_path.rstrip(file_name).rstrip("\\")
    testing_functions_folder_name = testing_functions_folder.split("\\")[-1]

    application_testing_folder = testing_functions_folder.rstrip(testing_functions_folder_name).rstrip("\\")
    icon_folder = os.path.join(application_testing_folder, "Icon")
    icon_path = os.path.join(icon_folder, "icon.ico")

    window.iconbitmap(icon_path)
    window.title("Traffic Sign Recognition Application by Gorkem Sarikaya")

    window.geometry("1280x720")
    window.resizable(False, False)

    window.configure(bg="black")
    window.protocol("WM_DELETE_WINDOW", lambda: on_closing(variable_object, cap, window))

    return window


def create_labels_in_window(window, application_testing_folder,
                            results_image_object, variables_object, camera_image_object,
                            detection_threshold, detection_area_coordinates,
                            cap, photos_folder):
    l_project_information = tk.Label(
        window, text="Traffic Sign Recognition by Application by Gorkem Sarikaya", font=("Montserrat", 16, "italic"),
        bg="black", fg="red"
    )
    l_project_information.place(relx=0.5, anchor="n")

    lf_camera = tk.LabelFrame(window, bg="black")
    lf_camera.place(x=30, y=80)

    l_camera_text = tk.Label(
        lf_camera,
        text="Put the traffic sign in the colored box.", font=("Montserrat", 16, "italic"),
        bg="black", fg="#D5EB34"
    )
    l_camera_text.grid(row=0, column=0)

    l_camera_image = tk.Label(lf_camera, bg="black")
    l_camera_image.grid(row=1, column=0)

    l_command_information_text = tk.Label(
        window,
        text="", font=("Montserrat", 10, "bold", "italic"),
        bg="black", fg="#34EB46"
    )
    l_command_information_text.place(relx=0.5, rely=1, anchor="s")

    lf_traffic_sign_infos = tk.LabelFrame(window, bg="black")
    lf_traffic_sign_infos.place(x=80, y=500)

    l_traffic_sign_id_text = tk.Label(
        lf_traffic_sign_infos,
        text="Traffic Sign ID: ", font=("Montserrat", 14, "bold"),
        bg="black", fg="#349EEB"
    )
    l_traffic_sign_id_text.grid(row=0, column=0)

    l_traffic_sign_name_text = tk.Label(
        lf_traffic_sign_infos,
        text="Traffic Sign Name: ", font=("Montserrat", 14, "bold"),
        bg="black", fg="#349EEB"
    )
    l_traffic_sign_name_text.grid(row=1, column=0)

    l_traffic_sign_accuracy_text = tk.Label(
        lf_traffic_sign_infos,
        text="Traffic Sign Accuracy: ", font=("Montserrat", 14, "bold"),
        bg="black", fg="#349EEB"
    )
    l_traffic_sign_accuracy_text.grid(row=2, column=0)

    l_traffic_sign_id_value = tk.Label(
        lf_traffic_sign_infos,
        text="-", font=("Montserrat", 14, "bold"),
        bg="black", fg="#349EEB"
    )
    l_traffic_sign_id_value.grid(row=0, column=1)

    l_traffic_sign_name_value = tk.Label(
        lf_traffic_sign_infos,
        text="-", font=("Montserrat", 14, "bold"),
        bg="black", fg="#349EEB"
    )
    l_traffic_sign_name_value.grid(row=1, column=1)

    l_traffic_sign_accuracy_value = tk.Label(
        lf_traffic_sign_infos,
        text="-", font=("Montserrat", 14, "bold"),
        bg="black", fg="#349EEB"
    )
    l_traffic_sign_accuracy_value.grid(row=2, column=1)

    l_fps = tk.Label(
        window,
        text="FPS: ", font=("Montserrat", 12, "bold"),
        bg="black", fg="green"
    )
    l_fps.place(x=20, y=20)

    lf_taken_photo_infos = tk.LabelFrame(window, bg="black")
    lf_taken_photo_infos.place(x=720, y=80)

    l_taken_photo_text = tk.Label(
        lf_taken_photo_infos,
        text="Taken Photo will be shown here.",
        font=("Montserrat", 16, "italic"),
        bg="black",
        fg="#D5EB34"
    )
    l_taken_photo_text.grid(row=0, column=0)

    image_frame = results_image_object.get_corresponding_image_frame("image_frame")
    l_taken_photo_frame = tk.Label(
        lf_taken_photo_infos,
        image=image_frame,
        bg="black"
    )
    l_taken_photo_frame.grid(row=1, column=0)

    l_traffic_sign_screenshot_name = tk.Label(
        lf_taken_photo_infos,
        text="",
        font=("Montserrat", 12, "bold"),
        bg="black",
        fg="green"
    )
    l_traffic_sign_screenshot_name.grid(row=2, column=0)

    l_traffic_sign_screenshot_description = tk.Label(
        lf_taken_photo_infos,
        text="",
        font=("Montserrat", 12, "bold"),
        bg="black",
        fg="green"
    )
    l_traffic_sign_screenshot_description.grid(row=3, column=0)

    lf_buttons = tk.LabelFrame(window, bg="black")
    lf_buttons.place(relx=0.5, y=700, anchor="s")

    b_clear_results_tab = tk.Button(
        lf_buttons,
        text="Clear Results Tab",
        font=("Montserrat", 12, "bold"),
        bg="black",
        fg="#F58442",
        width=16,
        height=1,
        command=lambda: clear_results_tab(
            l_taken_photo_text, results_image_object, l_taken_photo_frame,
            l_traffic_sign_screenshot_name, l_traffic_sign_screenshot_description,
            False, l_command_information_text, window
        )
    )
    b_clear_results_tab.grid(row=0, column=0)

    b_delete_photos = tk.Button(
        lf_buttons,
        text="Clear Photos",
        font=("Montserrat", 12, "bold"),
        bg="black",
        fg="#9834EB",
        width=16,
        height=1,
        command=lambda: clear_photos(application_testing_folder, results_image_object, l_command_information_text,
                                     window,
                                     l_taken_photo_text, l_taken_photo_frame,
                                     l_traffic_sign_screenshot_name, l_traffic_sign_screenshot_description
                                     )
    )
    b_delete_photos.grid(row=0, column=1)

    b_close = tk.Button(
        lf_buttons,
        text="Close",
        font=("Montserrat", 12, "bold", "underline"),
        bg="black",
        fg="#EB34B7",
        width=16,
        height=1,
        command=lambda: on_closing(variables_object, cap, window)
    )
    b_close.grid(row=0, column=2)

    b_analyze_start = tk.Button(
        lf_buttons,
        text="Begin Analyzing",
        font=("Montserrat", 12, "bold"),
        bg="black",
        fg="#34D8EB",
        width=16,
        height=1,
        command=lambda: analyze_state(True, variables_object, l_command_information_text, window)
    )
    b_analyze_start.grid(row=1, column=0)

    b_take_photo = tk.Button(
        lf_buttons,
        text="Take Photo",
        font=("Montserrat", 12, "bold"),
        bg="black",
        fg="#345EEB",
        width=16,
        height=1,
        command=lambda: take_and_update_photo(
            camera_image_object,
            variables_object, detection_threshold, detection_area_coordinates,
            photos_folder, l_taken_photo_text, l_command_information_text, window,
            results_image_object, l_traffic_sign_screenshot_name, l_traffic_sign_screenshot_description
        )
    )
    b_take_photo.grid(row=1, column=1)

    b_analyze_stop = tk.Button(
        lf_buttons,
        text="Stop Analyzing",
        font=("Montserrat", 12, "bold"),
        bg="black",
        fg="#34EB9E",
        width=16,
        height=1,
        command=lambda: analyze_state(False, variables_object, l_command_information_text, window)
    )
    b_analyze_stop.grid(row=1, column=2)

    objects = {
        "l_project_information": l_project_information,
        "lf_camera": lf_camera,
        "l_camera_text": l_camera_text,
        "l_camera_image": l_camera_image,
        "l_command_information_text": l_command_information_text,
        "lf_traffic_sign_infos": lf_traffic_sign_infos,
        "l_traffic_sign_id_text": l_traffic_sign_id_text,
        "l_traffic_sign_name_text": l_traffic_sign_name_text,
        "l_traffic_sign_accuracy_text": l_traffic_sign_accuracy_text,
        "l_traffic_sign_id_value": l_traffic_sign_id_value,
        "l_traffic_sign_name_value": l_traffic_sign_name_value,
        "l_traffic_sign_accuracy_value": l_traffic_sign_accuracy_value,
        "l_fps": l_fps,
        "lf_taken_photo_infos": lf_taken_photo_infos,
        "l_taken_photo_text": l_taken_photo_text,
        "l_taken_photo_frame": l_taken_photo_frame,
        "l_traffic_sign_screenshot_name": l_traffic_sign_screenshot_name,
        "l_traffic_sign_screenshot_description": l_traffic_sign_screenshot_description,
        "lf_buttons": lf_buttons,
        "b_clear_results_tab": b_clear_results_tab,
        "b_delete_photos": b_delete_photos,
        "b_close": b_close,
        "b_analyze_start": b_analyze_start,
        "b_take_photo": b_take_photo,
        "b_analyze_stop": b_analyze_stop
    }

    return window, objects


def load_model(model_path):
    model = tf.keras.models.load_model(model_path)
    return model


def analyze_sign(image, model, variables_object, detection_area_coordinates, detection_threshold,
                 l_traffic_sign_id_text, l_traffic_sign_name_text, l_traffic_sign_accuracy_text,
                 l_traffic_sign_id_value, l_traffic_sign_name_value, l_traffic_sign_accuracy_value):
    is_analyzing = variables_object.get_corresponding_variable("is_analyzing")
    if is_analyzing:
        analyze_area_image = image[
                             detection_area_coordinates["top_left_corner"]["y"] + 5:
                             detection_area_coordinates["bottom_right_corner"]["y"] - 5,

                             detection_area_coordinates["top_left_corner"]["x"] + 5:
                             detection_area_coordinates["bottom_right_corner"]["x"] - 5,
                             ]
        array_image = np.asarray(analyze_area_image)
        resized_image = cv2.resize(array_image, (32, 32))
        processed_image = preprocess_image(resized_image)
        reshaped_image = processed_image.reshape(1, 32, 32, 1)

        predictions = model.predict(reshaped_image)
        highest_prediction_index = np.argmax(predictions, axis=-1)[0]
        traffic_sign_accuracy = predictions[0][highest_prediction_index]

        if traffic_sign_accuracy >= detection_threshold:
            state = 1
            color_for_camera_image_text = (52, 235, 79)
            color_for_information_frames = "green"

        else:
            state = 0
            color_for_camera_image_text = (52, 73, 235)
            highest_prediction_index = -1
            color_for_information_frames = "red"

    else:
        state = -1
        traffic_sign_accuracy = 0
        highest_prediction_index = -2
        color_for_information_frames = "#349EEB"
        color_for_camera_image_text = (235, 158, 52)

    traffic_sign_name, traffic_sign_description = get_traffic_sign_information(highest_prediction_index)
    variables_object.set_corresponding_variable("traffic_sign_id", highest_prediction_index)
    variables_object.set_corresponding_variable("traffic_sign_name", traffic_sign_name)
    variables_object.set_corresponding_variable("traffic_sign_description", traffic_sign_description)
    variables_object.set_corresponding_variable("traffic_sign_accuracy", traffic_sign_accuracy)

    l_traffic_sign_id_text.configure(fg=color_for_information_frames)
    l_traffic_sign_name_text.configure(fg=color_for_information_frames)
    l_traffic_sign_accuracy_text.configure(fg=color_for_information_frames)
    l_traffic_sign_id_value.configure(fg=color_for_information_frames)
    l_traffic_sign_name_value.configure(fg=color_for_information_frames)
    l_traffic_sign_accuracy_value.configure(fg=color_for_information_frames)

    if state == 1:
        l_traffic_sign_id_value.configure(text=f"{highest_prediction_index}")
        l_traffic_sign_name_value.configure(text=traffic_sign_name)
        l_traffic_sign_accuracy_value.configure(text="{:.2f}%".format(round(traffic_sign_accuracy * 100, 2)))
        image = cv2.putText(
            image,
            "Traffic Sign Detected!",
            (
                detection_area_coordinates["top_left_corner"]["x"] - 50,
                detection_area_coordinates["bottom_right_corner"]["y"] + 40
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color_for_camera_image_text,
            2,
            cv2.LINE_AA
        )

    elif state == 0:
        l_traffic_sign_id_value.configure(text=f"-")
        l_traffic_sign_name_value.configure(text="No Traffic Sign Detected.")
        l_traffic_sign_accuracy_value.configure(text="<{:.2f}%".format(detection_threshold * 100, 2))
        image = cv2.putText(
            image,
            "No Traffic Sign Detected!",
            (
                detection_area_coordinates["top_left_corner"]["x"] - 75,
                detection_area_coordinates["bottom_right_corner"]["y"] + 40
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color_for_camera_image_text,
            2,
            cv2.LINE_AA
        )

    elif state == -1:
        l_traffic_sign_id_value.configure(text=f"-")
        l_traffic_sign_name_value.configure(text="Detection Deactivated.")
        l_traffic_sign_accuracy_value.configure(text=f"0.00%")
        image = cv2.putText(
            image,
            "Detection Deactivated!",
            (
                detection_area_coordinates["top_left_corner"]["x"] - 50,
                detection_area_coordinates["bottom_right_corner"]["y"] + 40
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color_for_camera_image_text,
            2,
            cv2.LINE_AA
        )

    cv2.rectangle(
        image,
        (detection_area_coordinates["top_left_corner"]["x"], detection_area_coordinates["top_left_corner"]["y"]),
        (detection_area_coordinates["bottom_right_corner"]["x"], detection_area_coordinates["bottom_right_corner"]["y"]),
        color_for_camera_image_text,
        3
    )

    return


def update_results_frame(results_image_object, l_taken_photo_frame, variables_object):
    results_image_frame = results_image_object.get_corresponding_image_frame("image_frame")
    l_taken_photo_frame['image'] = results_image_frame
    variables_object.set_corresponding_variable("is_results_frame_ready_to_be_updated", False)
    return


def update_fps_frame(variables_object, l_fps):
    passed_iterations = variables_object.get_corresponding_variable("passed_iterations")
    current_time = time.perf_counter()
    previous_time = variables_object.get_corresponding_variable("previous_time")
    try:
        fps = passed_iterations / (current_time - previous_time)
    except ZeroDivisionError:
        fps = variables_object.get_corresponding_variable("last_fps")

    if fps >= 15:
        l_fps.configure(text="FPS: {:.2f}".format(round(fps, 2)), fg="green")
    else:
        l_fps.configure(text="FPS: {:.2f}\nSlow Processing Speed Detected!".format(round(fps, 2)), fg="red")

    return current_time, fps


def main():
    return 0


if __name__ == "__main__":
    main()
