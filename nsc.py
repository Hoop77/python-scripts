# -*- coding: utf-8 -*-

import math

digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def convert( num, baseOrig, baseDest ):
	result = ''

	num = toDecimal( num, baseOrig )

	q = num

	while q > 0:
		r = q % baseDest
		q = q / baseDest

		result = digits[ r ] + result

	return result


def toDecimal( num, base ):
	result = 0
	i = 0
	pos = len( num )

	while pos > 0:
		digit = num[ i ]
		i += 1

		value = digits.index( digit )

		pos -= 1
		result += value * int( math.pow( base, pos ))

	return result

if __name__ == '__main__':

	nums = [ 20, 13, 14, 22, 17, 18, 27, 10 ]
	bases = [ 3, 2, 13, 14, 10, 7, 4, 8 ]

	i = 1

	for num in nums:
		row = '(' + str(i) + ')  '

		for base in bases:
			result = convert( str( num ), 10, base )
			row += result + '  '

		print( row + '\n' )

		i += 1


