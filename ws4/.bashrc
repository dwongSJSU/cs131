#!/bin/bash

alias gc='git commit -m'

# produce user specified number of head lines for every file in a directory
heads() {
	local lines="$1"
	local dir="$2"

	# check correct usage
	if [[ -z "$lines" || -z "$dir" ]]; then
		echo "Usage: heads <# lines> <directory>"
		return 1
	fi

	# check if arg is actually a directory
	if [ ! -d "$dir" ]; then
		echo "Error: '$dir' is not a directory"
		return 1
	fi

	# print head lines for each file in $dir
	for f in "$dir"/*; do
		if [ -f "$f" ]; then
			echo "File: '$f'"
			head -n "$lines" "$f"
			echo ""
		fi
	done
}
