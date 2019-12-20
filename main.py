from script.reduce_color_palette import ReduceColor
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-start', dest="reduce_color", nargs=2, help='reduce color palette', metavar=("filename", "n_color"))
    args = parser.parse_args()
    filename, n = args.reduce_color
    ReduceColor(filename, int(n)).start()
    exit()
