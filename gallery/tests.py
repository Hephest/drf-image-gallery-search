import os
from unittest import TestCase

from .utils import (
    api_get_images_id, api_get_images_pages_count, api_get_token,
    build_images_urls,
)

API_KEY = os.environ['API_KEY']


class GalleryUtilsTest(TestCase):

    def test_utils_api_get_token_works(self):
        """
        Ensure utils method `api_get_token` works and
        return token.
        """
        first_token = api_get_token()
        self.assertIsInstance(first_token, str)

        second_token = api_get_token()
        self.assertIsInstance(second_token, str)

        self.assertNotEqual(first_token, second_token)
        self.assertEqual(len(first_token), len(second_token))

    def test_utils_api_get_images_pages_count_works(self):
        """
        Ensure utils method `api_get_images_page_count` works
        and return valid count of pages.
        """

        pages_count = api_get_images_pages_count()
        self.assertIsInstance(pages_count, int)
        self.assertNotEqual(pages_count, 0)

    def test_utils_api_get_images_id_works(self):
        """
        Ensure utils method 'api_get_images_id' works and
        return valid list of pictures id.
        """
        images_count = api_get_images_pages_count() * 10
        images_id_list = api_get_images_id()

        self.assertIsInstance(images_id_list, list)
        self.assertEqual(len(images_id_list), images_count)

    def test_utils_build_images_urls_works(self):
        """
        Ensure utils method `build_images_urls` works and
        return valid list of urls.
        """
        images_id_list = api_get_images_id()
        images_urls_list = build_images_urls()

        self.assertIsInstance(images_urls_list, list)
        self.assertIsInstance(images_id_list, list)
        self.assertEqual(len(images_id_list), len(images_urls_list))
