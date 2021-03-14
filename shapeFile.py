import os
import shutil,random
from osgeo import osr, ogr
f = open("d:/gis/VECTOR/vec_bldgs_HPG.txt","r")
print("asdas")
# if os.path.exists("d:/gis/Shape_file"):
#     # shutil.rmtree("d:/gis/Shape_file")
# else:
#     os.mkdir("d:/gis/Shape_file")
driver = ogr.GetDriverByName("ESRI Shapefile")
path = os.path.join("d:/gis/Shape_file","hpg.shp")
datasource = driver.CreateDataSource(path)
spatialReference = osr.SpatialReference()
spatialReference.ImportFromEPSG(4326)
spatialReference.SetWellKnownGeogCS('WGS84')

layer = datasource.CreateLayer("layer", spatialReference)

field = ogr.FieldDefn("ID", ogr.OFTInteger)
field.SetWidth(4)
field.SetPrecision(3)
layer.CreateField(field)

field = ogr.FieldDefn("NAME",ogr.OFTString)
field.SetWidth(20)
field.SetPrecision(3)
layer.CreateField(field)

count=0
lf = list(f)
dataPolygon = ""
ring = None
featute = None

for item in lf:
    if "buildings" in item:
        if featute == None and ring == None:
            featute = ogr.Feature(layer.GetLayerDefn())
            ring = ogr.Geometry(ogr.wkbLinearRing)
        else:
            featute.SetGeometry(ring)
            featute.SetField("ID",count)
            featute.SetField("NAME","buildings-{}".format(count))
            layer.CreateFeature(featute)
            featute = ogr.Feature(layer.GetLayerDefn())
            ring = ogr.Geometry(ogr.wkbLinearRing)
        count+=1
    else:
        tmplocations = item.split(" ")
        lat = tmplocations[0]
        long = tmplocations[1].split("\n")[0]
        print("lat = {} - long = {}".format(lat,long))
        ring.AddPoint(float(lat), float(long))
datasource = None
print("Finish")   

# shapefile = ogr.Open("d:/gis/Shape_file/hcm.shp")
# layerx = shapefile.GetLayer(0)
# for i in range(layerx.GetFeatureCount()):
#   feature  = layer.GetFeature(i)
#   id       = feature.GetField("ID")
#   name     = feature.GetField("NAME")
#   geometry = feature.GetGeometryRef()
#   print(i, name, geometry.GetX(), geometry.GetY())