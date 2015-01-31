#!/usr/bin/env python
"""
Tests for Screenshooter class.
"""

import unittest
import imgurshot

class TestScreenshooter(unittest.TestCase):
    def setUp(self):
        self.imgur_app_id = '424c87cf63c1515'
        self.image_path = 'images/tuxedo-cat.jpg'

        self.client = imgurshot.Screenshooter(self.imgur_app_id)

    def test_upload(self):
        uploaded_img = self.client._upload(self.image_path)
        self.assertIsNotNone(uploaded_img)

if __name__ == '__main__':
    unittest.main()