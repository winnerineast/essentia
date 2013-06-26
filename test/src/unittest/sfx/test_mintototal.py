#!/usr/bin/env python

# Copyright (C) 2006-2013  Music Technology Group - Universitat Pompeu Fabra
#
# This file is part of Essentia
#
# Essentia is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation (FSF), either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the Affero GNU General Public License     
# version 3 along with this program. If not, see http://www.gnu.org/licenses/



from essentia_test import *

class TestMinToTotal(TestCase):

    def testEmpty(self):
        self.assertComputeFails(MinToTotal(), [])

    def testFlat(self):
        self.assertAlmostEquals(MinToTotal()([1]*100), 0)

    def testSingle(self):
        self.assertAlmostEquals(MinToTotal()([1]), 0)

    def testSimple(self):
        self.assertAlmostEquals(MinToTotal()([1,4,0.23,10.34]), 2/4.)


suite = allTests(TestMinToTotal)

if __name__ == '__main__':
    TextTestRunner(verbosity=2).run(suite)
