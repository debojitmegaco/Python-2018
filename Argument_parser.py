
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-r','--readfile',required=True,help='Read file Name')
parser.add_argument('-w','--writefile',required=True,help='Write file Name')
parser.add_argument('-v','--verbose',action='store_true',help='Verbose')
args=parser.parse_args()

#should be run from command line
with open(args.readfile) as srcfile:
	with open(rgs.writefile,'w') as dstfile:
		data = srcfile.read()
		dstfile.write(data)
		if args.verbose:
			print ("Verbose Flag was On")
		else:
			print ("Verbose Flag was Off")



