import unittest
import sys
sys.path.append("../")
import os
from bs4 import *
from get_data import *
import pandas as pd


class TestFuncs(unittest.TestCase):

    def testGetHtml(self):

        # Test valid URL
        url = 'https://en.wikipedia.org/wiki/Batman_Begins'
        h = get_html(url)

        self.assertIsInstance(h, bytes)

        # Test invalid URL
        url = 'a'
        h = get_html(url)
        self.assertIsNone(h)

        # Test URL for non-existent page
        url = 'https://asdfasdfa/'
        h = get_html(url)
        self.assertIsNone(h)


    def testMakeSoup(self):

        # Test valid url
        url = 'https://en.wikipedia.org/wiki/Batman_Begins'
        h = make_soup(url)
        self.assertIsInstance(h, BeautifulSoup)

        # Test invalid URL
        url = 'a'
        h = get_html(url)
        self.assertIsNone(h)

        # Test URL for non-existent page
        url = 'https://asdfasdfa/'
        h = get_html(url)
        self.assertIsNone(h)

    def testGetPlot(self):
        # Test valid url
        url = 'https://en.wikipedia.org/wiki/Batman_Begins'
        p = get_plot(url)
        self.assertIsInstance(p, str)
        self.assertTrue(len(p) > 0)

        # Test invalid URL
        url = 'a'
        p = get_plot(url)
        self.assertIsNone(p)

        # Valid URL, without Plot header
        url = 'https://cnn.com'
        p = get_plot(url)
        self.assertIsNone(p)

    def testNormalizeHeader(self):

        h = "Director"
        h = normalize_headers(h)
        self.assertEqual(h, "Director")

        h = "Cast and Crew"
        h = normalize_headers(h)
        self.assertEqual(h, "Cast")

        h = "English Title"
        h = normalize_headers(h)
        self.assertEqual(h, "Title")


    def testGetMovieTable(self):

        # Get American movies for year
        t = get_movie_table(2015, "American")
        self.assertIsInstance(t, pd.DataFrame)
        self.assertTrue(t.shape[0] > 0)

        # Get Italian movies for year
        t = get_movie_table(2015, "Italian")
        self.assertIsInstance(t, pd.DataFrame)
        self.assertTrue(t.shape[0] > 0)

        # Non-existent page returns None
        t = get_movie_table(100, "a")
        self.assertIsNone(t)

    def testGetAllTables(self):

        # Return dataframe for valid years
        t = get_all_tables(2015, 2016)
        self.assertIsInstance(t, pd.DataFrame)
        self.assertTrue(t["Release Year"].min() == 2015)
        self.assertTrue(t["Release Year"].max() == 2016)

        t = get_all_tables(3000, 3000)
        self.assertEqual(t.shape[0], 0)



if __name__ == "__main__":
    unittest.main()
