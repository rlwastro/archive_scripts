# sample script showing how to download HLA catalogs
# R. White, 2013 January 2
# Updated for Python 3, 2020 September 4

from __future__ import print_function
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

def getsourcelist(image, catalog="DAO", format="text", trimmed=True):

    """Retrieve HLA source list for an image

    catalog = "DAO" or "SEX"
    format = "text", "votable", "tsv", "csv", "html", "kml", or "json"
    trimmed = True means remove flagged sources, set to False to include all sources
    Note no checking is done on parameters.
    """

    url = "http://hla.stsci.edu/HLA/Catalogs/HLAcat.aspx?CATALOG=" + catalog + "&FORMAT=" + format + "&IMAGE=" + image
    if not trimmed:
        url = url + '&IGNOREFLAG=T'
    data = urlopen(url).read()
    return data.decode('UTF-8')

data = getsourcelist("hst_8992_52_acs_wfc_f606w")
print(data)
