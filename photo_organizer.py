import utils
import pickle

# example: '/run/media/durval/HD-EXTERNO/A_FOTOS/'
ORIGIN_PATH = 'ADD WHERE SHOULD I SEARCH PHOTOS'

# example: '/run/media/durval/HD-EXTERNO/RESULT_FOTOS/'
RESULT_PATH = 'ADD WHERE SHOULD I PUT PROCESSED PHOTOS'

all_pics_paths = utils.get_all_files(ORIGIN_PATH)

for pic_path in all_pics_paths:
    img_date = utils.get_img_date(pic_path)
    utils.move_file_to_right_dir(RESULT_PATH, pic_path, img_date)