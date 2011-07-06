from unittest import TestSuite

import test_points, test_polys

def test_suite():
    suite = TestSuite()
    suite.addTest(test_points.test_suite())
    #suite.addTest(test_polys.test_suite())
    return suite
    
    
if __name__ == '__main__':
    from unittest import TestResult
    
    res = TestResult()
    
    suite = test_suite()
    suite.run(res)
