import numpy as np
import math as m
import TRP_standard_clusters


def cart2sph(x, y, z):
    XsqPlusYsq = x**2 + y**2
    r = m.sqrt(XsqPlusYsq + z**2)               # r
    az = m.atan2(y,x)                           # phi
    elev = m.atan2(z,m.sqrt(XsqPlusYsq))     # theta
    return np.rad2deg(az), np.rad2deg(elev)


clstr_angl_dic = {}
clusters_keys = sorted(list(TRP_standard_clusters.clusters.keys()))#list(TRP_standard_clusters.clusters.keys())
for i in range(len(clusters_keys)):
    x = TRP_standard_clusters.clusters[clusters_keys[i]]['CG'][0]
    y = TRP_standard_clusters.clusters[clusters_keys[i]]['CG'][1]
    z = TRP_standard_clusters.clusters[clusters_keys[i]]['CG'][2]
    PhiTheta = cart2sph(x, y, z)
    clstr_angl_dic.update({clusters_keys[i]: [round(PhiTheta[0], 3), round(PhiTheta[1], 3)]})
print(clstr_angl_dic)