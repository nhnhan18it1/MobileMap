import numpy as np
import shapefile as shp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from osgeo import osr, ogr
sns.set(style="whitegrid", palette="pastel", color_codes=True)
sns.mpl.rc("figure", figsize=(10,6))
sf = shp.Reader("d:/gis/Shape_file/hcm.shp")
def read_shapefile(sf):
    """
    Read a shapefile into a Pandas dataframe with a 'coords' 
    column holding the geometry information. This uses the pyshp
    package
    """
    fields = [x[0] for x in sf.fields][1:]
    records = sf.records()
    shps = [s.points for s in sf.shapes()]
    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)
    return df

def plot_shape(id, s=None):
    """ PLOTS A SINGLE SHAPE """
    plt.figure()
    ax = plt.axes()
    ax.set_aspect('equal')
    shape_ex = sf.shape(id)
    x_lon = np.zeros((len(shape_ex.points),1))
    y_lat = np.zeros((len(shape_ex.points),1))
    for ip in range(len(shape_ex.points)):
        x_lon[ip] = shape_ex.points[ip][0]
        y_lat[ip] = shape_ex.points[ip][1]
    plt.plot(x_lon,y_lat) 
    x0 = np.mean(x_lon)
    y0 = np.mean(y_lat)
    plt.text(x0, y0, s, fontsize=10)
    plt.show()
    # use bbox (bounding box) to set plot limits
    # plt.xlim(shape_ex.bbox[0],shape_ex.bbox[2])
    return x0, y0

def plot_shape2():
    shapefile = ogr.Open("d:/gis/Shape_file/hcm.shp")
    layerx = shapefile.GetLayer(0)
    data = []
    for i in range(layerx.GetFeatureCount()):
        feature  = layerx.GetFeature(i)
        id       = feature.GetField("ID")
        name     = feature.GetField("NAME")
        geometry = feature.GetGeometryRef()
        print(i, name, geometry.GetX(), geometry.GetY())
        data.append([geometry.GetX(), geometry.GetY()])
    xs,ys = zip(*data)
    # print(data)
    plt.plot(xs,ys)
    plt.show()

df = read_shapefile(sf)
print(df.shape)
# plot_shape(1, "comuna")
plot_shape2()