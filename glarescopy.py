# I want to copy glares for FIFA16. There are 3 integers in a filename in order of Stadium ID, Day/Night, Alternate condition
import os
import shutil

# First I am copying Day/Night
cond = [3, 1]

# List of extensions
exten = ["lnx", "rx3"]

# Then there are variations for alternate conditions
vari = [1,2,3]

# Asks for stadium ID then converts string to integer
id = input("Stadium ID?")

# Copy-paste function, shutil.copy copies the file and renames it. This is for day/night duplication
for i in cond:
    for j in cond:
        for k in exten:
            for l in exten:
                if i != j and k != l:
                    i = str(i)
                    j = str(j)
                    src_dir="glares_%s_%s_0.%s" % (id, i, k)
                    dst_dir="glares_%s_%s_0.%s" % (id, j, l)
                    shutil.copy(src_dir,dst_dir)
                    break
                else:
                    continue

# For alternate condition duplicate
for j in cond:
    for i in vari:
        src_dir="glares_%s_%s_0.lnx" % (id, j)
        dst_dir="glares_%s_%s_%s.lnx" % (id, j, i)
        shutil.copy(src_dir,dst_dir)

        src_dir="glares_%s_%s_0.rx3" % (id, j)
        dst_dir="glares_%s_%s_%s.rx3" % (id, j, i)
        shutil.copy(src_dir,dst_dir)
