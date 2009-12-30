import rpy
import unittest


class TestFlowControl(unittest.TestCase):
    def test_if1( self ):
        def main_if(x, y):
            if x < y:
                return x
            return y
        self.assertEqual( 1234, rpy.run( main_if, 1234, 4567 ) )

    def test_if2( self ):
        def main_if(x, y):
            if x < y:
                z = 2 * x
            else:
                z = 2 * y
            return z
        self.assertEqual( 20, rpy.run( main_if, 10, 30 ) )
        self.assertEqual( 20, rpy.run( main_if, 30, 10 ) )


if __name__ == '__main__':
    unittest.main()
