import numpy as np
import copy
import cv2
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import shutil


class Variables:
    def __init__(self):
        self.is_analyzing = False
        self.traffic_sign_id = -2
        self.traffic_sign_name = ""
        self.traffic_sign_description = ""
        self.traffic_sign_accuracy = 0.0
        self.last_traffic_sign_id = -2
        self.is_fps_ready_to_be_updated = False
        self.previous_time = 0
        self.current_time = 0
        self.passed_iterations = 0
        self.last_fps = 0
        self.is_results_frame_ready_to_be_updated = False
        self.stop = False
        return

    def set_corresponding_variable(self, variable_name, value):
        if variable_name == "is_analyzing":
            self.is_analyzing = value

        elif variable_name == "traffic_sign_id":
            self.traffic_sign_id = value

        elif variable_name == "traffic_sign_name":
            self.traffic_sign_name = value

        elif variable_name == "traffic_sign_accuracy":
            self.traffic_sign_accuracy = value

        elif variable_name == "traffic_sign_description":
            self.traffic_sign_description = value

        elif variable_name == "last_traffic_sign_id":
            self.last_traffic_sign_id = value

        elif variable_name == "is_fps_ready_to_be_updated":
            self.is_fps_ready_to_be_updated = value

        elif variable_name == "previous_time":
            self.previous_time = value

        elif variable_name == "current_time":
            self.current_time = value

        elif variable_name == "passed_iterations":
            self.passed_iterations = value

        elif variable_name == "last_fps":
            self.last_fps = value

        elif variable_name == "is_results_frame_ready_to_be_updated":
            self.is_results_frame_ready_to_be_updated = value

        elif variable_name == "stop":
            self.stop = value

        return

    def get_corresponding_variable(self, variable_name):
        if variable_name == "is_analyzing":
            return self.is_analyzing

        elif variable_name == "traffic_sign_id":
            return self.traffic_sign_id

        elif variable_name == "traffic_sign_name":
            return self.traffic_sign_name

        elif variable_name == "traffic_sign_description":
            return self.traffic_sign_description

        elif variable_name == "traffic_sign_accuracy":
            return self.traffic_sign_accuracy

        elif variable_name == "last_traffic_sign_id":
            return self.last_traffic_sign_id

        elif variable_name == "is_fps_ready_to_be_updated":
            return self.current_time - self.previous_time >= 1

        elif variable_name == "previous_time":
            return self.previous_time

        elif variable_name == "current_time":
            return self.current_time

        elif variable_name == "passed_iterations":
            return self.passed_iterations

        elif variable_name == "last_fps":
            return self.last_fps

        elif variable_name == "is_results_frame_ready_to_be_updated":
            return self.is_results_frame_ready_to_be_updated

        elif variable_name == "stop":
            return self.stop


class Images:
    def set_image_frame(self, image, is_camera):
        if image is None:
            self.image = np.zeros([480, 640, 3], dtype=np.uint8)
        else:
            self.image = copy.copy(image)

        if is_camera:
            self.resized = copy.copy(self.image)
        else:
            self.resized = cv2.resize(self.image, (0, 0), fx=0.8, fy=0.8)

        self.converted = cv2.cvtColor(self.resized, cv2.COLOR_BGR2RGB)
        self.image_frame = ImageTk.PhotoImage(Image.fromarray(self.converted))
        return

    def __init__(self):
        self.image = None
        self.resized = None
        self.converted = None
        self.image_frame = None
        return

    def get_corresponding_image_frame(self, image_name):
        if image_name == "image":
            return self.image
        elif image_name == "resized":
            return self.resized
        elif image_name == "converted":
            return self.converted
        elif image_name == "image_frame":
            return self.image_frame


def on_closing(variables_object, cap, window):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        variables_object.set_corresponding_variable("stop", True)
        cap.release()
        window.destroy()

    return


def clear_results_tab(l_taken_photo_text, results_image_object, l_taken_photo_frame,
                      l_traffic_sign_screenshot_name, l_traffic_sign_screenshot_description,
                      call_from_delete, l_command_information_text, window):
    l_taken_photo_text.configure(text="Taken Photo will be shown here.", fg="#D5EB34")

    results_image_object.set_image_frame(None, False)
    blank_image = results_image_object.get_corresponding_image_frame("image_frame")

    l_taken_photo_frame['image'] = blank_image
    l_traffic_sign_screenshot_name.configure(text="")
    l_traffic_sign_screenshot_description.configure(text="")

    if not call_from_delete:
        l_command_information_text.configure(text="Results are cleared.")
    window.after(2000, lambda: clear_command_text(l_command_information_text))

    return


def clear_command_text(l_command_information_text):
    l_command_information_text.configure(text="")
    return


def clear_photos(application_testing_folder, results_image_object, l_command_information_text, window,
                 l_taken_photo_text, l_taken_photo_frame,
                 l_traffic_sign_screenshot_name, l_traffic_sign_screenshot_description
                 ):
    photos_folder = os.path.join(application_testing_folder, "Photos")

    current_cwd = os.getcwd()
    os.chdir(application_testing_folder)

    if os.path.exists(photos_folder):
        if len(os.listdir(photos_folder)) != 0:
            shutil.rmtree("Photos")
            os.mkdir("Photos")

    os.chdir(current_cwd)

    l_command_information_text.configure(text="All photos are deleted successfully.")
    clear_results_tab(l_taken_photo_text, results_image_object, l_taken_photo_frame,
                      l_traffic_sign_screenshot_name, l_traffic_sign_screenshot_description,
                      True, l_command_information_text, window)
    l_command_information_text.configure(text="All photos are deleted.")
    window.after(2000, lambda: clear_command_text(l_command_information_text))
    return


