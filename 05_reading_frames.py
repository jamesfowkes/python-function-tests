import unittest

START_CODON = "AUG"
#STOP_CODONS ["TAG", "TAA", "TGA"]

###################################
#### Write your function below! ####

def find_start_codon(seq):
    """
    This function should return
    a tuple, which is a number of values
    in parentheses. This function returns
    a two-value tuple.
    The first value contains the location of
    the start codon in the sequence.
    The second value contains the reading frame
    of the start codon.
    e.g. For the sequence "AUG" the function will
    return (0, 1), which means the start codon is at location 0
    in the sequence, which is the first reading frame.
    e.g. For the sequence "CATAGAUG" the function will
    return (5, 3), which means the start codon is at location 5
    in the sequence, which is the third reading frame.
    """

    if seq == "" or seq == None:
        return (None, None)
    else:
		position = seq.find("AUG")
		ORF = (position)%3
		
		return (position, (ORF+1))
		

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
        
        expected = (1, 2)
        actual = find_start_codon("AAUG")
        self.assertEqual(expected, actual)
        
        expected = (2, 3)
        actual = find_start_codon("AAAUG")
        self.assertEqual(expected, actual)

        expected = (7, 2)
        actual = find_start_codon("ATCGTAAAUG")
        self.assertEqual(expected, actual)
        
if __name__ == "__main__":
    unittest.main()