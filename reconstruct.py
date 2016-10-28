

class subseq:
	def __init__(self,name,inputfile):
		self.name=name
		self.length=len(inputfile)
		self.seq=inputfile
		self.whereOtherMatchesMyTail=None
		self.sequenceThatMatchesMyTail=None
		self.whereOtherMatchesMyHead=None
		self.sequenceThatMatchesMyHead=None


inputFile='example_easy_data_set.txt'
def readInput(inputFile):
	print (inputFile)
	allLines=''
	with open(inputFile) as f:
		allLines=f.readlines()

	seqAsList=[]
	seqList=[]
	nameList=[]
	justStarted=True
	count=1
	lengthOfFile=len(allLines)
	while count < lengthOfFile
		line=allLines[count]
		if line.startswith('>'):
			nameList.append(line.strip('\n'))
			if count>1: #if not the first line and we saw this marker again, then it's a new sequence. save the previous one
				seqList.append(''.join(seqAsList))
				seqAsList=[]
		else: #regular lines
			seqAsList.append(line.strip('n'))	
		if count==lengthOfFile: #if we've reached the last line
			seqList.append(''.join(seqAsList))
		count+=1
	return (nameList,seqList)


	# with open(inputFile, "r") as f:
	# 	name=''
	# 	subseqList=[]
	# 	for line in f:
	# 		if line.startswith('>'):
	# 			name=line
	# 			subseqList=[]
	# 		subseqList.append(line)
	# 		''.joinsubseqList

