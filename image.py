# from exif import Image


def get_exif(image_file_path):
    with open(image_file_path, "rb") as image_file:
        my_image = Image(image_file)
    if my_image.has_exif:
        return my_image.list_all()
    else:
        return None


if __name__ == "__main__":
    # exif = get_exif("WindowsXP.jpg")
    # print(exif)
    from PIL import Image, ExifTags

    img = Image.open("WindowsXP.jpg")
    img_exif = img.getexif()

    if img_exif is None:
        print('Sorry, image has no exif data.')
    else:
        for key, val in img_exif.items():
            if key in ExifTags.TAGS:
                print(f'{ExifTags.TAGS[key]}:{val}')
            else:
                print(f'{key}:{val}')
