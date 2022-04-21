# test_case_extended
# ------------------
# Provides TestCaseExtended, a subclass of unittest.TestCase.
# This subclass has additional methods to make testing easier.

from unittest import TestCase, main
from pathlib import Path
from bs4 import BeautifulSoup as BS

SAMPLE_DOC_PATH = Path("tests/samples")

class TestCaseExtended(TestCase):
    "A subclass of TestCase with additional assert methods."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self, "samples"):
            self.sample_docs = []
            for sample_path in self.samples:
                self.sample_docs.append(BS((SAMPLE_DOC_PATH/sample_path).read_text(), 'lxml'))

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
