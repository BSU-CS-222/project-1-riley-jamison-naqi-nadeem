import unittest
import Project_1


def test_get_recent_changes_url(self):
        article_name = "Ball_State_University"
        expected_url = (
            "https://en.wikipedia.org/w/api.php?action=query&format=json&"
            "prop=revisions&titles=Ball State University&rvprop=timestamp|user&"
            "rvlimit=30&redirects"
        )
        result_url = Project_1.get_recent_changes_url(article_name)
        self.assertEqual(result_url, expected_url, "The URL should match the expected one.")

if __name__ == "__main__":
    unittest.main()
