#     __                            __                                                               __   __                       
#    / /_     ___     ____ _   ____/ /  ___     _____   ____ _   ___     ____              ____ _   / /  / /        ____     __  __
#   / __ \   / _ \   / __ `/  / __  /  / _ \   / ___/  / __ `/  / _ \   / __ \            / __ `/  / /  / /        / __ \   / / / /
#  / / / /  /  __/  / /_/ /  / /_/ /  /  __/  / /     / /_/ /  /  __/  / / / /           / /_/ /  / /  / /   _    / /_/ /  / /_/ / 
# /_/ /_/   \___/   \__,_/   \__,_/   \___/  /_/      \__, /   \___/  /_/ /_/  ______    \__,_/  /_/  /_/   (_)  / .___/   \__, /  
#                                                    /____/                   /_____/                           /_/       /____/   
# 
# -*- coding: utf-8 -*-

import sys, os, argparse, glob

# paths
HEADERGEN_PY = "~/python/headergen.py"

# kill ""-signes if they occur at the beginning and at the end of the argument
def evalArg( arg ):
	result = ''

	# check empty
	if arg == '':
		return ''

	# check if ""-signs exist
	l = len( arg )
	if arg[ 0 ] == '"' and arg[ l - 1 ] == '"':
		result = arg[ 1 : l - 2 ]
	else:
		result = arg

	return result

# main
if __name__ == '__main__':

	# create command line interface
	parser = argparse.ArgumentParser( description = '' )

	parser.add_argument( 'fileEnding', metavar = 'FILE-ENDING', help = 'the file ending of the files to be affected' )
	parser.add_argument( '-b', '--lineBegin', metavar = '', help = 'a string that is put at the beginning of each line of the generated text' )
	parser.add_argument( '-e', '--lineEnd', metavar = '', help = 'a string that is put at the end of each line of the generated text' )
	parser.add_argument( '--generate-method', metavar = '', help = 'a custom method of generating the text' )

	args = parser.parse_args()

	# variables needed
	fileEnding = ''
	lineBegin = ''
	lineEnd = ''
	generateMethod = ''

	# evaluate arguments
	if args.fileEnding is not None:
		fileEnding = evalArg( args.fileEnding )
	if args.lineBegin is not None:
		lineBegin = evalArg( args.lineBegin )
	if args.lineEnd is not None:
		lineEnd = evalArg( args.lineEnd )
	if args.generate_method is not None:
		generateMethod = evalArg( args.generate_method )

	# get all filenames with the given ending in the current working directory
	files = glob.glob( os.getcwd() + '/*.' + fileEnding )
	for filename in files:
		filename = os.path.basename( filename )		# filter only the filename

		# modify the filename for the generated text a little bit
		filenameText = ''
		for i in range( len( filename )):
			filenameText = filenameText + filename[ i ] + ' '

		# add generated header to each file
		os.popen( 'python ' + HEADERGEN_PY + ' -t "' + filenameText + '" -b "' + lineBegin + '" -e "' + lineEnd + '" --generate-method="' + generateMethod + '" ' + filename )



