from PIL import Image
import argparse
import settings as st
import sys

def convert_one(name_in: str, name_out: str, show_msg: bool = False):
    file_out_ext = name_out.split('.')[-1]
    Image.open(name_in).convert("RGB").save(name_out, file_out_ext)

    if show_msg:
        print(f"File {name_in} converted to {file_out_ext} with name {name_out}")


def convert_many(ext_from: str, ext_to: str, dir_in: str = '.', dir_out: str = '.'):
    import os

    files = [file for file in os.listdir(dir_in) if file.split('.')[-1] == ext_from]

    if not files:
        raise Exception(f"Not found any file with '{ext_from}' extension")

    for file in files:
        try:
            out_file = dir_out + '/' + file.split('.')[0] + '.' + ext_to
            in_file = dir_in + '/' + file
            convert_one(in_file, out_file)

        except Exception as e:
            print(f"Can not convert '{file}' to '{out_file}'.")

        else:
            print(f"Converted {len(files)} images")


def choose_mode(line_args: argparse.Namespace):
    line_in = getattr(line_args, 'in', None)
    line_out = getattr(line_args, 'out', None)

    if line_in and line_out:
        convert_one(line_in, line_out, show_msg=True)

    ext_from = getattr(line_args, 'from', None)
    ext_to = getattr(line_args, 'to', None)
    dir_in = getattr(line_args, 'source')
    dir_out = getattr(line_args, 'dist')

    if ext_from and ext_to:
        convert_many(ext_from=ext_from, ext_to=ext_to, dir_in=dir_in, dir_out=dir_out)

def main():
    parser = argparse.ArgumentParser(description=st.program_description, prog=st.program_name, epilog=st.program_epilog)
    parser.add_argument('--version', action='version', version=st.program_version)
    parser.add_argument('-i', '--in', help="Input filename")
    parser.add_argument('-o', '--out', help="Output filename")
    parser.add_argument('-f', '--from', help="Convert all images with given extension. Don't work without '--to' argument")
    parser.add_argument('-t', '--to', help="Convert all images to given extension. Don't work without '--from' argument")
    parser.add_argument('-s', '--source', help="Where take files to convert. Works only with multiple conversion")
    parser.add_argument('-d', '--dist', help="Place converted files to DIST. Works only with multiple conversion")

    args = parser.parse_args()
    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)

    choose_mode(args)


if __name__ == "__main__":
    main()
