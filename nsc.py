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

def solveTable():
	nums = [ 20, 13, 14, 22, 17, 18, 27, 10 ]
	bases = [ 3, 2, 13, 14, 10, 7, 4, 8 ]
	spaces = [ 5, 7, 4, 4, 4, 4, 5, 4 ]

	print( '+-----+-------+----+----+----+----+-----+----+' )

	# BASES
	row = ''
	i = 0
	for base in bases:
		row += '| ' + str( base )
		l = len( str( base ))
		while l < spaces[ i ] - 1:
			row += ' '
			l += 1

		i += 1

	print( row + '|' )

	# VALUES
	i = 1
	for num in nums:
		row = ''

		j = 0
		for base in bases:
			result = convert( str( num ), 10, base )
			row += '| ' + result

			l = len( result )
			while l < spaces[ j ] - 1:
				row += ' '
				l += 1

			j += 1

		print( '+-----+-------+----+----+----+----+-----+----+' )
		print( row + '|' )

		i += 1

	print( '+-----+-------+----+----+----+----+-----+----+' )

if __name__ == '__main__':
	solveTable()

