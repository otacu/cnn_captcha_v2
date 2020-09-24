# -*- coding: UTF-8 -*-
"""
ʹ��captcha lib������֤�루ǰ�᣺pip install captcha��
"""
from captcha.image import ImageCaptcha
import os
import random
import time
import json


def gen_special_img(text, file_path, width, height):
    # ����img�ļ�
    generator = ImageCaptcha(width=width, height=height)  # ָ����С
    img = generator.generate_image(text)  # ����ͼƬ
    img.save(file_path)  # ����ͼƬ


def gen_ima_by_batch(root_dir, image_suffix, characters, count, char_count, width, height):
    # �ж��ļ����Ƿ����
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)

    for index, i in enumerate(range(count)):
        text = ""
        for j in range(char_count):
            text += random.choice(characters)

        timec = str(time.time()).replace(".", "")
        p = os.path.join(root_dir, "{}_{}.{}".format(text, timec, image_suffix))
        gen_special_img(text, p, width, height)

        print("Generate captcha image => {}".format(index + 1))


def main():
    with open("conf/captcha_config.json", "r") as f:
        config = json.load(f)
    # ���ò���
    root_dir = config["root_dir"]  # ͼƬ����·��
    image_suffix = config["image_suffix"]  # ͼƬ�����׺
    characters = config["characters"]  # ͼƬ����ʾ���ַ��� # characters = "0123456789abcdefghijklmnopqrstuvwxyz"
    count = config["count"]  # ���ɶ���������
    char_count = config["char_count"]  # ͼƬ�ϵ��ַ�����

    # ����ͼƬ�߶ȺͿ��
    width = config["width"]
    height = config["height"]

    gen_ima_by_batch(root_dir, image_suffix, characters, count, char_count, width, height)


if __name__ == '__main__':
    main()
