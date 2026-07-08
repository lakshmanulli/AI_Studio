from base import BaseVideoGenerator


class Wan21(BaseVideoGenerator):

    def load_model(self):

        print("Loading Wan2.1")

    def generate(
        self,
        prompt,
        output_path
    ):

        print("Generating with Wan2.1")

        with open(output_path, "w") as file:

            file.write(
                "Dummy Video"
            )