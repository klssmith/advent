#! /usr/bin/env python

from knot import knot_hash_encrypt

key = 'amgozmfv'
rows = ['{}-{}'.format(key, i) for i in range(128)]
hashed_rows = [knot_hash_encrypt(row) for row in rows]

answer = ''

for row in hashed_rows:
    answer += '{0:0128b}'.format(int(row, 16))

print(answer.count('1'))
