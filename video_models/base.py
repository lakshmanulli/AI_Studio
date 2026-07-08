"""
Base class for all video generation models.
"""

from abc import ABC, abstractmethod


class BaseVideoGenerator(ABC):

    @abstractmethod
    def load_model(self):
        """Load the AI model."""
        pass

    @abstractmethod
    def generate(
        self,
        prompt: str,
        output_path: str
    ):
        """Generate a video."""
        pass