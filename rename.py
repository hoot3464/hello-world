#The purpose of this little system is to rename a bunch of files that are identical in name but are placed in different directories. I did some concatenation trickery in excel before exporting to two text files which were referenced here.
#It's very improper to use duplicate file names in a folder but at least this is a nice little way to fix it

import os

old = []
new = []

# the r before the path turns it into a raw string, so it doesnt get confused when it finds backslashes
with open(r'C:\Users\Administrator\Desktop\old_names.txt') as f:
    for lines in f:
        old.append(lines)

with open(r'C:\Users\Administrator\Desktop\new_names.txt') as g:
    for lines in g:
        new.append(lines)

#the lists of absolute paths are ready to go now, so all we need to do now is set them up for the os.rename function
for i in range(len(old)):
    old[i] = str(old[i])[:-1] #the -1 is needed to get rid of the "\n" at the end of each line in the text files
    new[i] = str(new[i])[:-1]
    os.rename(old[i], new[i])




