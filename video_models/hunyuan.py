from base import BaseVideoGenerator


class HunyuanVideo(BaseVideoGenerator):

    def load_model(self):

        print("Loading Hunyuan Video")

    def generate(
        self,
        prompt,
        output_path
    ):

        print("Generating with Hunyuan")

        with open(output_path, "w") as file:

            file.write(
                "Dummy Video"
            )