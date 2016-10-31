# George's d_coding_challenge


# Usage

To have output saved to a file:
```
python reconstruct.py `<folder_path/filename`> `<outputfilename.txt`>
e.g.
python reconstruct.py test_data_sets/coding_challenge_data_set.txt output.txt
```

To directly print to screen and not write to any output files:

```
python reconstruct.py `<folder_path/filename`>
e.g.
python reconstruct.py test_data_sets/coding_challenge_data_set.txt
```

To run tests:
```
python unit_test.py
or
python integreated_tests.py
```

# Requirements

* Output a unique sequence that contains each of the given input strings as a substring. Given the following inputs:
  * Total file size < 50 sequences
  * Each sequence <= 10000chars
  * Some sequences will overlap with others for more than half their length
* There exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length
* No guarentee that adjacent entries in the input file will have overlaps
* Sequences are different lengths
* Assumptions:
  * No two sequences will erroneously overlap with a third sequence. For example, the following is assumed to not ever happen: aabb, bbc, bbd (bbc and bbd are in contention)
  * All subsequences in the input file will get used
  
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

    Example output:
    ATTAGACCTGCCGGAATAC

    Example of how to piece together the output
    >Frag_56: ATTAGACCTG
    >Frag_57:       CCTGCCGGAA
    >Frag_58:    AGACCTGCCG
    >Frag_59:          GCCGGAATAC

    Building it in order
    >Frag_56: ATTAGACCTG
    >Frag_58:    AGACCTGCCG
    >Frag_57:       CCTGCCGGAA
    >Frag_59:          GCCGGAATAC
    output:   ATTAGACCTGCCGGAATAC
    ```

# Initial thoughts:

There are two problems here:

1. String matching subproblem (see my reconstruct.match_and_glue() function
  * Googling shows that Boyer-Moore seems to be the fastest string search algorithm. Futher googling showed that Cpython already implements this. https://hg.python.org/cpython/file/tip/Objects/stringlib/fastsearch.h

2. All-pairs matching problem using string matching described above (see my reconstruct.reconstruct() function)
  * Form a growing master sequence and keep gluing sequences into it



# What my `match_and_glue` function does:
This function attempts to match two sequences, on both sides (left or right):

1. It takes one character more than half of the shorter of the two sequences (to satisfy the "more than half") and then sees if it is in the longer string (CPython's "substring in string" check uses Boyer-Moore, which is best case Ω(n/m), worst case O(mn))
2. If this substring is in nose section or tail section longer string, see if the remainder of the substring also overlaps. I only check nose or tail section in order to save time. Nose and tail sizes are set to the length of the smaller substring. (It's pointless to check the middle of the longer substring to see if there are matches if a match doesn't result in growing the strings)
3. If it does, perform the glue

```    
Example:
smaller_string =    aabbcde
longer_string  = aaaaabbcd
1. Get just more than half of aabbcdd: aabb
    a) Is this piece inside the longer string?
        Yes, as shown:
           aabb
        aaaaabbcd
2. Is the remainder of the smaller substring also there?
    Yes:
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
```   
