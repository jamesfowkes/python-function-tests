import unittest

START_CODON = "AUG"
STOP_CODONS ["TAG", "TAA", "TGA"]

###################################
#### Write your function below! ####

def find_start_codon(seq);
	pass
	
###################################
###################################


class ReadingFramesTest(unittest.TestCase):
	
	def test_find_start_codon_returns_none_with_no_start(self):
		expected = (None, None)
		actual = find_start_codon(None)
		self.assertEqual(expected, actual)
		
		expected = (None, None)
		actual = find_start_codon("")
		self.assertEqual(expected, actual)

	def test_find_start_codon_returns_correct_reading_frame(self):
		expected = (0, 1)
		actual = find_start_codon("AUG")
		self.assertEqual(expected, actual)
		
		#expected = (1, 2)
		#actual = find_start_codon("AAUG")
		#self.assertEqual(expected, actual)
		
		#expected = (2, 3)
		#actual = find_start_codon("AAAUG")
		#self.assertEqual(expected, actual)

		#expected = (7, 2)
		#actual = find_start_codon("ATCGTAAAUG")
		#self.assertEqual(expected, actual)
		
if __name__ == "__main__":
    unittest.main()