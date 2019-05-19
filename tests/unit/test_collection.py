"""Test for generating phish-stats"""
import os
import unittest

from phish_stats import Collection

API_KEY = os.environ['PHISHNET_API_KEY']


class TestCollection(unittest.TestCase):
    """Test class for show collection."""

    @classmethod
    def setUpClass(cls):
        """Setup function."""
        kwargs = {
            'year': 1998,
            'month': 4
        }
        cls.collection = Collection()
        cls.collection.add_shows(API_KEY, **kwargs)
        cls.collection.set_show_attributes(API_KEY)

    def test_number_of_shows(self):
        """Test accurate number of shows"""
        self.assertEqual(len(self.collection.shows), 4)

    def test_avg_rating(self):
        """Test average rating by month."""
        avg_rating = self.collection.calculate_avg_rating()
        self.assertTrue(isinstance(avg_rating, float))


class TestAllTime(unittest.TestCase):
    """Test case for all time show collection."""

    @classmethod
    def setUpClass(cls):
        """Setup function."""
        cls.collection = Collection()
        cls.collection.add_shows(API_KEY)

    # def test_shows_per_year(self):
    #     """Test calculate shows per year."""
    #     self.collection.calculate_shows_per_year()


if __name__ == '__main__':
    unittest.main()
