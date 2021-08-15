# -*- coding: utf-8 -*-

#----------------------------#
#                            #
#  Version 0.0.1             #
#  Ostrovsky Alexey, 2016    #
#  0x0all@gmail.com          #
#                            #
#----------------------------#

filename     = "ideal.pptx"
out_filename = "ideal_new.pptx"

import os

def zipdir(path, ziph, m = ""):
    for root, dirs, files in os.walk(path):
        for file in files:
            r = os.path.join(root, file)
            r2 = r.replace(m, "") 
            ziph.write(r, r2)

fn_ = filename.split('.')

import zipfile

d = "./%s/ppt/embeddings/" % fn_[0]
d2 = d + "*" # .xlsx"

import glob

files = glob.glob(d2)

import shutil

for fn in files:
    
    # print fn

    b = fn.split('/')[-1]
    a = b + '.xlsx'

    # print a

    zipf = zipfile.ZipFile(d + a, 'w', zipfile.ZIP_DEFLATED)
    zipdir(fn + '/', zipf, d + b)
    zipf.close()

    shutil.rmtree(fn)

fn = filename.split('.')

zipf = zipfile.ZipFile(out_filename, 'w', zipfile.ZIP_DEFLATED)

d3 = fn[0] + '/'
zipdir(d3, zipf, d3)
zipf.close()

