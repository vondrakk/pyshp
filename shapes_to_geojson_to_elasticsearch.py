import shapefile
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch()

# read the shapefile
reader = shapefile.Reader("gadm28")
reader.iterJsonES('data', 'geo')
actions = reader.toJsonES('data', 'geo', 1000)
while actions.count:
    try:
        helpers.parallel_bulk(es, actions)
        actions = reader.toJsonES('data', 'geo', 1000)
    except:
        pass
    
