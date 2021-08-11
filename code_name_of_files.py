#--------------------------------#
#                                #
#  Version 0.0.2                 #
#  Aleksiej Ostrowski, 2017      #
#  aleksiej.ostrowski@gmail.com  #
#                                #
#--------------------------------#

import os
import shutil
import datetime
import hashlib
import time
import random

random.seed(time.time())

def code_all_files(home):
    files = [file for file in os.listdir(home) if os.path.isfile(os.path.join(home, file))]

    with open('logs_code_files_%s_%s.txt' % (str(datetime.datetime.now())[:10].replace("-",""), random.randint(100000, 900000)), 'a+') as logs:
    
        for x in files:
            x = x.encode()
            new_file_name = '%s.mp3' % hashlib.md5(x).hexdigest()[:8] 
            try:
                logs.write('%s==>%s\n' % (x, new_file_name))
                os.rename(x, new_file_name)
            except:
                logs.write("ERROR %s==>%s\n" % (x, new_file_name)) 

if __name__ == "__main__":
    code_all_files('.')
