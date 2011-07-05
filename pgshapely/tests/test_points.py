import unittest
import pgshapely

class TestPoints(unittest.TestCase):

    database = "test"
    user = "test"
    password = "test"

    def setUp(self):
        
        conn = pgshapely.connect(database=self.database, user=self.user, password=self.password)
        cursor = conn.cursor()
        
        sql = "CREATE TABLE test(geometry GEOMETRY);"
        cursor.execute(sql)
        
        self.conn = conn
    
    def test_points(self):
        
        params = {
            'x'    : -122.2482834, 
            'y'    : 47.4377447,
            'ewkb' : '01010000A0E6100000F1C80EE0E38F5EC0A93FB10408B847400000000000000000',
            'wkt'  : 'POINT(-122.2482834 47.4377447)',
            'ewkt' : 'SRID=4326;POINT(-122.2482834 47.4377447)'
        }
        
        cursor = self.conn.cursor()
        
        sql = "INSERT INTO test VALUES(ST_MakePoint(%(x)s, %(y)s));"
        cursor.execute(sql, params)

        sql = "INSERT INTO test VALUES(GeomFromText(%(wkt)s));"
        cursor.execute(sql, params)

        sql = "INSERT INTO test VALUES(GeomFromEWKT(%(ewkt)s));"
        cursor.execute(sql, params)

        sql = "SELECT geometry FROM test"
        cursor.execute(sql)
        
        for row in cursor.fetchall():
            #print row[0]
            point = row[0]
            print point

            self.assertEquals(point.x,params['x'])
            self.assertEquals(point.y,params['y'])
            #self.assertEquals(point.wkt, params['wkt'])

        sql = "DELETE FROM test;"
        cursor.execute(sql)

        sql = "DROP TABLE test;"
        cursor.execute(sql)

        cursor.close()
        
def test_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPoints)

if __name__ == '__main__':
    unittest.main()