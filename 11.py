import os
base=os.path.basename('/root/dir/sub/file.txt')
a = base.split(".")

x = slice(len(a)-3, len(a))
print(a[x])