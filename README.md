# image-timestamper
Adds timestamps to images in source folder.

Basic script that iterates through a source directory and adds in a timestamp to each image, just in case you need it. 

The timestamp reads from the image's EXIF data and "writes" the EXIF data in red at the bottom right, like an old style photo. 

Made this in about 15 minutes or so, so it's pretty rough, but I hope it's helpful to someone out there!

Missing features:
- scaling text size based on input size photo.
- not tested on PNG, TIFF, GIF, HEIC etc
- hardcoded values for input and output folder. Change in __main__ 

