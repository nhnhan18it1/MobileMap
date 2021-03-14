import os

f = open("./total.txt","r")

def writeF(str,fname):
    # print(str)
    f2 = open("./data_rd/datax50/{}.txt".format(fname),"a")
    f2.write(str)
    f2.close()

dtf = list(f)
titleC = 0
for item in dtf:
    if "Call Index" in item and titleC == 0:
        # strs+=item
        writeF(item,"hcmUser")
        titleC+=1
    elif "Call Index" in item and titleC != 0:
        continue
    else:
        if "floors" in item:
            properties = item.split("\t")
            column1 = 27
            column2 = 28
            if properties[27]=="1" or properties[27]=="N/A":
                print("lon={}  lat={}".format(properties[28],properties[29]))
                if float(properties[28])>671327.910 and float(properties[28])<692101.740 and float(properties[29])>1180108.140 and float(properties[29])<1201648.995:
                    writeF(item,"hcmUser")
            else:
                if float(properties[27])>671327.910 and float(properties[27])<692101.740 and float(properties[28])>1180108.140 and float(properties[28])<1201648.995:
                    writeF(item,"hcmUser")
        else:
            continue
        