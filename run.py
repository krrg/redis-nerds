# Script to delete all non-expiring keys.
# NERDS are Non Expiring Redis Deletion Sets


# The MIT License (MIT)
#
# Copyright (c) 2015 Ken Reese
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.



import redis
import argparse

parser = argparse.ArgumentParser(description='Deletes all keys in a Redis store that have a ttl == -1')
parser.add_argument('--host', default='localhost', required=False)
N = parser.parse_args()

R = redis.StrictRedis(host=N.host, port=6379)

for key in list(R.keys()):
    if R.ttl(key) == -1:
        print "DEL `{}` : No expiry detected.".format(key)
        R.delete(key)

print "DONE"
