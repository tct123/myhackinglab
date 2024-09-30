from exif import Image


def get_exif(image_file_path):
    with open(image_file_path, "rb") as image_file:
        my_image = Image(image_file)
    if my_image.has_exif:
        return dir(my_image)
    else:
        return None


if __name__ == "__main__":
    exif = get_exif("WindowsXP.jpg")
    print(exif)
