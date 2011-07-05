import unittest
import pgshapely
import binascii

class TestPolys(unittest.TestCase):

    database = "test"
    user = "test"
    password = "test"

    def setUp(self):
        
        conn = pgshapely.connect(database=self.database, user=self.user, password=self.password)
        cursor = conn.cursor()
        
        sql = "CREATE TABLE test(geometry GEOMETRY);"
        cursor.execute(sql)
        
        self.conn = conn
        
    def tearDown(self):
        
        self.conn.close()
        self.conn=None
        
    def test_poly(self):

        params = {
            'wkt'  : 'POLYGON ((0.0000000000000000 0.0000000000000000, 4.0000000000000000 0.0000000000000000, 4.0000000000000000 4.0000000000000000, 0.0000000000000000 4.0000000000000000, 0.0000000000000000 0.0000000000000000), (1.0000000000000000 1.0000000000000000, 2.0000000000000000 1.0000000000000000, 2.0000000000000000 2.0000000000000000, 1.0000000000000000 2.0000000000000000, 1.0000000000000000 1.0000000000000000))',
            'ewkt' : 'SRID=4326;POLYGON((0 0 0,4 0 0,4 4 0,0 4 0,0 0 0),(1 1 0,2 1 0,2 2 0,1 2 0,1 1 0))',
            'wkb'  : '01030000000200000005000000000000000000000000000000000000000000000000001040000000000000000000000000000010400000000000001040000000000000000000000000000010400000000000000000000000000000000005000000000000000000f03f000000000000f03f0000000000000040000000000000f03f00000000000000400000000000000040000000000000f03f0000000000000040000000000000f03f000000000000f03f'
        }

        cursor = self.conn.cursor()

        sql = "INSERT INTO test VALUES(GeomFromText(%(wkt)s));"
        cursor.execute(sql, params)

        sql = "INSERT INTO test VALUES(GeomFromEWKT(%(ewkt)s));"
        cursor.execute(sql, params)

        sql = "INSERT INTO test VALUES(%(wkb)s);"
        cursor.execute(sql, params)

        sql = "SELECT geometry FROM test"
        cursor.execute(sql)

        for row in cursor:
            poly = row[0]
            self.assertEquals(poly.wkt, params['wkt'])
            self.assertEquals(binascii.b2a_hex(poly.wkb), params['wkb'])
        
        sql = "DELETE FROM test;"
        cursor.execute(sql)

        sql = "DROP TABLE test;"
        cursor.execute(sql)

        cursor.close()
        
        self.assertEquals(1,1)
        
        
def test_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPolys)

if __name__ == '__main__':
    unittest.main()