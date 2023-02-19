import cv2
import time

def main():
    window_title = "CSI Camera"
    
    # video_capture = cv2.VideoCapture("/dev/video0")
    video_capture = cv2.VideoCapture("rtsp://10.0.0.12:8554/test")
    video_capture.set(cv2.CAP_PROP_BUFFERSIZE,1)

    start = time.time()
    paused = False
    print(f"FPS: {int(video_capture.get(cv2.CAP_PROP_FPS))}")
    if video_capture.isOpened():
        try:
            
            # window_handle = cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE)
            while True:
                if (time.time() - start > 5) and paused == False:
                    print("inside")
                    time.sleep(5)
                    video_capture.release()
                    video_capture = cv2.VideoCapture("rtsp://10.0.0.12:8554/test")
                    video_capture.set(cv2.CAP_PROP_BUFFERSIZE,1)
                    paused = True
                t0 = time.time()
                ret, img = video_capture.read()
                # print(f"time for capture {time.time() - t0}")
                if ret == False:
                    continue
                cv2.imshow("Source", img)
                keyCode = cv2.waitKey(10) & 0xFF
                # Stop the program on the ESC key or 'q'
                if keyCode == 27 or keyCode == ord('q'):
                   break
        finally:
            video_capture.release()
            cv2.destroyAllWindows()
    else:
        print("Error: Unable to open camera")


if __name__ == "__main__":
    main()

