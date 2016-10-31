import unittest
import os
import reconstruct
test_data_sets_folder='test_data_sets/'

class Test_entire(unittest.TestCase):
    def test_simple_example_write_to_file(self):
        input_file='example_easy_data_set.txt'
        output_file="output_"+input_file
        input_file=test_data_sets_folder+input_file
        output_file=test_data_sets_folder+output_file
        try:
            os.remove(output_file)
        except OSError:
            pass
        args=['', input_file, output_file]
        reconstruct.main(args)
        output=''
        with open(output_file, 'r') as myfile:
            output=myfile.read()
        self.assertEqual(output,'ATTAGACCTGCCGGAATAC')

    def test_simple_example_write_to_file2(self):
        input_file='example_easy_data_set2.txt'
        output_file="output_"+input_file
        input_file=test_data_sets_folder+input_file
        output_file=test_data_sets_folder+output_file
        try:
            os.remove(output_file)
        except OSError:
            pass
        args=['', input_file, output_file]
        reconstruct.main(args)
        output=''
        with open(output_file, 'r') as myfile:
            output=myfile.read()
        self.assertEqual(output,'xAAAAAAAAAAAAABBBBBCCCCCCCCCCxddx')

    def test_simple_example_write_to_file3(self):
        input_file='example_easy_data_set3.txt'
        output_file="output_"+input_file
        input_file=test_data_sets_folder+input_file
        output_file=test_data_sets_folder+output_file
        try:
            os.remove(output_file)
        except OSError:
            pass
        args=['', input_file, output_file]
        reconstruct.main(args)
        output=''
        with open(output_file, 'r') as myfile:
            output=myfile.read()
        self.assertEqual(output,'xAAAAAAAAAAAAABBBBBCCCCCCCCCCxddx')

    def test_all_input_sequences_are_in_output_string(self):
        input_file='coding_challenge_data_set.txt'       
        output_file="output_"+input_file
        input_file=test_data_sets_folder+input_file
        output_file=test_data_sets_folder+output_file
        try:
            os.remove(output_file)
        except OSError:
            pass
        args=['',input_file, output_file]
        print("args: ", args)
        name_list,seq_list=reconstruct.read_input(input_file) 
        reconstruct.main(args)
        output=''
        with open(output_file, 'r') as myfile:
            output=myfile.read()
        count=0   
        for seq in seq_list:
            count+=1
            print("count: ", count, ". seq: ", seq)
            self.assertIn(seq,output)

    def test_all_input_sequences_are_in_output_string2(self):
        input_file='in_order_easy_data_set.txt'       
        output_file="output_"+input_file
        input_file=test_data_sets_folder+input_file
        output_file=test_data_sets_folder+output_file
        try:
            os.remove(output_file)
        except OSError:
            pass
        args=['',input_file, output_file]
        print("args: ", args)
        name_list,seq_list=reconstruct.read_input(input_file) 
        reconstruct.main(args)
        output=''
        with open(output_file, 'r') as myfile:
            output=myfile.read()
        count=0   
        for seq in seq_list:
            count+=1
            print("count: ", count, ". seq: ", seq)
            self.assertIn(seq,output)

    def test_all_input_rows_are_in_output_string(self):
        input_file='coding_challenge_data_set.txt'       
        output_file="output_"+input_file
        input_file=test_data_sets_folder+input_file
        output_file=test_data_sets_folder+output_file
        try:
            os.remove(output_file)
        except OSError:
            pass
        args=['',input_file, output_file]
        print("args: ", args)
        all_lines=[]
        with open(input_file) as f:
            for line in f:
                all_lines.append(line.replace('\n', ''))
        reconstruct.main(args)
        output=''
        with open(output_file, 'r') as myfile:
            output=myfile.read()
        count=0   
        for line in all_lines:
            if line.startswith('>'):
                count+=1
            else:
                self.assertIn(line,output)
            print("subseq_num: ", count, ". subseq: ", line)

    def test_all_input_rows_are_in_output_string2(self):
        input_file='coding_challenge_data_set_reordered.txt'       
        output_file="output_"+input_file
        input_file=test_data_sets_folder+input_file
        output_file=test_data_sets_folder+output_file
        try:
            os.remove(output_file)
        except OSError:
            pass
        args=['',input_file, output_file]
        print("args: ", args)
        all_lines=[]
        with open(input_file) as f:
            for line in f:
                all_lines.append(line.replace('\n', ''))
        reconstruct.main(args)
        output=''
        with open(output_file, 'r') as myfile:
            output=myfile.read()
        count=0   
        for line in all_lines:
            if line.startswith('>'):
                count+=1
            else:
                self.assertIn(line,output)
            print("subseq_num: ", count, ". subseq: ", line)
 
    def test_different_order_inputs_result_in_same_output(self):
        input_file1='coding_challenge_data_set.txt'       
        output_file1="output_"+input_file1
        input_file1=test_data_sets_folder+input_file1
        output_file1=test_data_sets_folder+output_file1
        input_file2='coding_challenge_data_set_reordered.txt'       
        output_file2="output_"+input_file2
        input_file2=test_data_sets_folder+input_file2
        output_file2=test_data_sets_folder+output_file2
        try:
            os.remove(output_file1)
            os.remove(output_file2)
        except OSError:
            pass
        args1=['',input_file1, output_file1]
        args2=['',input_file2, output_file2]
        print("args1: ", args1)
        print("args2: ", args2)
        reconstruct.main(args1)
        reconstruct.main(args2)
        output1='a'
        output2='b'
        with open(output_file1, 'r') as myfile:
            output1=myfile.read()
        output2=''
        with open(output_file2, 'r') as myfile:
            output2=myfile.read()
        self.assertEqual(output1,output2)

    def test_different_ordered_inputs_result_in_same_output2(self):
        input_file1='in_order_easy_data_set.txt'       
        output_file1="output_"+input_file1
        input_file1=test_data_sets_folder+input_file1
        output_file1=test_data_sets_folder+output_file1
        input_file2='example_easy_data_set.txt'       
        output_file2="output_"+input_file2
        input_file2=test_data_sets_folder+input_file2
        output_file2=test_data_sets_folder+output_file2
        try:
            os.remove(output_file1)
            os.remove(output_file2)
        except OSError:
            pass
        args1=['',input_file1, output_file1]
        args2=['',input_file2, output_file2]
        print("args1: ", args1)
        print("args2: ", args2)
        reconstruct.main(args1)
        reconstruct.main(args2)
        output1='a'
        output2='b'
        with open(output_file1, 'r') as myfile:
            output1=myfile.read()
        output2=''
        with open(output_file2, 'r') as myfile:
            output2=myfile.read()
        self.assertEqual(output1,output2)

    def test_raises_exception_due_to_incorrect_input(self):
        input_file='example_easy_data_set4.txt'
        output_file="output_"+input_file
        input_file=test_data_sets_folder+input_file
        output_file=test_data_sets_folder+output_file
        try:
            os.remove(output_file)
        except OSError:
            pass
        args=['', input_file, output_file]
        self.assertRaises(Exception,reconstruct.main,args)

if __name__ == '__main__':
    unittest.main()