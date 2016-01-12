# OSM edits statistics (GIS1)

Usage:

        ./osm-stats.py user [T1] [T2]

where

        T1 find changesets closed after T1
        T2 find changesets created before T2

Example:

        ./osm-stats.py Ijaak 2015-10-01 2016-01-04
        Number of changesets: 7
        Number of changes: 409

# Requirements

        python-xmltodict