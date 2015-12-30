import unittest

###################################
#### Write your function below! ####
import string
def find_index_of_first_nonpunctation_in_string(word):
    for pos, i in enumerate(word):
        if i not in string.punctuation:
            return pos

def find_index_of_last_nonpunctation_in_string(word):
    flip_word = word[::-1]
    for pos, i in enumerate(flip_word):
        if i not in string.punctuation:
            return (len(word) - pos) - 1

def strip_punctuation(string_in):
    start_pos = find_index_of_first_nonpunctation_in_string(string_in)
    end_pos = find_index_of_last_nonpunctation_in_string(string_in)
    return string_in[start_pos:end_pos+1]


###################################
###################################


class FunctionTest(unittest.TestCase):

    def test_find_index_of_first_nonpunctation_in_string(self):
        expected = None
        actual = find_index_of_first_nonpunctation_in_string(",")
        self.assertEqual(expected, actual)

        expected = 0
        actual = find_index_of_first_nonpunctation_in_string("word")
        self.assertEqual(expected, actual)

        expected = 1
        actual = find_index_of_first_nonpunctation_in_string(",word")
        self.assertEqual(expected, actual)
        
        expected = 6
        actual = find_index_of_first_nonpunctation_in_string(".!.[],didn't")
        self.assertEqual(expected, actual)

    def test_find_index_of_last_nonpunctation_in_string(self):
        expected = None
        actual = find_index_of_last_nonpunctation_in_string(",")
        self.assertEqual(expected, actual)

        expected = 3
        actual = find_index_of_last_nonpunctation_in_string("word")
        self.assertEqual(expected, actual)

        expected = 4
        actual = find_index_of_last_nonpunctation_in_string(",word")
        self.assertEqual(expected, actual)
            
        expected = 11
        actual = find_index_of_last_nonpunctation_in_string(".!.[],didn't")
        self.assertEqual(expected, actual)

    def test_strip_punctuation_leaves_midword_punctation_intact(self):
        expected = "didn't"
        actual = strip_punctuation("didn't")
        self.assertEqual(expected, actual)

    def test_strip_punctuation_leaves_standard_word_intact(self):
        expected = "word"
        actual = strip_punctuation("word")

        self.assertEqual(expected, actual)

    def test_strip_punctuation_removes_trailing_puncutation(self):
        expected = "word"
        actual = strip_punctuation("word.")

        self.assertEqual(expected, actual)

        expected = "word"
        actual = strip_punctuation("word,")

        self.assertEqual(expected, actual)


    def test_strip_punctuation_removes_leading_puncutation(self):
        expected = "word"
        actual = strip_punctuation(".word")

        self.assertEqual(expected, actual)

        expected = "word"
        actual = strip_punctuation(",word")

        self.assertEqual(expected, actual)


    def test_strip_punctuation_removes_leading_and_trailing_puncutation(self):
        expected = "word"
        actual = strip_punctuation(".word.")

        self.assertEqual(expected, actual)

        expected = "word"
        actual = strip_punctuation(",word,")

        self.assertEqual(expected, actual)

    def test_strip_punctuation_removes_mutiple_punctuation_marks(self):
        expected = "word"
        actual = strip_punctuation("..word.,")

        self.assertEqual(expected, actual)

        expected = "word"
        actual = strip_punctuation(",,,word.,")

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()