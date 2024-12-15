import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import webbrowser

folder = 'trimmed_clips'

input_string = 'oaou'

# 隣り合った文字のペアを作成
pairs = [input_string[i:i+2] + '.mp4' for i in range(len(input_string) - 1)]
print(pairs)

clips = []
for pair in pairs:
    file_path = os.path.join(folder, pair)

    if os.path.exists(file_path):
        try:
            clips.append(VideoFileClip(file_path, fps_source='fps'))
        except Exception as e:
            print(f"エラーが発生しました: {e}")
    else:
        print(f"{pair} が存在しません。")

if clips:
    final_clip = concatenate_videoclips(clips)
    
    final_clip.write_videofile('combined_output.mp4', codec="libx264", audio_codec="aac")

print("動画をファイルとして保存しました。")

video_path = 'combined_output.mp4'

if os.path.exists(video_path):
    webbrowser.open(video_path)
else:
    print(f"{video_path} が存在しません。")
