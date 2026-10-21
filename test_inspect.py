import unittest
from pathlib import Path
from quality_check import assess, load_pgm

class TestQuality(unittest.TestCase):
    def test_sample(self):
        result = assess(Path(__file__).with_name("sample.pgm"))
        self.assertEqual(result["flags"], [])
        self.assertGreater(result["contrast_range"], 0.9)

if __name__ == "__main__":
    unittest.main()
