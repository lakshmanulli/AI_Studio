from video_generator import VideoGenerator
from video_models.ltx_video import LTXVideo

generator = VideoGenerator(LTXVideo())

video_path = generator.generate_video(
    prompt="A futuristic AI robot walking through a cyberpunk city",
    filename="robot.mp4"
)

print("Video saved at:", video_path)