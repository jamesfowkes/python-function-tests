import unittest
import random

def multiply_by_2(value):
    return value * 2

def make_string_uppercase(string):
    return string.upper()

def quadratic(a, b, c, x):
    return (x ** 2) * a + (b*x) + c

def get_largest(a, b, c):
    numbers = [a, b, c]
    numbers = sorted(numbers) #sorted takes a list and sorts by obvious arrangement eg. numbers smallest to largest, letters alphabetically, unbroken words by letters alphabetically, list of words by words (separated by commas) alphabetically
    return numbers[-1]

def count_letters_in_string(find, string):
    number_of_find = 0
    for letter in string:
        if letter == find:
            number_of_find = number_of_find + 1
    return number_of_find
    
def factorial(value):
    factorial_value = value
    factorial_count = value
    while factorial_count > 1:
        factorial_count = factorial_count - 1
        factorial_value = factorial_value * factorial_count
    return factorial_value

def get_random_rgb_colour():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	return [r, g, b]
class FunctionTests(unittest.TestCase):

    def test_get_random_rgb_colour(self):
        rgb = get_random_rgb_colour()
        self.assertEqual(3, len(rgb))
        self.assertTrue(rgb[0]>=0)
        self.assertTrue(rgb[0]<=255)
        self.assertTrue(rgb[1]>=0)
        self.assertTrue(rgb[1]<=255)
        self.assertTrue(rgb[2]>=0)
        self.assertTrue(rgb[2]<=255)
        
    def test_factorial(self):
        expected = 1
        actual = factorial(1)
        self.assertEqual(expected, actual)

        expected = 2
        actual = factorial(2)
        self.assertEqual(expected, actual)

        expected = 24
        actual = factorial(4)
        self.assertEqual(expected, actual)
        
    def test_count_letters_in_string(self):
        expected = 4
        actual = count_letters_in_string('a', 'frgdeaacdadefa')
        self.assertEqual(expected, actual)
    
        expected = 2
        actual = count_letters_in_string('f', 'frgdeaacdadefa')
        self.assertEqual(expected, actual)
    
    def test_multiply_by_2_function(self):
        expected = 6
        actual = multiply_by_2(3)
        self.assertEqual(expected, actual)

    def test_make_string_uppercase(self):
        expected = "ABC"
        actual = make_string_uppercase("abc")
        self.assertEqual(expected, actual)
        
    def test_quadratic_function(self):
        expected = 45
        actual = quadratic(2, 3, 1, 4)
        self.assertEqual(expected, actual)
    
    def test_return_largest(self):
        expected = 77
        actual = get_largest(77, 16, 32)
        self.assertEqual(expected, actual)
    

if __name__ == "__main__":
    unittest.main()
