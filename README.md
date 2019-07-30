## Keyframer

### Dependencies

* Python 3


* [OpenCV](https://pypi.org/project/opencv-python/)
* [Pillow](https://pypi.org/project/Pillow/)

### Setup

pip install -r "requirements.txt"

### Usage

`python keyframer.py INPUT [OPTIONS]`

```
usage: keyframer.py [-h] [-o OUTPUT] [-f FORMAT] [-s SENSITIVITY] [-p PDF]
                    [-g GRIDSIZE]
                    INPUT

positional arguments:
  INPUT                 Input file or directory containing videos to be
                        processed.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output directory.
  -f FORMAT, --format FORMAT
                        Format of image frames (affects speed of processing.
  -s SENSITIVITY, --sensitivity SENSITIVITY
                        Sensitivity of comparison [low|normal|high]. Defaults
                        to normal.
  -p PDF, --pdf PDF     Generate pdf containing image grid of key frames.
                        Defaults to True.
  -g GRIDSIZE, --gridsize GRIDSIZE
                        Grid size of pdf image generated [width, length].
                        Default: 3 by 3.  
```


