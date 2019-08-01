## Keyframer

A CLI tool to extract and present key frames from videos by sequentially comparing histograms.

### Dependencies

* Python 3  


* [OpenCV](https://pypi.org/project/opencv-python/)  
* [Pillow](https://pypi.org/project/Pillow/)  

### Setup

pip install -r "requirements.txt"

### Usage

`python keyframer.py INPUT [OPTIONS]`

```
usage: keyframer.py [-h] [-o OUTPUT] [-f FORMAT] [-s SENSITIVITY] [-p]
                    [-g GRIDSIZE GRIDSIZE]
                    INPUT

positional arguments:
  INPUT                 Input file or directory containing videos to be
                        processed.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output directory.
  -f {jpg,png,bmp}, --format {jpg,png,bmp}
                        Format of image frames.
  -s {low,normal,high}, --sensitivity {low,normal,high}
                        Sensitivity of comparison (higher is stricter).
                        Defaults to normal.
  -p, --purge           Remove frame and keyframe images to save space during
                        large processes.
  -g GRIDSIZE GRIDSIZE, --gridsize GRIDSIZE GRIDSIZE
                        Grid size of pdf image generated (WIDTH, HEIGHT).
                        Defaults to 3 by 3.
```

### TODO
 
- [ ] Implement progress bars  
- [ ] Potentially use threading to speed up frame r/w, or other solutions  
- [ ] Improve key frame detection  
- [x] Option to only get pdf (avoid storage issues when working with large files or batch processing)  
- [ ] End result formats other than pdf  
- [ ] Explore realtime scene change detection (ie directly grab key frames from a video to avoid writing frames)  
