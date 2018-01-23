# TODOER
# By: Amrit Hariharan
# Python comment parser and todo list generator

# TODO:
# - get it to work with block comments
#	- use regex maybe?
# - markdown output
# - optional arg2 (output filename)
# - turn this into a VSCode extension

from sys import argv

if __name__ == "__main__":

	# Check arguments
	print(argv)
	if (len(argv) != 3):
		print("Usage: python todoer.py INPUT_FILE OUTPUT_FILE")
	
	# Open file
	output_file = open(argv[2], 'w')

	# Dictionary of all todo items
	keywords = [
		'TODO',
		'FIXME',
		'WTF'
	] # Add keywords here
	todos = dict((keywords[i], []) for i in range(len(keywords)))

	# Find out what comment syntax was used
	comment_types = {
		'cpp': '//', 	# C++
		'c': '//',		# C
		'java': '//',	# JavaScript
		'js': '//',		# JavaScript
		'py': '#',		# Python
		'sh': '#',		# Bash shell scripts
		'hs': '--',		# Haskell
		'lhs': '--'		# Haskell
	}
	filename = argv[1]
	print(filename)
	comment = comment_types[filename[filename.find('.')+1:]]
	print('comment syntax: %s this is a line comment' % comment)

	# Go through the file line by line
	line_num = 1
	with open(argv[1], 'r') as f:
		for line in f:
			pos = line.find(comment)
			if pos != -1:
				for tag in keywords:
					if tag in line[pos:-1]:
						todos[tag].append(line[pos+len(comment):-1])
			line_num += 1

	# Print out all relevant comments
	for tag in keywords:
		if todos[tag]:
			print('%s:' % tag)
			for line in todos[tag]:
				print('\t%s' % line)
