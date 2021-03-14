import os

class attrData:
    """docstring for attrData."""
    def __init__(self, index, start_long, start_lat, end_long, end_lat, count_user):
        self._index = index
        self._start_long = start_long
        self._start_lat = start_lat
        self._end_long = end_long
        self._end_lat = end_lat
        self._count_user = count_user
    @property
    def start_long(self):
        """The start_long property."""
        return self._start_long
    @start_long.setter
    def start_long(self, value):
        self._start_long = value
    @property
    def index(self):
        """The index property."""
        return self._index
    @property
    def end_long(self):
        """The end_long property."""
        return self._end_long
    @end_long.setter
    def end_long(self, value):
        self._end_long = value
    @property
    def start_lat(self):
        """The start_lat property."""
        return self._start_lat
    @start_lat.setter
    def start_lat(self, value):
        self._start_lat = value
    @property
    def end_lat(self):
        """The end_lat property."""
        return self._end_lat
    @end_lat.setter
    def end_lat(self, value):
        self._end_lat = value
    @property
    def count_user(self):
        """The coun_user property."""
        return self._count_user
    @count_user.setter
    def count_user(self, value):
        self._count_user = value

f = open("d:/gis/data_rd/datax50/hcmUser.txt", "r")
def writeF(str):
    # print(str)
    f2 = open("d:/gis/data_rd/datax50/attrHCM.txt", "a")
    f2.write(str)
    f2.close()
def writeLocation():
    dem = 1
    currentLat=671327.910
    currentLon=1180108.140
    bfLon=1180108.140
    for row in range(430):
        for col in range(1,415):
            #lat:671327.910
            #lon:1180108.140
            strs="{}\t{}\t{}\t{}\t{}\t{}\n".format(dem, currentLat, currentLon, str(currentLat+50),str(currentLon+50), "0")
            currentLon+=50
            dem+=1
            writeF(strs)
        currentLon=1180108.140
        currentLat+=50
def splitDataLocation():
    dt = list(f)
    for item in dt:
        if "Call Index" in item:
            continue
        else:
            pass


def writeTitle():
    strs = "index\tstart_long\tstart_lat\tend_long\tend_lat\tcount_user\n"
    writeF(strs)

def insertCountUser():
    fattr = open("./datax50/attrHCM.txt")
    lfattr = list(fattr)
    dt = list(f)
    for record in lfattr:
        for item in dt:
            if "Call Index" in item:
                continue
            else:
                properties = item.split("\t")
                if properties[27]=="1" or properties[27]=="N/A":
                    print("lon={}  lat={}".format(properties[28],properties[29]))
                    if float(properties[28])>671327.910 and float(properties[28])<692101.740 and float(properties[29])>1180108.140 and float(properties[29])<1201648.995:
                        writeF(item,"hcmUser")
                else:
                    if float(properties[27])>671327.910 and float(properties[27])<692101.740 and float(properties[28])>1180108.140 and float(properties[28])<1201648.995:
                        writeF(item,"hcmUser")

def createClassData():
    f2 = open("d:/gis/data_rd/datax50/attrHCM.txt", "r")
    lf2 = list(f2)
    data = []
    for item in lf2:
        if "index" in item:
            continue
        else:
            list_item = item.split("\t")
            data.append(attrData(list_item[0],list_item[1],list_item[2],list_item[3],list_item[4],list_item[5]))
    return data

def updateDataUser(list_attr):
    global str
    f2 = open("d:/gis/data_rd/datax50/hcmUser.txt", "r")
    data_f2 = list(f2)
    for item in list_attr:
        count = 0
        for i in range(0,len(data_f2)):
            if "Call Index" in data_f2[i]:
                continue
            else:
                properties = data_f2[i].split("\t")
                print("------------------------")
                print("1-lon={}  lat={}".format(item.start_long,item.start_lat))
                print("2-lon={}  lat={}".format(item.end_long,item.end_lat))
                if properties[27]=="1" or properties[27]=="N/A":
                    print("lon={}  lat={}".format(properties[28],properties[29]))
                    
                    if float(properties[28]) >= item.start_long and float(properties[28]) <= item.end_long and float(properties[29]) >= item.start_lat and float(properties[29]) <= item.end_lat:
                        # writeF(item,"hcmUser")
                        count+=1
                        data_f2.pop(i)
                else:
                    print("lon={}  lat={}".format(properties[27],properties[28]))
                    if float(properties[27]) >= item.start_long and float(properties[27]) <= item.end_long and float(properties[28]) >= item.start_lat and float(properties[28]) <= item.end_lat:
                        # writeF(item,"hcmUser")
                        count+=1
                        data_f2.pop(i)
                print(count)
        item.count_user = count
        print("--------------------")
        print(count)
        # print(item.count_user)
        count=0

list_dt = createClassData()
updateDataUser(list_dt)
print(len(list_dt))

# writeTitle()
# writeLocation()
