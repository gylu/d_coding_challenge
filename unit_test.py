import unittest
from reconstruct import match_and_glue

class TestMatchAndGlue(unittest.TestCase):
    def test_seq1_longer(self):
        seq1='01234567'
        seq2='678'
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,'012345678')

    def test_seq2_longer(self):
        seq2='01234567'
        seq1='678'
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,'012345678')

    def test_seq1_not_exist(self):
        seq2='01234567'
        seq1='333'
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,False)

    def test_seq2_not_exist(self):
        seq2='01234567'
        seq1='333'
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,False)

    def test_morechars(self):
        seq2='012345678'
        seq1='345678xx'
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,'012345678xx')

    def test_morechars2(self):
        seq1='012345678'
        seq2='345678xx'
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,'012345678xx')

    def test_eqlen(self):
        seq2='012345678'
        seq1='345678xxx'
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,'012345678xxx')


    def test_eqlen2(self):
        seq1='012345678'
        seq2='345678xxx'
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,'012345678xxx')

    def test_new_stuff_longer(self):
        seq1='012345678'
        seq2='345678xxxxxxx'
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,'012345678xxxxxxx')

    def test_new_stuff_longer2(self):
        seq2='012345678'
        seq1='345678xxxxxxx'
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,'012345678xxxxxxx')        

    def test_one_empty(self):
        seq1='012345678'
        seq2=''
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,False)

    def test_one_empty2(self):
        seq2='012345678'
        seq1=''
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,False)

    def test_one_small(self):
        seq2='012345678'
        seq1='56'
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,False)

    def test_one_all_inside(self):
        seq1='012345678'
        seq2='1234567'
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,False)

    def test_one_all_inside2(self):
        seq2='012345678'
        seq1='1234567'
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,False)

    def test_one_side_inside1(self):
        seq1='12345678'
        seq2='012345678'
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,False)

    def test_one_side_inside2(self):
        seq2='12345678'
        seq1='012345678'
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,False)

    def test_one_side_inside3(self):
        seq1='01234567'
        seq2='012345678'
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,False)

    def test_one_side_inside4(self):
        seq2='01234567'
        seq1='012345678'
        output=match_and_glue(seq1,seq2)
        self.assertEqual(output,False)


if __name__ == '__main__':
    unittest.main()