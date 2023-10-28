import unittest
from unittest.mock import patch
from Project_1 import get_wikipedia_url, fetch_wikipedia_data

class TestProject1(unittest.TestCase):
    def test_get_wikipedia_url(self):
        article_name = "Ball State University"
        expected_url = (
            "https://en.wikipedia.org/w/api.php?action=query&format=json&"
            "prop=revisions&titles=Ball%20State%20University&rvprop=timestamp|user&"
            "rvlimit=30&redirects"
        )
        url = get_wikipedia_url(article_name)
        self.assertEqual(url, expected_url, "URL should match the expected one.")

if __name__ == "__main__":
    unittest.main()
