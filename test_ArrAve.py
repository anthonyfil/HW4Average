import unittest
import ArrAve
class test_ArrAve(unittest.TestCase): 
	def test_Ave(self):
                #Testing Numbers
		result = ArrAve.Ave([1])
		self.assertEqual(result, 1)
		
		result = ArrAve.Ave([1, 2])
		self.assertEqual(result, 1.5)
		
		result = ArrAve.Ave([1,0.5,2,3,3.5])
		self.assertEqual(result, 2)
	def test_Ave_negatives(self):
                #Testing negatives
		result = ArrAve.Ave([-1,-0.5,-2,-3,-3.5])
		self.assertEqual(result, -2)
		
		result = ArrAve.Ave([-1, 1])
		self.assertEqual(result, 0)
	def test_Ave_text(self):
		#Testing text
		result = ArrAve.Ave("Words")
		self.assertEqual(result, "Error")
		
		result = ArrAve.Ave(["3", "4", "we"])
		self.assertEqual(result, "Error")
	def test_Ave_other(self):
		#testing complex numbers
		result = ArrAve.Ave(complex(5,2))
		self.assertEqual(result, "Error")
		
		result = ArrAve.Ave([complex(5,2), complex(5,2)])
		self.assertEqual(result, "Error")
		#testing emptly list
		result = ArrAve.Ave([])
		self.assertEqual(result, "Error")
		#testing an actual integer
		result = ArrAve.Ave(1)
		self.assertEqual(result, "Error")


if __name__ == "__main__":
        unittest.main()
