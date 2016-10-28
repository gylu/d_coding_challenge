
import sys
import math

#python's "substring in string" usage seems to be implemented in https://hg.python.org/cpython/file/tip/Objects/stringlib/fastsearch.h

class subseq:
    def __init__(self,name,input_file):
        self.name=name
        self.length=len(input_file)
        self.seq=input_file
        self.seq_for_head=None
        self.index_of_other_seq_for_my_lefthead=None
        self.seq_for_tail=None
        self.index_of_other_seq_for_my_righttail=None


def read_input(input_file):
    """
    INPUT: filename.txt
    OUTPUT: name_list, seq_list 
    name_list has list of names of the sequences in the input file. seq_list has a list of the actual values
    """
    allLines=''
    with open(input_file) as f:
        allLines=f.readlines()
    seq_as_list=[]
    seq_list=[]
    name_list=[]
    count=0
    lengthOfFile=len(allLines)
    while count < lengthOfFile:
        line=allLines[count]
        if line.startswith('>'):
            name_list.append(line.strip('\n'))
            if count>1: #if not the first line and we saw this marker again, then it's a new sequence. save the previous one
                seq_list.append(''.join(seq_as_list))
                seq_as_list=[]
        else: #regular lines
            seq_as_list.append(line.strip('\n'))    
        if count+1==lengthOfFile: #if we've reached the last line
            seq_list.append(''.join(seq_as_list))
        count+=1
    return (name_list,seq_list)


def match_and_glue(seq1,seq2):
    """
    INPUT: two sequences
    OUTPUT: a glued output sequence. 
    Glue only occurs if more than half of one sequence overlaps with the other, and there are additional new characters in the glued sequence
    This function attempts to match on both sides (left or right):
        1. It takes the shorter of the two sequences, halves it and adds a character (to satisfy the "more than half"), and the sees if that half-character is in the longer string (CPython's substring in string check uses Boyer-Moore, which is one of the fastest string search algorithms)
        2. If this substring is in the longer string, see if the remainder of the substring also overlaps
        3. If it is, perform the glue
        
        Example:
        smaller_string = aabbcde
        longer_string  = aaaaabbcd
        1. more than half of aabbcdd = aabb
            a) Is this more-than-half of inside the longer string?
                Yes, as shown:
                   aabb
                aaaaabbcd
        2. Is the remainder of the substring also there
            a) remainder-of-longer-string: 
                cd (length = 2)
            b) reaminder of smaller string 
                cde
            c) reaminder of smaller string up to same length as remainder of longer-string
                cd (length=2)
        3. Perform the glue:
               aabbcde
            aaaaabbcd
            -----------
            aaaaabbcde
    """
    if len(seq1)<len(seq2):
        small_seq=seq1
        other_seq=seq2
    else:
        small_seq=seq2
        other_seq=seq1
    substr_lefthalf=small_seq[0:len(small_seq)//2+1] #get substring that's the first half of the string plus one more character
    substr_righthalf=small_seq[math.ceil(len(small_seq)/2)-1::]
    temp=False
    if substr_lefthalf in other_seq:
        len_substr=len(substr_lefthalf)
        head_index=other_seq.index(substr_lefthalf)
        remainder_other_seq=other_seq[head_index+len_substr::]
        len_remainder_other_seq=len(remainder_other_seq)
        remainder_substr=small_seq[len_substr:len_substr+len_remainder_other_seq] #this is the remainder of the string that fits with the remainder of the other sequence
        #print("remainder_other_seq0: ", remainder_other_seq)
        #print("remainder_substr0: ", remainder_substr)
        if (remainder_substr==remainder_other_seq):
            remainder_small_seq=small_seq[len_substr+len_remainder_other_seq::]
            temp=''.join([other_seq,remainder_small_seq])
    elif substr_righthalf in other_seq: #same as above, except try matching the right side of the shorter string against the left side of the long string
        len_substr=len(substr_righthalf)
        head_index=other_seq.index(substr_righthalf)
        remainder_other_seq=other_seq[0:head_index]
        len_remainder_other_seq=len(remainder_other_seq)
        remainder_substr=small_seq[-len_substr-len_remainder_other_seq:-len_substr]
        #print("remainder_other_seq1: ", remainder_other_seq)
        #print("remainder_substr1 ", remainder_substr)
        if (remainder_substr==remainder_other_seq):
            remainder_small_seq=small_seq[0:-len_substr-len_remainder_other_seq]
            temp=''.join([remainder_small_seq,other_seq])
    return temp


def main():
    args=sys.argv
    input_file=args[1]
    # input_file='coding_challenge_data_set.txt'
    # input_file='example_easy_data_set.txt'
    name_list,seq_list=read_input(input_file)

    # myDict={}
    # for seq_name, seq_value in zip(name_list,seq_list):
    #     myDict[seq_name]={'value':seq_value}
    #     myDict[seq_name]["length"]=len(seq_value)
    master=seq_list.pop()

    max_loops=len(seq_list) * (len(seq_list))/2
    count=0
    loopsTotal=0
    while seq_list:
        seq=seq_list[count]
        result=match_and_glue(master,seq)
        count+=1
        loopsTotal+=1
        print(loopsTotal)
        if result:
            count=0
            seq_list.remove(seq)
            master=result

    print(master)

if __name__=="__main__":
    main()

#python main.py example_easy_data_set.txt
#python main.py coding_challenge_data_set.txt