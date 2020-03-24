import subprocess

from os import listdir
from os.path import isdir


CURRENT_WORKING_DIR = '.'
RUST_NON_ROOT_IMAGE = 'rust-non-root'
NAMESPACE = 'nitinbhojwani'


def get_rust_dirs(dir_path):
    return [filepath for filepath in listdir(dir_path) if isdir(filepath) and filepath.startswith('rust')]


def get_image_tag(rust_dir_name):
    return '{}/{}:{}'.format(NAMESPACE, RUST_NON_ROOT_IMAGE, rust_dir_name.split('-')[1])


def build_images(rust_dirs):
    for dir in rust_dirs:
        resp = subprocess.run(
            'docker build -t {} {}'.format(get_image_tag(dir), dir), shell=True)


def push_images(rust_dirs):
    for dir in rust_dirs:
        resp = subprocess.run(
            'docker push {}'.format(get_image_tag(dir)), shell=True)


def build_and_push_images():
    rust_dirs = get_rust_dirs(CURRENT_WORKING_DIR)
    build_images(rust_dirs)
    push_images(rust_dirs)


if __name__ == '__main__':
    build_and_push_images()
