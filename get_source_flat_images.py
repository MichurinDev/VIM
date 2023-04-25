import os
from PIL import Image


def watermark(path):
    img = Image.open(path)
    watermark_img = Image.open("D://Personal//VIM//Квартиры на публикацию//Logo VIM 1.0.png")

    (width1, height1) = img.size
    (width2, height2) = watermark_img.size
    up_margin, bottom_margin, left_margin, right_margin = \
        10, 10, 10, 10

    img.paste(watermark_img, (
        width1 - width2 - bottom_margin,
        height1 - height2 - right_margin),  watermark_img)

    img.save(path)

    return "Вотермарка наложена"


def get_height(width, height):
    return int(round(height * 850 / width))


def change_img_size(path):
    img = Image.open(path)

    width, height = img.size
    new_height = get_height(width, height)
    new_image = img.resize((850, new_height))

    new_image.save(path)

    return "Изображение сжато"


def get_img_tag():
    pre_source = \
        "https://raw.githubusercontent.com/MichurinDev/VIM/master/flats"

    with open("flat_image_source.txt", "w", encoding="utf-8") as f:
        for dir in os.listdir("flats"):
            image_srcs = list(
                map(lambda x: f'<img src="{pre_source}/{dir}/{x}">',
                    list(filter(
                        lambda x: "pdf" not in x,
                        [file for file in os.listdir(f"flats/{dir}")]))))

            f.write(" ".join(image_srcs) + "\n")

    return "Тэги получены"


for i, dir in enumerate(os.listdir("flats")):
    for j, file in enumerate(os.listdir(f"flats/{dir}")):
        path = f"flats/{dir}/{file}"
        if path.split('.')[-1].lower() in ["png", "jpg", "jpeg"]:
            print(f'{i + 1}/{len(os.listdir("flats"))} | {j + 1}/{len(os.listdir(f"flats/{dir}"))}')
            print(change_img_size(path))
            print(watermark(path))
            print()
