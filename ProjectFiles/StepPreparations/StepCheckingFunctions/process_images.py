import cv2
import pygetwindow as pgw
import time


def process_images():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera is currently unavailable. Please try again after checking camera.")
        exit(1)
    else:
        print("Camera found. Getting the information and frames.")

    show_original = True
    show_grayed = False
    show_equalized = False
    show_normalized = False

    fps_cap = 30

    frame_count = 0
    fps_start_frame_time = time.time()
    while any([show_original, show_grayed, show_equalized, show_normalized]):
        success, original_image = cap.read()

        frame_count += 1
        fps_end_frame_time = time.time()
        time_diff = fps_end_frame_time - fps_start_frame_time

        try:
            fps = 1 / time_diff
        except ZeroDivisionError:
            fps = 30

        fps = round(fps, 2)
        fps_start_frame_time = fps_end_frame_time

        width = int(cap.get(3))
        height = int(cap.get(4))

        print(f"Width {width}px, Height: {height}px, Frame: {frame_count}, FPS: {fps}")

        grayed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        equalized_image = cv2.equalizeHist(grayed_image)
        normalized_image = equalized_image / 255

        if show_original:
            cv2.imshow("Original Image", original_image)
        else:
            windows = pgw.getAllTitles()
            if "Original Image" in windows:
                cv2.destroyWindow("Original Image")

        if show_grayed:
            cv2.imshow("Grayed Image", grayed_image)
        else:
            windows = pgw.getAllTitles()
            if "Grayed Image" in windows:
                cv2.destroyWindow("Grayed Image")

        if show_equalized:
            cv2.imshow("Grayed + Equalized Image", equalized_image)
        else:
            windows = pgw.getAllTitles()
            if "Grayed + Equalized Image" in windows:
                cv2.destroyWindow("Grayed + Equalized Image")

        if show_normalized:
            cv2.imshow("Grayed + Equalized + Normalized Image", normalized_image)
        else:
            windows = pgw.getAllTitles()
            if "Grayed + Equalized + Normalized Image" in windows:
                cv2.destroyWindow("Grayed + Equalized + Normalized Image")

        captured_key = cv2.waitKey(1000 // fps_cap)

        if captured_key == ord('q') or (
                cv2.getWindowProperty("Original Image", cv2.WND_PROP_VISIBLE) < 1 and
                cv2.getWindowProperty("Grayed Image", cv2.WND_PROP_VISIBLE) < 1 and
                cv2.getWindowProperty("Grayed + Equalized Image", cv2.WND_PROP_VISIBLE) < 1 and
                cv2.getWindowProperty("Grayed + Equalized + Normalized Image", cv2.WND_PROP_VISIBLE) < 1):
            break

        elif captured_key in [ord('1'), ord('2'), ord('3'), ord('4')]:
            if captured_key == ord('1'):
                show_original = not show_original

            elif captured_key == ord('2'):
                show_grayed = not show_grayed

            elif captured_key == ord('3'):
                show_equalized = not show_equalized

            elif captured_key == ord('4'):
                show_normalized = not show_normalized

    cap.release()
    cv2.destroyAllWindows()


def main():
    return 0


if __name__ == "__main__":
    main()
