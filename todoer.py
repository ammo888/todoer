# TODOER
# By: Amrit Hariharan, forked by Minh Nguyen
# Python comment parser and todo list generator

import os
import re
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Parse input file')
	parser.add_argument('INPUT_FILE', help="input source code")
	parser.add_argument('OUTPUT_FILE', nargs="?", default='output.md', help="output markdown file")
	args = parser.parse_args()
	INPUT_FILE = args.INPUT_FILE
	OUTPUT_FILE = args.OUTPUT_FILE

	# Dictionary of all todo items
	keywords = [
		'TODO:',
		'FIXME:',
		'WTF:'
	] # Add keywords here
	key_patterns = '|'.join(keywords)
	todos = {k : [] for k in keywords}

	# Find out what comment syntax was used
	comment_types = {
		'.cpp': '//', 	# C++
		'.c': '//',		# C
		'.java': '//',	# Java
		'.js': '//',	# JavaScript
		'.py': '#',		# Python
		'.sh': '#',		# Bash shell scripts
		'.hs': '--',	# Haskell
		'.lhs': '--'	# Haskell
	}

	name, ext = os.path.splitext(INPUT_FILE)
	comment_type = comment_types[ext]
	print('comment syntax: %s this is a line comment' % comment_type)

	# Go through the file line by line
	pattern = re.compile(r'%s.*(%s)(.*)' % (comment_type, key_patterns))
	with open(INPUT_FILE, 'r') as f:
		for line_num, line in enumerate(f,1):
			match = re.search(pattern, line)
			if match:
				tag = match.group(1)
				comment = match.group(2)
				todos[tag].append((line_num, comment))

	# Print out all relevant comments
	with open(OUTPUT_FILE, 'w') as f:
		f.write('# Todo list for `%s`\n-----\n' % INPUT_FILE)
		for tag in keywords:
			if todos[tag]:
				f.write('## %s\n' % tag)
				for line in todos[tag]:
					f.write('- [ ] line %d: %s\n' % (line[0], line[1]))
				f.write('-----\n')

	print('todo list for %s saved in %s' % (INPUT_FILE, OUTPUT_FILE))