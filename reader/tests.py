# This file contains tests for the reader. 
# Keep adding tests as we write more and more functions.
# you can run these with `python tests.py`.

from unittest import TestCase, main
from reader import parse_reference

class TestCaseWithDictComparison(TestCase):
    "A subclass of TestCase which knows how to compare expected and observed dicts."

    def assertDictsAreEqual(self, expected, observed):
        """Compares two dicts. 
        Checks that both are dicts, that they have the same keys, 
        and that the value for each key is the same.
        """
        self.assertIsInstance(expected, dict)
        self.assertIsInstance(observed, dict)
        self.assertEqual(set(expected.keys()), set(observed.keys()))
        for expected_key, expected_value in expected.items():
            self.assertTrue(expected_key in observed)
            self.assertEqual(expected_value, observed[expected_key])


class TestParseReference(TestCaseWithDictComparison):
    sample_references = {
        "061423ai": {
            "year": 2014,
            "month": "June",
            "question": 23,
            "course": "Algebra I"
        },
        "012032ai": {
            "year": 2020,
            "month": "January",
            "question": 32,
            "course": "Algebra I"
        }
    }
    def test_parses_reference_correctly(self):
        for ref, expected in self.sample_references.items():
            observed = parse_reference(ref)
            self.assertDictsAreEqual(expected, observed)

if __name__ == '__main__':
    main()
