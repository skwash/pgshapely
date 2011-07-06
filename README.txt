======
README
======

This is a stupid proof of concept I created to register the GEOMETRY type with 
psycopg2 to return Shapely geometry objects in result sets.

I figured I'd try my hand at this since PPyGIS seemed to overcomplicate things 
a bit. There are probably a lot of issues with it still, but it passes the 
provided tests that exercise inserting various points and polygons and making 
sure the Point and Polygon objects returned match what was inserted.