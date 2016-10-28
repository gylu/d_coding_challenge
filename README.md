# George's d_coding_challenge

Example input:

`>Frag_56
`ATTAGACCTG
`>Frag_57
`CCTGCCGGAA
`>Frag_58
`AGACCTGCCG
`>Frag_59
`GCCGGAATAC

Example output:
ATTAGACCTGCCGGAATAC

Example of how to piece together the output
`Frag_56: ATTAGACCTG
`Frag_57:       CCTGCCGGAA
`Frag_58:    AGACCTGCCG
`Frag_59:          GCCGGAATAC
output:  ATTAGACCTGCCGGAATAC

Building it in order
`Frag_56: ATTAGACCTG
`Frag_58:    AGACCTGCCG
`Frag_57:       CCTGCCGGAA
`Frag_59:          GCCGGAATAC


Requirements:
* Output a unique sequence that contains each of the given input strings as a substring. Given the following inputs:
  * Total file size < 50 sequences
  * Each sequence <= 10000chars
  * Some sequences will overlap with others for more than half their length
* There exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length
* No guarentee that adjacent entries in the input file will have overlaps
* Sequences are different lengths


Initial thoughts:
There are two problems here:
1. String matching subproblem
* Doing some googling shows that Boyer-Moore seems to be the fastest string search algorithm. Futher googling showed that Cpython already implements this.
2. All-pairs matching problem using 1.
* Two ways of attacking the problem:
 * Form a growing master sequence and keep gluing sequences into it
 * Keep taking pairs and merging them (then only further merging with previously paired/merged), this won't work, because won't be able to determine whether it's 50% that matches or not


* What my string matching function does:
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
