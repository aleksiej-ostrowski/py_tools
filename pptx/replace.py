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

fn_ = filename.split('.')

import glob2

all_files = glob2.glob("./" + fn_[0] + "/**/*.xml")

all_codes = ["7071%s" % i for i in xrange(1,4279)]

all_id = [str(i) for i in xrange(1,4279)]

dk = { key : value for (key, value) in zip(all_id, all_codes) }

# print all_files
# print all_codes

for f_ in all_files:
    lines = []
    with open(f_) as infile:
        for line in infile:
            for k1, k2 in dk.iteritems():
                line = line.replace("%s<" % k2, "%s<" % k1).replace("%s " % k2, "%s " % k1)
            lines.append(line)

    with open(f_, 'w') as outfile:
        for line in lines:
            outfile.write(line)
