import utils
import pickle

# example: '/run/media/durval/HD-EXTERNO/A_FOTOS/'
ORIGIN_PATH = '/media/durval/HD-EXTERNO/HP-All-in-One'

# example: '/run/media/durval/HD-EXTERNO/RESULT_FOTOS/'
RESULT_PATH = '/media/durval/HD-EXTERNO/HP-All-in-One/organizado'

all_pics_paths = utils.get_all_files(ORIGIN_PATH)
total = len(all_pics_paths)

for idx, pic_path in enumerate(all_pics_paths):
    percent = (idx/total) * 100
    print(f'{round(percent, 2)} %')
    img_date = utils.get_img_date(pic_path)
    utils.move_file_to_right_dir(RESULT_PATH, pic_path, img_date)