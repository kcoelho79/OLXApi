import unittest
from olxapi import OlxApi

class TestOlxApi(unittest.TestCase):

    def test_get_list_product(self):
        # Create an instance of OlxApi
        olx = OlxApi(page_limit=1)

        # Call the get_list_product method
        # For the purpose of this test, you might want to use a mock URL or product to avoid actual web scraping
        product = 'iphone'
        olx.get_list_product(product)

        # Check if list_ads is populated
        self.assertGreater(len(olx.list_ads), 0, "list_ads should not be empty")

if __name__ == '__main__':
    unittest.main()
