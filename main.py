from PIL import Image
import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, help="path of the single file")
    parser.add_argument(
        "--path",
        type=str,
        help="path for jfif folder. \
                        Will overwrite --file if --path is given.",
    )
    parser.add_argument(
        "--output",
        type=str,
        help='Output folder. If not given, will make an "output" folder \
            in the same directory of the file or inside the path. \
                Will make the directory if does not exist ',
    )

    args = parser.parse_args()
    file = args.file
    path = args.path
    output = args.output

    if not output:
        if path:
            output = os.path.join(path, "output")
        elif file:
            output = os.path.join(os.path.dirname(file), "output")
        else:
            raise Exception("No arguments given!")

    if not os.path.exists(output):
        os.makedirs(output)

    if path:
        if not os.path.exists(path):
            raise Exception("Path does not exist!")
        count = 0
        for root, _, files in os.walk(path):
            for file in files:
                if file.lower().endswith(".jfif"):
                    img = Image.open(os.path.join(root, file))
                    file_name = os.path.splitext(file)[0]
                    img.save(os.path.join(output, file_name + ".jpg"))
    elif file:
        if not os.path.isfile(file):
            raise Exception("File does not exist!")

        img = Image.open(file)
        file_name = os.path.splitext(os.path.basename(file))[0]
        img.save(os.path.join(output, file_name + ".jpg"))
    else:
        print("Path nor file given")

    print("Converted! ..or nah?")
