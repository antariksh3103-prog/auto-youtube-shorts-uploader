import os
from moviepy.editor import *
import random

SCRIPT_PATH = "output/script.txt"
AUDIO_PATH = "output/voice.mp3"
VIDEO_PATH = "output/short.mp4"

BACKGROUND_VIDEOS = [
    "assets/bg1.mp4",
    "assets/bg2.mp4",
    "assets/bg3.mp4"
]

def generate_video():
    if not os.path.exists(SCRIPT_PATH) or not os.path.exists(AUDIO_PATH):
        raise FileNotFoundError("Missing script or voice file!")

    # Read script
    with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    # Background video
    bg_video = VideoFileClip(random.choice(BACKGROUND_VIDEOS)).subclip(0, 35)
    bg_video = bg_video.resize(height=1920).fx(vfx.crop, width=1080)

    # Voice audio
    audio = AudioFileClip(AUDIO_PATH)

    # Subtitles overlay
    txt = TextClip(
        text,
        fontsize=70,
        color="white",
        stroke_color="black",
        stroke_width=3,
        method="caption",
        size=(1000, 1600),
        align="center"
    ).set_duration(audio.duration).set_position("center")

    # Combine
    final = CompositeVideoClip([bg_video, txt]).set_audio(audio)
    final.write_videofile(VIDEO_PATH, fps=30)

    print("Short created:", VIDEO_PATH)
    return VIDEO_PATH

if __name__ == "__main__":
    generate_video()
