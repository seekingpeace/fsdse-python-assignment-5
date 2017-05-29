from unittest import TestCase
from errors import no_function_found, incorrect_output, succeed


class TestCountWord(TestCase):
    def test_countWord(self):
        try:
            from count_word import countWord
            result = countWord('./files/testfile.txt', 'dummy')
            self.assertEqual(2, result)

            result1 = countWord('./files/testfile.txt', 'Lorem')
            self.assertEqual(2, result1)
            self.assertTrue(succeed("countWord"))
        except ImportError:
            self.assertFalse(no_function_found("countWord"))
        except AssertionError:
            self.assertFalse(incorrect_output())
        except:
            self.assertFalse(no_function_found("file not found"))
