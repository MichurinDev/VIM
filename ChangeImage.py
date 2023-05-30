import os
from PIL import Image
import csv
import random


def watermark(path):
    img = Image.open(path)
    watermark_img = Image.open("./Logo VIM 1.0.png")

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


def get_img_tag(origin):
    pre_source = \
        "https://raw.githubusercontent.com/MichurinDev/VIM/master/flats"

    with open("flat_image_source.txt", "w", encoding="utf-8") as f:
        for dir in os.listdir(origin):
            image_srcs = list(
                map(lambda x: f'<img src="{pre_source}/{dir}/{x}">',
                    list(filter(
                        lambda x: "txt" not in x,
                        [file for file in os.listdir(f"{origin}/{dir}")]))))

            f.write(" ".join(image_srcs) + "\n")

    return "Тэги получены"


def MakeDirectory(origin):
    with open('./flats2.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for index, row in enumerate(reader):

            if index != 0:
                path = f"{origin}/{' '.join(row[1:9]).lower()}_{''.join([random.choice('abcdifghijklmnopqrstuvqxwz1234567890') for _ in range(10)])}"
                os.makedirs(path)

                with open(f"{path}/link.txt", "w") as f:
                    f.write(row[-1])
                    f.close()

    print("Директории созданы")


origin = "new_flats"
exceptions = ['комфорт двухкомнатная 50-100 современный светлая холодное яркая семья ( пара+1)_alwgmczmiz']

for i, dir in enumerate(os.listdir(origin)):
    for j, file in enumerate(os.listdir(f"{origin}/{dir}")):
        path = f"{origin}/{dir}/{file}"
        if path.split('.')[-1].lower() in ["png", "jpg", "jpeg"]:
            print(f'{i + 1}/{len(os.listdir(origin))} | \
                  {j + 1}/{len(os.listdir(f"{origin}/{dir}"))}')
            print(change_img_size(path))
            if dir not in exceptions:
                print(watermark(path))
            print()

print(get_img_tag(origin))
