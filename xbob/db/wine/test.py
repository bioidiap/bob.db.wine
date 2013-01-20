#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Laurent El Shafey <Laurent.El-Shafey@idiap.ch>

"""Test Units
"""

import unittest
import xbob.db.wine as wine

class WineTests(unittest.TestCase):

  def wine_data(self):
    self.assertEqual(len(wine.names), 13)
    self.assertEqual(len(wine.data()), 178)

