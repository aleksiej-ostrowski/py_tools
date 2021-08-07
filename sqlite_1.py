# -*- coding: utf-8 -*-

import time
import random
from random import randint as ri 
import sqlite3

conn = sqlite3.connect('example1.db')
# conn = sqlite3.connect(":memory:")
# conn.isolation_level = None

c = conn.cursor()

'''
c.execute('DROP TABLE IF EXISTS tabl1')
c.execute('CREATE TABLE tabl1 (x1 integer, x2 integer, x3 integer, x4 integer, x5 integer, x6 integer, x7 integer, x8 integer, x9 integer, x10 integer)')
random.seed(144)

a = []
for x in xrange(1000000):
    a.append([ri(10, 1000), ri(10, 1000), ri(10, 1000), ri(10, 1000), ri(10, 1000), ri(10, 1000), ri(10, 1000), ri(10, 1000), ri(10, 1000), ri(10, 1000)])

c.executemany('INSERT INTO tabl1 VALUES (?,?,?,?,?,?,?,?,?,?)', a)
conn.commit()
'''

start_ = time.time()

c.execute("select count(*) from tabl1 where (x1 > 550) and ( (x2 + x3) < 100)")

end_ = time.time()

print "==" + str(end_ - start_) + " сек. =="
print c.fetchone()[0]


conn.close()
