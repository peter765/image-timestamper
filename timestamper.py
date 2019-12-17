import os
from PIL import Image, ImageDraw, ImageFont
from PIL.ExifTags import TAGS


def file_processor(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        with Image.open(os.path.join(input_dir,filename)) as im:
            # extract EXIF timestamp
            # from https://stackoverflow.com/questions/765396/exif-manipulation-library-for-python/765403#765403
            info = im._getexif()
            exif = {}
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                exif[decoded] = value
            exif_time = exif.get('DateTime')
            
            # Write timestamp onto image and save into destination folder
            width, height = im.size
            d = ImageDraw.Draw(im)
            font = ImageFont.truetype("arial.ttf", 75)

            d.text((width-800, height-100), exif_time, fill='red', font=font)
            print("Processing image: " + filename)
            im.save(os.path.join(output_dir, filename))


if __name__ == "__main__":
    INPUT_DIR = "iCloud Photos"
    OUTPUT_DIR = INPUT_DIR + "_output"
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    file_processor(INPUT_DIR, OUTPUT_DIR)