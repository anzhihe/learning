import os
import argparse

def rename(file_path, old_ext):

    print(old_ext)
    old_names = os.listdir(file_path)
    new_name = 1

    for old_name in old_names:

        if old_name.endswith(old_ext):

            old_path = os.path.join(file_path, old_name)
            new_path = os.path.join(file_path, str(new_name)+".JPG")
            os.rename(old_path, new_path)
            new_name = int(new_name)+1

def args_opt():

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", required=True, help="path to rename")
    parser.add_argument("-e", "--ext", required=True, help="files name extension, eg: jpg")
    return  parser.parse_args()


if __name__ == "__main__":

    args = args_opt()
    rename(args.path, "."+args.ext)
    print(os.listdir(args.path))
    #  ['3.JPG', '2.JPG', '1.JPG', 'xyz.bmp']

# python3 rename_v2.py -p /Users/edz/Desktop/pic -e jpg