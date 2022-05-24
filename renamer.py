from os import rename,getcwd,chdir,walk,system
import os.path as osp

root = input("enter dir to apply this script: ")

for paths,dirs,files in walk(root):
    for p in paths:
        print(p)
        l=p.split(osp.sep) # [., a, b]
        f_prefix = ''
        for dir in l:
            f_prefix+=dir if dir!='.' else ''
            chdir(dir)
            print(f_prefix)
            for f in files:
               rename(f, f_prefix+'_'+f)
        for i in l:
            chdir('..')
            print(getcwd())

os.system("pause")