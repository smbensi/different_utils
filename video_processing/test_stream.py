import cv2
import time
import sys

def main():
    print("capture screenshot using y key")
    if len(sys.argv) < 2:
        print("usage: python3 test_stream.py <device number> ")
    video_capture = cv2.VideoCapture(f"/dev/video{sys.argv[1]}")
    #define resolution
    # video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    # video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    
    
    # video_capture = cv2.VideoCapture("rtsp://10.0.0.12:8554/test")
    # video_capture.set(cv2.CAP_PROP_BUFFERSIZE,1)

    start = time.time()
    paused = False
    print(f"FPS: {int(video_capture.get(cv2.CAP_PROP_FPS))}")
    i  =  0
    if video_capture.isOpened():
        try:
            
            # window_handle = cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE)
            while True:
                t0 = time.time()
                ret, img = video_capture.read()
                print(f"time for capture {time.time() - t0}")
                if ret == False:
                    continue
                # cv2.imshow("Source", img)
                # keyCode = cv2.waitKey(10) & 0xFF
                # Stop the program on the ESC key or 'q'
            #     if keyCode == 27 or keyCode == ord('q'):
            #        break
            #    # take a screenshot
            #     if keyCode == 27 or keyCode == ord('y'):
            #         path = f'test_{i}.jpg'
            #         cv2.imwrite(path,img)
            #         print(f'image captured and path is {path}')
            #         i += 1
                    
        finally:
            video_capture.release()
            cv2.destroyAllWindows()
    else:
        print("Error: Unable to open camera")


if __name__ == "__main__":
    main()

