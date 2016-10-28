
import sys
from reconstruct import reconstruct

def main():
	args=sys.argv
	inputfile=args[1]
	print("inputfile:",inputfile)
	reconstruct(inputfile)

if __name__=="__main__":
	main()

#python main.py example_easy_data_set.txt