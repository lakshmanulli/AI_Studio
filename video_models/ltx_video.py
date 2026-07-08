"""
LTX Video Generator
"""

import torch

from diffusers import LTXPipeline
from diffusers.utils import export_to_video

from .base import BaseVideoGenerator

from config import (
    VIDEO_WIDTH,
    VIDEO_HEIGHT,
    VIDEO_NUM_FRAMES,
    VIDEO_INFERENCE_STEPS,
    VIDEO_FPS,
)


class LTXVideo(BaseVideoGenerator):

    def __init__(self):

        self.pipeline = None

    def load_model(self):

        print("Loading LTX Video Model...")

        self.pipeline = LTXPipeline.from_pretrained(
            "Lightricks/LTX-Video",
            torch_dtype=torch.bfloat16
        )

        self.pipeline.to("cuda")

        print("Model Loaded Successfully!")

    def generate(
        self,
        prompt,
        output_path
    ):

        print("Generating Video...")

        negative_prompt = (
            "worst quality, blurry, distorted, jittery"
        )

        result = self.pipeline(

            prompt=prompt,

            negative_prompt=negative_prompt,

            width=VIDEO_WIDTH,

            height=VIDEO_HEIGHT,

            num_frames=VIDEO_NUM_FRAMES,

            num_inference_steps=VIDEO_INFERENCE_STEPS

        )

        video = result.frames[0]

        export_to_video(
            video,
            output_path,
            fps=VIDEO_FPS
        )

        print("Video Saved:", output_path)