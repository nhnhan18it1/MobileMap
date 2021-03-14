import os
import zipfile
import gzip
dem = 0
crow = 10000
def writeF(str,fname):
    global dem
    # print(str)
    f2 = open("./data_sample_2/{}-{}.txt".format(fname,dem),"a+")
    f2.write(str)
    dem+=1
    f2.close()

def openF(path):
    lf2 = os.listdir(path)
    for ft in lf2:
        print(ft)
        if ft.endswith(".txt"):
            print("is txt file")
            fdirtmp = '/%s'%(ft)
            fg = path + fdirtmp
            f = open(fg, 'r')
            str = ""
            for i in range(0,crow):
                str += f.readline()
            f.close
            writeF(str,ft.split(".")[0])
        if ft.endswith(".gz"):
            fdirtmp = '/%s'%(ft)
            fg = path + fdirtmp
            f = gzip.open(fg, 'r')
            str = ""
            for i in range(0,crow):
                str += f.readline()
            f.close()
            writeF(str,ft.split(".")[0])
        else :
            fdirtmp = '/%s'%(ft)
            fg = path + fdirtmp
            # print fg
            if(os.path.isdir(fg)):
                openF(fg)

fdir = "./AHan_2"
lf = os.listdir(fdir)
print lf

for ft in lf:
    print(ft)
    if ft.endswith(".txt"):
        print "txt"
        print("is txt file")
        fdirtmp = '/%s'%(ft)
        fg = fdir + fdirtmp
        f = open(fg, 'r')
        
        str = ""
        for i in range(0,crow):
            str += f.readline()
        f.close
        writeF(str,ft.split(".")[0])
    elif ft.endswith(".gz"):
        print "gz"
        fdirtmp = '/%s'%(ft)
        fg = fdir + fdirtmp
        f = gzip.open(fg, 'r')
        str = ""
        for i in range(0,crow):
            str += f.readline()
        f.close()
        writeF(str,ft.split(".")[0])
    elif ft.endswith(".csv"):
        continue
    else :
        fdirtmp = '/%s'%(ft)
        fg = fdir + fdirtmp
        # print os.path.isdir(fg)
        if os.path.isdir(fg):
            openF(fg)
            print("-----------------------------")
print("Done")



