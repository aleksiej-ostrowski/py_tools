# -*- coding: utf-8 -*-

import re

test_str = ur'__" 011*12  (*2345*) 34 112, "*12, "qwe"*2 (23)  "*1'
print test_str
subst = u"%%"

# --- 1
p = re.compile(ur'(?<="\*)[0-9]{1,}', re.MULTILINE | re.IGNORECASE)
result = re.sub(p, subst, test_str) # replace 12 and 2 after "* to %%_
print result
# ---

# --- 2
p = re.compile(ur'(?<=\()[^\[.]+?(?=\))', re.MULTILINE | re.IGNORECASE)
result = re.sub(p, subst, test_str) # replace *2345* and 23 in brackets to %%
print result
# ---

# --- 3
p = re.compile(ur'".*?"\*[0-9]{1,}', re.MULTILINE | re.IGNORECASE)
result = re.sub(p, subst, test_str) # replace "..."*n to %%
print result

for match in re.finditer(p, test_str):
    print match.group()
