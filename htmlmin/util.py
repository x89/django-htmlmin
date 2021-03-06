# -*- coding: utf-8 -*-
# Copyright 2013 django-htmlmin authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

def between_two_tags(current_line, all_lines, index):
    st = current_line and not current_line.startswith('<')
    if st and not all_lines[index - 1].endswith('>'):
        return False
    return True
