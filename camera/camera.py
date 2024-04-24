import cv2 
import threading
import time

class Camera:
    def __init__(self):
        self.start_stream()
        self.stop = 0

        # Create threads for each task
        cap_thread = threading.Thread(target=self.capture_frame)
        det_thread = threading.Thread(target=self.detect)
        dis_thread = threading.Thread(target=self.display)

        # Start threads
        cap_thread.start()
        time.sleep(1)
        det_thread.start()
        dis_thread.start()

        # Wait for threads to finish
        cap_thread.join()
        det_thread.join()
        dis_thread.join()
        

    def start_stream(self):
        self.cap = cv2.VideoCapture("/dev/video0")
        if not self.cap.isOpened():
            print("Error: Could not open video stream")

    def capture_frame(self):
        while self.cap.isOpened() and not self.stop:
            self.frame = self.cap.read()

    def detect(self):
        while not self.stop:
            detect_frame = self.frame.copy()
            pass

    def display(self):
        while not self.stop:
            display_frame = self.frame.copy()
            cv2.imshow('Camera Stream', display_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stop = 1
                break

        self.cap.release()
        cv2.destroyAllWindows()