def analyze_state(state, variables_object, l_command_information_text, window):
    if state:
        variables_object.set_corresponding_variable("is_analyzing", True)
        l_command_information_text.configure(text="Analyzing is activated.")

    else:
        variables_object.set_corresponding_variable("is_analyzing", False)
        l_command_information_text.configure(text="Analyzing is deactivated.")

    window.after(2000, lambda: clear_command_text(l_command_information_text))
    return


def save_image(photos_folder, photo_to_save, count):
    camera_frame = Image.fromarray(photo_to_save)
    current_cwd = os.getcwd()
    os.chdir(photos_folder)
    camera_frame.save(f"{count + 1}.jpg")
    os.chdir(current_cwd)
    return


def show_information(variables_object, l_traffic_sign_screenshot_name, l_traffic_sign_screenshot_description, color):
    traffic_sign_name = variables_object.get_corresponding_variable("traffic_sign_name")
    traffic_sign_description = variables_object.get_corresponding_variable("traffic_sign_description")
    l_traffic_sign_screenshot_name.configure(text=f"Traffic Sign Name:\n{traffic_sign_name}", fg=color)
    l_traffic_sign_screenshot_description.configure(text=f"Traffic Sign Description:\n{traffic_sign_description}",
                                                    fg=color)
    return


def take_photo(variables_object, camera_image_object, detection_threshold, detection_area_coordinates,
               photos_folder, l_taken_photo_text, l_command_information_text, window,
               l_traffic_sign_screenshot_name, l_traffic_sign_screenshot_description, ):
    count = len(os.listdir(photos_folder))

    traffic_sign_id = variables_object.get_corresponding_variable("traffic_sign_id")
    traffic_sign_name = variables_object.get_corresponding_variable("traffic_sign_name")
    traffic_sign_accuracy = variables_object.get_corresponding_variable("traffic_sign_accuracy")

    is_analyzing = variables_object.get_corresponding_variable("is_analyzing")
    photo_to_save = camera_image_object.get_corresponding_image_frame("converted")
    detected = (traffic_sign_id != -1 and traffic_sign_name != "" and traffic_sign_accuracy >= detection_threshold)
    if is_analyzing and detected:
        variables_object.set_corresponding_variable("last_traffic_sign_id", traffic_sign_id)
        color = "green"
        photo_to_save = cv2.putText(
            photo_to_save, f"ID: {traffic_sign_id}",
            (
                detection_area_coordinates["top_left_corner"]["x"] + 5,
                detection_area_coordinates["top_left_corner"]["y"] - 100
            ),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (52, 235, 79), 2, cv2.LINE_AA
        )

        photo_to_save = cv2.putText(
            photo_to_save, f"Name: {traffic_sign_name}",
            (
                detection_area_coordinates["top_left_corner"]["x"] + 5,
                detection_area_coordinates["top_left_corner"]["y"] - 85
            ),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (52, 235, 79), 2, cv2.LINE_AA
        )

        photo_to_save = cv2.putText(
            photo_to_save,
            "Accuracy: {:.2f}%".format(round(traffic_sign_accuracy * 100, 2)),
            (
                detection_area_coordinates["top_left_corner"]["x"] + 5,
                detection_area_coordinates["top_left_corner"]["y"] - 70
            ),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (52, 235, 79), 2, cv2.LINE_AA
        )

        l_taken_photo_text.configure(text="Taken Photo - Traffic Sign Detected!", fg="green")

    elif is_analyzing and not detected:
        variables_object.set_corresponding_variable("last_traffic_sign_id", -1)
        color = "red"
        l_taken_photo_text.configure(text="Taken Photo - No Traffic Sign Detected!", fg="red")

    else:
        variables_object.set_corresponding_variable("last_traffic_sign_id", -2)
        color = "#349EEB"
        l_taken_photo_text.configure(text="Taken Photo - Detection Deactivated!", fg="#349EEB")

    variables_object.set_corresponding_variable("last_traffic_sign_id", traffic_sign_id)

    save_image(photos_folder, photo_to_save, count)
    l_command_information_text.configure(text=f"Photo is saved with the name '{count + 1}.jpg' in the 'Photos' folder!")
    window.after(2000, lambda: clear_command_text(l_command_information_text))
    show_information(variables_object, l_traffic_sign_screenshot_name, l_traffic_sign_screenshot_description, color)

    return


def update_photo(results_image_object, variables_object, photos_folder):
    current_count = len(os.listdir(photos_folder))
    current_cwd = os.getcwd()
    os.chdir(photos_folder)
    try:
        image_read = cv2.imread(f"{current_count}.jpg")
    except TypeError:
        results_image_object.set_image_frame(None, False)
        image_read = results_image_object.get_corresponding_image_frame("image_frame")

    os.chdir(current_cwd)

    results_image_object.set_image_frame(image_read, False)
    variables_object.set_corresponding_variable("is_results_frame_ready_to_be_updated", True)
    return


def take_and_update_photo(camera_image_object,
                          variables_object, detection_threshold, detection_area_coordinates,
                          photos_folder, l_taken_photo_text, l_command_information_text, window,
                          results_image_object, l_traffic_sign_screenshot_name, l_traffic_sign_screenshot_description
                          ):
    take_photo(variables_object, camera_image_object, detection_threshold, detection_area_coordinates,
               photos_folder, l_taken_photo_text, l_command_information_text, window,
               l_traffic_sign_screenshot_name, l_traffic_sign_screenshot_description, )
    window.after(1000, lambda: update_photo(results_image_object, variables_object, photos_folder))
