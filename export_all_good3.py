#--------------------------------#
#                                #
#  version 0.0.1                 #
#                                #
#  Aleksiej Ostrowski, 2021      #
#                                #
#  https://aleksiej.com          #
#                                #
#--------------------------------#  

import argparse

parser = argparse.ArgumentParser(description='export csv to excel')
parser.add_argument('-i', help='input file', required=True)

args = vars(parser.parse_args())

inp = args['i']
out = inp + ".xls" 

# https://stackoverflow.com/questions/12976378/openpyxl-convert-csv-to-excel/13016530

import csv
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

with open(inp) as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        ws.append(row)

wb.save(out)
