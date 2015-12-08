import unittest

###################################
#### Write your function below! ####

def get_dictionary_count(input):
    if input == "":
        return {}
    else:
        summat = input.lower()
        keys = summat.split()
        count = len(keys)
        
        dictionary = {}

        for i in keys:
            if not i in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] = dictionary[i] + 1
        
    return dictionary

###################################
###################################


class FunctionTest(unittest.TestCase):

    def test_get_dictionary_count_is_case_sensitive_with_option(self):
        expected = {"word" : 1, "Word" : 1}
        actual = get_dictionary_count("word Word", ignore_case=False)
        
        self.assertEqual(expected, actual)

    def test_get_dictionary_count_is_not_case_sensitive(self):
        expected = {"word" : 2}
        actual = get_dictionary_count("word Word")
        
        self.assertEqual(expected, actual)
        
    def test_get_dictionary_count_returns_dictionary_of_many_repeated_words(self):
        expected = {'word1': 2, 'word2':2}
        actual = get_dictionary_count("word1 word2 word1 word2")
        
        self.assertEqual(expected, actual)
        
    def test_get_dictionary_count_returns_dictionary_of_many_single_words(self):
        expected = {'word1': 1, 'word2':1}
        actual = get_dictionary_count("word1 word2")
        
        self.assertEqual(expected, actual) 
        
    def test_get_dictionary_count_counts_same_word_twice(self):
        expected = {'word':4}
        actual = get_dictionary_count("word word word word")

        self.assertEqual(expected, actual)

    def test_get_dictionary_count_returns_empty_dictionary_for_empty_string_input(self):
        expected = {}
        actual = get_dictionary_count("")

        self.assertEqual(expected, actual)
    
    def test_get_dictionary_count_returns_dictionary_with_single_word_as_key(self):
        expected = {'word':1}
        actual = get_dictionary_count("word")

        self.assertEqual(expected, actual)

        expected = {'anotherword':1}
        actual = get_dictionary_count("anotherword")

        self.assertEqual(expected, actual)
        
    #def test_produce_dictionary_of_words_in_a_string(self):
    #    expected = {
    #        'sentences': 3,
    #        'have' : 2,
    #        'words': 1,
    #        'full' : 2,
    #        'stops' : 2,
    #        'end' : 1
    #        }

    #    actual = get_dictionary_count("Sentences have words. Sentences have full stops. Full stops end sentences.")

    #    self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()