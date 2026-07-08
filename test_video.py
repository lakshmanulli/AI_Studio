from video_generator import VideoGenerator

from video_models.ltx_video import LTXVideo


generator = VideoGenerator(
    LTXVideo()
)

generator.generate_video(

    prompt="""
A futuristic AI robot walking
through a cyberpunk city
at night with neon lights,
cinematic camera movement,
high quality.
""",

    filename="robot.mp4"
)