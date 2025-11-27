import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

VIDEO_PATH = "output/short.mp4"

def upload_video():
    if not os.path.exists(VIDEO_PATH):
        raise FileNotFoundError("No video available! Run generate_video.py")

    creds = Credentials.from_authorized_user_file("token.json", ["https://www.googleapis.com/auth/youtube.upload"])
    youtube = build("youtube", "v3", credentials=creds)

    request_body = {
        "snippet": {
            "title": "Motivation for Future Millionaires 💸🔥",
            "description": "Daily shorts to level up your life & money game! #motivation #finance",
            "tags": ["Motivation", "Finance", "Wealth", "Mindset", "Success"]
        },
        "status": {"privacyStatus": "public"}
    }

    media = MediaFileUpload(VIDEO_PATH)

    upload = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )
    response = upload.execute()

    print("Video uploaded successfully!")
    print("Video ID:", response["id"])

if __name__ == "__main__":
    upload_video()
