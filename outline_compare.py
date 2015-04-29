# Copyright (c) 2015, Keith Kikta
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this
#    list of conditions and the following disclaimer in the documentation and/or
#    other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors may
#    be used to endorse or promote products derived from this software without
#    specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import sys
from lxml import etree

class Member(object):
   def __init__(self, dimension, name):
      self.dimension = dimension
      self.name = name

   def __str__(self):
      return self.dimension + '|' + self.name

def readOutline(xml):
   f = open(xml)
   member = []
   doc = etree.parse(f)
   f.close()
   for d in doc.xpath('//Dimension'):
      dimname = d.xpath('./@name')[0]
      for item in d.xpath('.//Member'):
         member.append(Member(dimname, item.xpath('./@name')[0]))
   return sorted(set(member), key=lambda k: (k.dimension, k.name))

def printOutline(members, prefix = ""):
   for member in members:
      print prefix + " " + member.dimension + "|" + member.name

def compareOutlines(xml1, xml2):
   a = []
   b = []
   for item in xml1:
      if not contains(xml2, lambda x: (x.dimension.lower() == item.dimension.lower() and x.name.                            lower() == item.name.lower())):
         a.append(item)
   for item in xml2:
      if not contains(xml1, lambda x: (x.dimension.lower() == item.dimension.lower() and x.name.                            lower() == item.name.lower())):
         b.append(item)
   printOutline(a, "> ")
   printOutline(b, "< ")

def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False

def main(argv):
   file1 = readOutline(sys.argv[1])
   if len(argv) >= 3:
      file2 = readOutline(sys.argv[2])
      compareOutlines(file1, file2)
   else:
      printOutline(file1)
   pass

if __name__ == "__main__":
   main(sys.argv)
