from os import walk, path, makedirs
from PIL.JpegImagePlugin import JpegImageFile
from PIL.GifImagePlugin import GifImageFile
from PIL import Image
from PIL.ExifTags import TAGS
from shutil import copy2

def get_img_date(img_path):
    ext = img_path.split('.')[-1]
    ext = ext.lower()
    
    # You may need to add more extensions to this tuple, according to the files in your directory
    not_supported = ('dcr', 'mov', 'db', 'docx', 'ini', 'avi', 'nef', 'xml', 'aae', 'mp4', 'mts', 'sfk', 'wma', 'mp3', 'rar', 'exe', 'htm', 'bin', 'heic', 'ppsx', 'gif')
    
    if ext in not_supported: return None
    
    img = Image.open(img_path)

    # if isinstance(img, GifImageFile): return None
    
    info = img._getexif()

    # TODO: Move to another DIR
    if(info == None): return None

    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        if decoded == 'DateTime':
            return '-'.join(value.split()[0].split(':')[:2])

def get_all_files(dir_path):
    files = []
    for rel_path, _, dir_files in walk(dir_path):
        dir_files = [path.join(rel_path, file) for file in dir_files]
        files += dir_files
    return files

def move_file_to_right_dir(base_dir, img_path, img_date):
    
    if img_date is None:
        dir_path = path.join(base_dir, 'fail')

    else:
        dir_path = path.join(base_dir, 'success', img_date)

    if not path.isdir(dir_path):
        makedirs(dir_path)

    copy2(img_path, dir_path)
