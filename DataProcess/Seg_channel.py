import os

import tifffile


def run(path_dir):
    fileList = os.listdir(path_dir)
    for name in fileList:
        image_path = os.path.join(path_dir, name)
        image = tifffile.imread(image_path)
        confocal = image[0]
        STED = image[1]
        id = os.path.splitext(name)[0].split('_')[1]
        new_name = 'img_{:04d}.tif'.format(int(id))
        GT_Path = os.path.join(GT_dir, new_name)
        low_Path = os.path.join(low_dir, new_name)
        tifffile.imwrite(GT_Path, STED)
        tifffile.imwrite(low_Path, confocal)


if __name__ == '__main__':
    img_dir = r'D:\Data\backups\TAGAN\AxonaRingsDataset\train'
    sav_dir = r'D:\Data\backups\TAGAN\NewAxonal\train'
    GT_dir = os.path.join(sav_dir, 'GT')
    low_dir = os.path.join(sav_dir, 'low')
    if not os.path.exists(GT_dir):
        os.makedirs(GT_dir)
    if not os.path.exists(low_dir):
        os.makedirs(low_dir)

    run(img_dir)
