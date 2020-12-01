from . import timecard

# even though main() is immediately called afterwards,
# it's still defined as a function so that setup.py can make a launcher script for it
def main():
	import sys
	lines = sys.argv[1:] or sys.stdin
	timecard(lines)

main()
