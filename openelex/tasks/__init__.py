from invoke import Collection

from fetch import fetch
import archive, cache, datasource, load

# Build tasks namespace
ns = Collection()
ns.add_task(fetch)
ns.add_collection(archive)
ns.add_collection(cache)
ns.add_collection(datasource)
ns.add_collection(load)
