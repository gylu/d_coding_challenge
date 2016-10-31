
import sys
import math
import io


def read_input(input_file):
    """
    INPUT: filename.txt
    OUTPUT: name_list, seq_list 
    name_list has list of names of the sequences in the input file.  (e.g. >Rosalind_1836)
    seq_list has a list of the actual values
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
    Glue only occurs if more than half of one sequence overlaps with the other and there are additional new characters in the glued sequence
    This function attempts to match on both sides (left or right):
        1. It takes one character more than half of the shorter of the two sequences (to satisfy the "more than half") and then sees if it is in the longer string
        2. If this substring is in nose section or tail section longer string, see if the remainder of the substring also overlaps. I only check nose or tail section in order to save time. Nose and tail sizes are set to the length of the smaller substring. (It's pointless to check the middle of the longer substring to see if there are matches if a match doesn't result in growing the strings)
        3. If the remaining substring also matches, the glue them together
        See readme.md on github for more detail
    """
    if len(seq1)<len(seq2):
        small_seq=seq1
        other_seq=seq2
    else:
        small_seq=seq2
        other_seq=seq1
    len_small_seq=len(small_seq)
    substr_lefthalf=small_seq[0:len(small_seq)//2+1] #get substring that's the first half of the string plus one more character
    substr_righthalf=small_seq[math.ceil(len(small_seq)/2)-1::]
    temp=False
    if substr_lefthalf in other_seq[len(other_seq)-len_small_seq:]: #check only the rightmost characters up to the length of the small sequence. Checking for the tail ends instead of the whole string seems to save about 40% of time
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
    elif substr_righthalf in other_seq[0:len_small_seq]: #same as above, except try matching the right side of the shorter string against the left side of the long string
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


def reconstruct(input_file):
    """
    INPUT: file path with filename to the input file.
    OUTPUT: a glued output sequence
    """
    name_list,seq_list=read_input(input_file)
    master_seq=''
    master_seq=seq_list.pop()
    max_loops=1+(len(seq_list)*(len(seq_list)+1) )/2 #esentially n*(n+1)/2 loops, only allow this amount of loops to run
    count=0
    loops_total=0
    while seq_list:
        if loops_total < max_loops:
            seq=seq_list[count]
            result=match_and_glue(master_seq,seq)
            count+=1 #count is used to loop through all of the remaining subsequences that haven't yet been glued
            if result:
                count=0 #if a matching subsequence was found, remove it from the list, and start over with finding the next match
                seq_list.remove(seq)
                master_seq=result
        else:
            raise Exception("Exceeded number of expected iterations required to find solution. Iterations ran: ", loops_total)
        loops_total+=1
        #print("loops_total: ",loops_total)
    return master_seq


def main(args):
    input_file=args[1]
    master_seq=reconstruct(input_file)
    if len(args)>2: #if 2 arguments were given in the commnand line, such as "python reconstruct.py arg1 arg2" then treat arg2 as the filename to write output to
        with open(args[2], "w") as file:
            file.write(master_seq)
    else:
        print(master_seq)

if __name__=="__main__":
    args=sys.argv
    main(args)

#python reconstruct.py test_data_sets/example_easy_data_set.txt
#python reconstruct.py test_data_sets/coding_challenge_data_set.txt