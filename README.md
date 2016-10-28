# d_coding_challenge

Example input:

>Frag_56
ATTAGACCTG
>Frag_57
CCTGCCGGAA
>Frag_58
AGACCTGCCG
>Frag_59
GCCGGAATAC

Example output:
ATTAGACCTGCCGGAATAC

Example of how to piece together the output
Frag_56: ATTAGACCTG
Frag_57:       CCTGCCGGAA
Frag_58:    AGACCTGCCG
Frag_59:          GCCGGAATAC
output:  ATTAGACCTGCCGGAATAC

Building it in order
Frag_56: ATTAGACCTG
Frag_58:    AGACCTGCCG
Frag_57:       CCTGCCGGAA
Frag_59:          GCCGGAATAC


Requirements:
-Output a unique sequence that contains each of the given input strings as a substring. Given the following inputs:
  -Total file size < 50 sequences
  -Each sequence <= 10000chars
  -Some sequences will overlap with others for more than half their length
-There exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length
-No guarentee that adjacent entries in the input file will have overlaps
-Sequences are different lengths

Assume

Initial thoughts:
There are two problems here:
* String matching subproblem
* All-pairs matching problem

Need to find matching strings






More random thoughts
Thoughts on pseudocode:
If any 2 sequences match more than 50% of their lengths, combine them to form a new sequence


Two ways of attacking the problem:
* Form a primary sequence and keep taking and merging sequences into it
* Keep taking pairs and merging them (then only further merging with previously paired/merged), this won't work, because won't be able to determine whether it's 50% that matches or not
