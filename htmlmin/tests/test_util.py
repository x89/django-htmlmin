# -*- coding: utf-8 -*-

# Copyright 2013 django-htmlmin authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import unittest
from htmlmin.util import between_two_tags


class TestUtil(unittest.TestCase):

    def test_should_be_between_two_tags(self):
        all_lines = [
            '<script type="text/javascript">',
            'alert("Hello World!");',
            '</script>',
            '<p>Hello ',
            'World!</p>'
            ]
        self.assertTrue(between_two_tags(all_lines[1], all_lines, 1))

    def test_should_not_be_between_two_tags(self):
        all_lines = [
            '<script type="text/javascript">',
            'alert("Hello World!");',
            '</script>',
            '<p>Hello ',
            'World!</p>'
            ]
        self.assertFalse(between_two_tags(all_lines[4], all_lines, 4))
