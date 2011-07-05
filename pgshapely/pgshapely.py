import psycopg2
import psycopg2.extensions

from shapely import wkb
import binascii

def make_shapely_geometry(value, cursor=None):
    return wkb.loads(binascii.a2b_hex(value))
    
def connect(*a, **kw):
    c = psycopg2.connect(*a, **kw)
    #c = psycopg2.extensions.connection(*a, **kw)
    
    GEOMETRY_OID = get_oid(c)

    GEOMETRY = psycopg2.extensions.new_type((GEOMETRY_OID, ), "GEOMETRY",
        make_shapely_geometry)

    psycopg2.extensions.register_type(GEOMETRY)
    
    return c

def get_oid(conn):
    cursor = conn.cursor()
    
    sql = """
    SELECT pg_type.oid
      FROM pg_type JOIN pg_namespace
             ON typnamespace = pg_namespace.oid
     WHERE typname = 'geometry'
       AND nspname = 'public';
    """
    cursor.execute(sql)
    
    oid = cursor.fetchone()[0]
    
    cursor.close()
    
    return oid
