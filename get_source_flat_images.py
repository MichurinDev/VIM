import os

pre_source = "https://raw.githubusercontent.com/MichurinDev/VIM/master/flats"

with open("flat_image_source.txt", "w", encoding="utf-8") as f:
    for dir in os.listdir("flats"):
        image_srcs = list(map(lambda x: f'<img src="{pre_source}/{dir}/{x}">', list(filter(lambda x: "pdf" not in x, [file for file in os.listdir(f"flats/{dir}")]))))
        f.write(" ".join(image_srcs) + "\n")
