import os
from pytube import YouTube

video_links_list = []

def ask_links():
    num_of_links = input("Enter the number of videos you want to download: ")
    if num_of_links.isdigit():
        num_of_links = int(num_of_links)
    else:
        print("Please enter a number.")
        ask_links()
    
    print("Enter the links of the video you want to download")
    for i in range(num_of_links):
        link = input(f"LINK {i + 1}/{num_of_links}: ")
        video_links_list.append(link)

def download_videos(video_links):
    current_directory = os.getcwd()

    for link in video_links:
        try:
            yt = YouTube(link)
            video = yt.streams.filter(file_extension="mp4", progressive=True).first()

            print(f"\nDownloading: {yt.title}")
            
            # Construct the output path for each video in the current directory
            video_path = os.path.join(current_directory, f"{yt.title}.mp4")
            
            video.download(video_path)
            print(f"\nDownload completed! Saved to: {video_path}")
        except Exception as e:
            print(f"\nAn error occurred for video {link}: \n{e}")

def start():
    ask_links()
    download_videos(video_links_list)

if __name__ == "__main__":
    start()
