import cv2
import os

def extract_frames(path,op_folder,pose_type):
    cap = cv2.VideoCapture(path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

    n = 5
    frame_interval = frame_count // (n-1)
    frame_number = 0
    frames_extracted = 0

    output_dir = f'D:\OpenCV Practice\Comparative_Study\comp_study\output_frames\{op_folder}'
    os.makedirs(output_dir, exist_ok=True)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_number % frame_interval == 0 or frame_number == frame_count - 1:
            frame_filename = os.path.join(output_dir, f'1_{pose_type}_{frames_extracted:04d}.jpg')
            cv2.imwrite(frame_filename, frame)
            frames_extracted += 1

        frame_number += 1

        if frames_extracted == n:
            break

    cap.release()
    cv2.destroyAllWindows()

    print(f"{n} frames extracted and saved to {output_dir}")

extract_frames(r'D:\OpenCV Practice\Comparative_Study\comp_study\Front\1_sit_vid_main.mp4','Front','sit')
extract_frames(r'D:\OpenCV Practice\Comparative_Study\comp_study\Front\1_stand_vid_main.mp4','Front','stand')
extract_frames(r'D:\OpenCV Practice\Comparative_Study\comp_study\Side\1_sit_vid_main.mp4','Side','sit')
extract_frames(r'D:\OpenCV Practice\Comparative_Study\comp_study\Side\1_stand_vid_main.mp4','Side','stand')
extract_frames(r'D:\OpenCV Practice\Comparative_Study\comp_study\Angle\1_sit_vid_main.mp4','Angle','sit')
extract_frames(r'D:\OpenCV Practice\Comparative_Study\comp_study\Angle\1_stand_vid_main.mp4','Angle','stand')