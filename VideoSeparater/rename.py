import os
import re

vowels = ['a', 'i', 'u', 'e', 'o', 'n']
rename_list = [f'{v1}{v2}.mp4' for v1 in vowels for v2 in vowels]

folder = 'trimmed_clips'

# クリップファイルのリストを取得して、番号順にソート
files = [f for f in os.listdir(folder) if f.endswith(".mp4")]
files.sort(key=lambda f: int(re.findall(r'\d+', f)[0]))

# clip_0 から順にファイルをリネーム
for i, filename in enumerate(files):
    if i >= len(rename_list):
        print(f"ファイルが多すぎます。リネームリストには {len(rename_list)} 個の名前しかありません。")
        break

    old_path = os.path.join(folder, filename)
    new_path = os.path.join(folder, rename_list[i])
    
    os.rename(old_path, new_path)

print("全てのファイルを番号順と五十音順にリネームしました。")
