"""
video_generator.py

Main Video Generator Controller
"""

import os


class VideoGenerator:

    def __init__(self, provider):

        self.provider = provider

        self.provider.load_model()

        os.makedirs(
            "generated_videos",
            exist_ok=True
        )

    def generate_video(
        self,
        prompt,
        filename="video.mp4"
    ):

        if not prompt:

            raise ValueError(
                "Prompt cannot be empty."
            )

        output_path = os.path.join(
            "generated_videos",
            filename
        )

        self.provider.generate(
            prompt,
            output_path
        )

        return output_path