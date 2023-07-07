import cv2
import time


def detect_camera():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera is currently unavailable. Please try again after checking camera.")
        exit(1)
    else:
        print("Camera found. Getting the information and frames.")

    fps_cap = 30

    frame_count = 0
    fps_start_frame_time = time.time()
    while True:
        _valid_, frame = cap.read()

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

        cv2.imshow('Camera', frame)

        if cv2.waitKey(1000 // fps_cap) == ord('q') or cv2.getWindowProperty("Camera", cv2.WND_PROP_VISIBLE) < 1:
            print("Stopped at frame " + str(frame_count))
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    return 0


if __name__ == '__main__':
    main()
