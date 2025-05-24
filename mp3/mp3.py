
from pytube import YouTube

def download_video(url, path="downloads"):
    try:
        # 建立 YouTube 物件
        yt = YouTube(url)
        
        # 選擇最高解析度的影片
        stream = yt.streams.get_lowest_resolution()
        
        # 開始下載
        print(f"Downloading {yt.title}...")
        stream.download(output_path=path)
        print("Download completed!")
        
    except Exception as e:
        print("An error occurred:", e)

# 輸入影片的網址
url = input()
download_video(url)
