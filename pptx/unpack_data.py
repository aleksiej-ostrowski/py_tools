# -*- coding: utf-8 -*-

#----------------------------#
#                            #
#  Version 0.0.1             #
#  Ostrovsky Alexey, 2016    #
#  0x0all@gmail.com          #
#                            #
#----------------------------#

filename = "results_tyum_20160801_20160807.zip"
t = filename.split('.')[0].split('_')
dir_ = '_'.join(t[2:4])

import os
os.makedirs(dir_)

import zipfile

zip_ref = zipfile.ZipFile(filename, 'r')
zip_ref.extractall("./" + dir_)
zip_ref.close()

exit()

d = "./%s/ppt/embeddings/" % fn[0]
d2 = d + "*.xlsx"

import glob

files = glob.glob(d2)

for fn in files:
    a = fn.split('/')[-1].split('.')[0]
    new_ = d + a
    os.makedirs(new_)

    zip_ref2 = zipfile.ZipFile(fn, 'r')
    zip_ref2.extractall(new_)
    zip_ref2.close()

    # ./1/ppt/embeddings/_____Microsoft_Excel3.xlsx
    print fn 

    os.remove(fn)


