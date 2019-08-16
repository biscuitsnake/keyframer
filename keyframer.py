import argparse
import sys
import os
import shutil

from modules.frames import get_frames
from modules.keyframes import image_comparison, by_interval
from modules.pdf import create_pdf


def get_args():
    parser = argparse.ArgumentParser(prog="keyframer.py")

    parser.add_argument("input", metavar="INPUT",
                        help="Input file or directory containing videos to be processed.")
    parser.add_argument("-o", "--output",
                        help="Output directory.")
    parser.add_argument("-i", "--interval", type=int,
                        help="Get key frames every x seconds rather than through comparison.")
    parser.add_argument("-f", "--format", default="jpg", choices=['jpg', 'png', 'bmp'],
                        help="Format of image frames.")
    parser.add_argument("-s", "--sensitivity", default="normal", choices=['low', 'normal', 'high'],
                        help="Sensitivity of comparison (higher is stricter). Defaults to normal.")
    parser.add_argument("-p", "--purge", action="store_true",
                        help="Remove frame and keyframe images to save space during large processes.")
    parser.add_argument("-g", "--gridsize", default=[3, 3], nargs=2, type=int,
                        help="Grid size of pdf image generated (WIDTH, HEIGHT). Defaults to 3 by 3.")
    return parser.parse_args()


def purge(root, input_path, filename):
    shutil.move(os.path.join(input_path, filename), os.path.join(root, filename))
    shutil.rmtree(input_path)


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
        name = os.path.basename(os.path.normpath(video))
        path = os.path.join(output_path, name)
        os.makedirs(os.path.join(path, "keyframes"), exist_ok=True)
        os.makedirs(os.path.join(path, "frames"), exist_ok=True)

        sys.stdout.write("{}: extracting frames...".format(name))
        sys.stdout.flush()
        get_frames(video, path, args.format)

        sys.stdout.write(" extracting keyframes...")
        sys.stdout.flush()
        if args.interval:
            by_interval(path, args.interval)
        else:
            image_comparison(path, args.sensitivity)

        sys.stdout.write(" creating pdf...")
        sys.stdout.flush()
        create_pdf(args.gridsize[0], args.gridsize[1], path, name)

        if args.purge:
            purge(output_path, path, name+".pdf")
        sys.stdout.write(" done!\n")

    print("Successfully processed {} videos to {}.".format(len(videos), output_path))


if __name__ == "__main__":
    main()
