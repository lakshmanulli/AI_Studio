from .base import BaseVideoGenerator


class CogVideoX(BaseVideoGenerator):

    def load_model(self):

        print("Loading CogVideoX...")

    def generate(
        self,
        prompt,
        output_path
    ):

        print("Generating with CogVideoX")

        with open(output_path, "w") as file:

            file.write(
                "Dummy Video"
            )
