import unittest
from models.Serve import RandomServe, EvenServe, OddServe

class ServeTest(unittest.TestCase):

    def test_random_serve(self):
        minValue=1;maxValue=100
        serve = RandomServe(minValue, maxValue)
        points = serve.serve()
        self.assertIn(points,[0,1])

    def test_even_serve(self):
        minValue=1;maxValue=100
        serve = EvenServe(minValue, maxValue)
        points = serve.serve()
        self.assertEqual(points, 0)

    def test_odd_serve(self):
        minValue=0;maxValue=100
        serve = OddServe(minValue, maxValue)
        points = serve.serve()
        self.assertEqual(points, 1)
