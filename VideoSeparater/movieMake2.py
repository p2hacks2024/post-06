import cv2
import os

def split_video_into_clips(video_path, output_dir, interval):
    cap = cv2.VideoCapture(video_path)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 出力形式を指定

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    clip_count = 25
    frame_count = 0
    out = None

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        if frame_count % interval == 0:
            if out is not None:
                out.release()

            output_video_path = os.path.join(output_dir, f"clip_{clip_count}.mp4")
            out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
            clip_count += 1
            print(f"Started new clip {clip_count}")

        out.write(frame)
        frame_count += 1

    if out is not None:
        out.release()

    cap.release()

video_path = 'a~n.mp4'
output_dir = 'output_clips'
interval = 33  # 指定したフレームで分割

split_video_into_clips(video_path, output_dir, interval)
