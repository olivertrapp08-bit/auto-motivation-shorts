import random
from moviepy.editor import ImageClip, AudioFileClip, TextClip, CompositeVideoClip

# QUOTES LADEN
with open("quotes.txt", "r", encoding="utf-8") as f:
    quotes = f.readlines()

quote = random.choice(quotes).strip()

# DATEIEN
image_path = "background.jpg"
audio_path = "music.mp3"

audio = AudioFileClip(audio_path)
video = ImageClip(image_path).set_duration(audio.duration)

text = TextClip(
    quote,
    fontsize=70,
    color="white",
    size=video.size,
    method="caption"
).set_duration(audio.duration)

final = CompositeVideoClip([video, text.set_position("center")])
final = final.set_audio(audio)

final.write_videofile("output.mp4", fps=24)
