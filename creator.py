import os,string,traceback

preffered_folder = input('where would you like to add new folders? \nby default it will store in demo folder at your current working directory: ')

cd = lambda x: os.chdir(x)
mkdir = lambda x: os.mkdir(f"{x}")
cur = os.getcwd
out = lambda f: print(f())
pause = lambda: os.system("pause")
go_up = lambda: cd('..')
test_folder_name = 'demo'

def input_pref_dir() ->str:
    return preffered_folder if preffered_folder != "" else test_folder_name
    

def creator(lst,childs):
    for i in lst:
        mkdir(i)
        cd(i)
        out(cur)
        for child in childs:
            mkdir(child)
        
        go_up()

if __name__=="__main__":
    try:
        out(cur)
        l = input("\nbase dirs names: ").split()
        print(l)
        childs = input('\n child dirs: ').split()
        print(childs)
        mkdir(input_pref_dir())
        cd(input_pref_dir())
        out(cur)
        creator(l,childs)
        pause()
    except:
        print("something went wrong ...")
        traceback.print_exc()
        pause()
        pass