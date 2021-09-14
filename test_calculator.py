import unittest
import calculator

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(0,-1),-1)
        self.assertEqual(calculator.add(10,5),15)
        self.assertEqual(calculator.add(-1,-1),-2)
        self.assertEqual(calculator.add(-5,2.5),-2.5)
    def test_sub(self):
        self.assertEqual(calculator.sub(10,5),5)
        self.assertEqual(calculator.sub(-10.9,2),-12.9)
        self.assertEqual(calculator.sub(0,1),-1)
        self.assertEqual(calculator.sub(-4,-10),6)
    def test_mul(self):
        self.assertEqual(calculator.mul(0,100),0)
        self.assertEqual(calculator.mul(-2,100),-200)
        self.assertEqual(calculator.mul(200,300),60000)
        self.assertEqual(calculator.mul(-9,-2),18)
    def test_div(self):
        self.assertEqual(calculator.div(0,2),0)
        self.assertEqual(calculator.div(-2,100),-0.02)
        self.assertEqual(calculator.div(2,10),0.2)
        self.assertEqual(calculator.div(2.5,4.6),0.5434782608695653)
        self.assertEqual(calculator.div(2,-30),-0.06666666666666667)
        self.assertEqual(calculator.div(-3,-20),0.15)
        
        self.assertRaises(ValueError,calculator.div,10,0)
        self.assertRaises(ValueError,calculator.div,0,0)

        1

if __name__=='__main__':
    unittest.main()

#pytest test.py --html=report.html