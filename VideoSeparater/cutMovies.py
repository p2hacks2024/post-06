import os
from moviepy.video.io.VideoFileClip import VideoFileClip

input_folder = 'output_clips'
output_folder = 'trimmed_clips'
start_trim_time = 0.4  # 前をカットする時間（秒）
end_trim_time = 0.6    # 後ろをカットする時間（秒）

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        with VideoFileClip(input_path) as video:
            duration = video.duration
            
            # 前を0.4秒、後ろを0.6秒カットした新しいクリップを作成
            trimmed_video = video.subclip(start_trim_time, duration - end_trim_time)
            
            trimmed_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

print("全ての動画を前後カットして保存しました。")

