# Usage

Python 3 is used.

To have output saved to a file:
```
python3 reconstruct.py <folder_path/filename> <outputfilename.txt>
e.g.
python3 reconstruct.py test_data_sets/coding_challenge_data_set.txt output.txt
```

To directly print to screen and not write to any output files:
```
python3 reconstruct.py <folder_path/filename>
e.g.
python3 reconstruct.py test_data_sets/coding_challenge_data_set.txt
```

To run tests:
```
python3 unit_test.py
or
python3 integrated_tests.py
```

# Requirements

* Output a unique sequence that contains each of the given input strings as a substring. Given the following inputs:
  * Total file size < 50 sequences
  * Each sequence <= 10000chars
  * There exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length
  * No guarentee that adjacent entries in the input file will have overlaps
  * Sequences are different lengths
* Assumptions:
  * No two sequences will erroneously overlap with a third sequence. For example, the following is assumed to not ever happen: aabb, bbc, bbd (bbc and bbd are in contention)
  * All subsequences in the input file will get used and there aren't any subsequences that match but don't grow the string. E.g. aabbcc and bbcc (the bbcc substring doesn't grow the string)
  
    ```
    Example input:
    `>Frag_56
    `ATTAGACCTG
    `>Frag_57
    `CCTGCCGGAA
    `>Frag_58
    `AGACCTGCCG
    `>Frag_59
    `GCCGGAATAC

    Example of overlapping and building the output:
    >Frag_56: ATTAGACCTG
    >Frag_58:    AGACCTGCCG
    >Frag_57:       CCTGCCGGAA
    >Frag_59:          GCCGGAATAC
    output:   ATTAGACCTGCCGGAATAC
    ```


# Overview of solution

There are two problems here:

1. String matching subproblem (See my `match_and_glue` function in reconstruct.py and additional description below)
  * Googling shows that Boyer-Moore seems to be the standard for efficient string search algorithms. Futher googling showed that Cpython already implements a variant of this (Boyer–Moore–Horspool), which results in an average run-time of O(k), where k is the length of the string to be searched against. See https://news.ycombinator.com/item?id=1976275. And https://hg.python.org/cpython/file/tip/Objects/stringlib/fastsearch.h

2. All-pairs matching problem using string matching described above 
  * Form a growing master sequence and keep gluing sequences into it (See my `reconstruct` function in reconstruct.py and description below)



# What my `match_and_glue` function does
This function attempts to match two sequences on either sides (left or right):

1. It takes one character more than half of the shorter of the two sequences (to satisfy the "more than half" condition) and then sees if this half is in the longer string (CPython's "substring in string" check uses Boyer–Moore–Horspool)
2. If this substring is in the nose or tail section of the longer string, see if the remainder of the longer string also matches the substring. Only the nose or tail section of the longer string is checked in order to save time. The Nose and tail sizes that are checked against are set to the length of the smaller substring. (It's pointless to check the middle of the longer substring to see if there are matches if a match doesn't result in growing the strings)
3. If the above conditions are met, perform the glue, otherwise, return False

```    
Example:
smaller_string =    aabbcde
longer_string  = aaaaabbcd
1. Get just more than half of aabbcdd: aabb
    a) Is this piece inside the longer string? If so, make note of where the match occured
        Yes, as shown:
           aabb
        aaaaabbcd
2. Do the remainders of the sub-strings also match?
    Yes:
    a) Remainder of longer-string: 
        cd (length = 2)
    b) Remainder of smaller string:
        cde
    c) Remainder of smaller string up to same length as remainder of longer-string:
        cd (length=2)
3. Perform the glue starting at the location of where the match occured:
       aabbcde
    aaaaabbcd
    -----------
    aaaaabbcde
```   


# Thoughts on  Runtime

Runtime is O(n^2\*k). Where n is the total number of segments and k is average length of the segment. The n^2 term comes from the all-pairs matching. The k comes from the Boyer-Moore string search. Perhaps the n^2 can be avoided if substrings were hashed and looked up. But since it's "more than" half of a substring that will match another string (not exactly half), this means all possible substrings more than half would need to be hashed. That's potentially n\*k hashes (or 5000, which is greater than n^2, where n=50). There might be ways to transform the string to a frequency domain and/or cluster and group the segments by similarity and only search through similar groups or do some sort of graph search, but that is a little too advanced for the scope of this challenge. So currently, it doesn't seem that the n^2 term is avoidable. 


# Explaination on other parts of the code

* The `read_input` function in `reconstruct.py` reads the input file and concatenates lines to return a list of sequences, it is called by the reconstruct function
* The `reconstruct` function in `reconstruct.py` first calls the `read_input` function to get the list of sequences and then loops over the list while calling the `match_and_glue` function in each iteration in attempt to glue each sequence to a growing master sequence. If there is a match and a glue is performed, the smaller sequence is removed from the list so it won't be needlessly used again, and the looping is restarted to find the next sequence that can be matched and glued to the master sequence. The master sequence is initialized by taking one of the sequences in the list of sequences. 
* `unit_test.py` currently just tests the match_and_glue function
* `integrated_tests.py` tests whole input and outputs. Most of the tests make sure that all the inputs are seen in the output, as it should be