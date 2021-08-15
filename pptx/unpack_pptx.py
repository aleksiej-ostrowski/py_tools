# -*- coding: utf-8 -*-

#----------------------------#
#                            #
#  Version 0.0.1             #
#  Ostrovsky Alexey, 2016    #
#  0x0all@gmail.com          #
#                            #
#----------------------------#

filename = "ideal.pptx"
fn = filename.split('.')

import os
os.makedirs(fn[0])

import zipfile

zip_ref = zipfile.ZipFile(filename, 'r')
zip_ref.extractall("./" + fn[0])
zip_ref.close()

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


