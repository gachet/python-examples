import unittest
from app.shape import Shape
 
class TddInPythonExample(unittest.TestCase):
 
    def test_shape_area_method_returns_correct_result(self):
        s = Shape(5, 4)
        area = s.area()
        self.assertEqual(20, area)

    def test_shape_perimeter_method_returns_correct_result(self):
        s = Shape(5, 4)
        p = s.perimeter()
        self.assertEqual(18, p)
        
    def test_shape_describe_method_returns_correct_result(self):
        s = Shape(5, 4)
        desc = s.describe("My description")
        self.assertEqual("My description", s.description)

    def test_shape_authorName_method_returns_correct_result(self):
        s = Shape(5, 4)
        s.authorName("My name")
        self.assertEqual("My name", s.author)
        
    def test_shape_scaleSize_method_returns_correct_result(self):
        s = Shape(5, 4)
        s.scaleSize(2)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 8)        

        
if __name__ == '__main__':
    unittest.main()
