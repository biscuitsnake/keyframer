import argparse
import os

from modules.frames import get_frames
from modules.keyframes import image_comparison
from modules.pdf import create_pdf


def get_args():

    parser = argparse.ArgumentParser(prog="keyframer.py")

    parser.add_argument("input", metavar="INPUT",
                        help="Input file or directory containing videos to be processed.")
    parser.add_argument("-o", "--output",
                        help="Output directory.")
    parser.add_argument("-f", "--format", default="jpg",
                        help="Format of image frames (affects speed of processing.")
    parser.add_argument("-s", "--sensitivity", default="normal",
                        help="Sensitivity of comparison [low|normal|high]. Defaults to normal.")
    parser.add_argument("-p", "--pdf", default="True",
                        help="Generate pdf containing image grid of key frames. Defaults to True.")
    parser.add_argument("-g", "--gridsize", default=[3, 3], nargs=2, type=int,
                        help="Grid size of pdf image generated [width, length]. Default: 3 by 3.")
    return parser.parse_args()


def main():
    args = get_args()
    root = os.getcwd()

    if os.path.isdir(args.input):
        videos = [os.path.join(os.path.abspath(args.input), v) for v in os.listdir(args.input)
                  if v.endswith(('.mp4', '.avi', '.mov', 'flv', '.wmv'))]
    elif os.path.isfile(args.input):
        videos = [os.path.abspath(args.input)]
    else:
        raise Exception("Input not found.")

    if args.output:
        output_path = os.path.abspath(args.output)
    else:
        output_path = os.path.join(root, "output")

    for video in videos:
        path = os.path.join(output_path, os.path.basename(os.path.normpath(video)))
        os.makedirs(os.path.join(path, "keyframes"), exist_ok=True)
        os.makedirs(os.path.join(path, "frames"), exist_ok=True)
        get_frames(video, path, args.format)
        image_comparison(path, args.sensitivity)
        if args.pdf:
            create_pdf(args.gridsize[0], args.gridsize[1], path)


if __name__ == "__main__":
    main()
