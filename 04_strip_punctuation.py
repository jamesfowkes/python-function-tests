import unittest

###################################
#### Write your function below! ####
import string
def strip_punctuation(string_in):
    string_out = ""
    for i in string_in:
        if i not in string.punctuation:
            string_out = string_out + i
    return string_out
###################################
###################################


class FunctionTest(unittest.TestCase):

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

    def test_strip_punctuation_leaves_midword_punctation_intact(self):
        expected = "didn't"
        actual = strip_punctuation("didn't")
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()