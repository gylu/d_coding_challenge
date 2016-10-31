import unittest
import os
import reconstruct
test_data_sets_folder='test_data_sets/'

class Test_entire(unittest.TestCase):
    def test_simple_example_write_to_file(self):
        input_file='example_easy_data_set.txt'
        output_file="output_"+input_file
        input_path=test_data_sets_folder+input_file
        try:
            os.remove(output_file)
        except OSError:
            pass
        args=['', input_path, output_file]
        reconstruct.main(args)
        output=''
        with open(output_file, 'r') as myfile:
            output=myfile.read().replace('\n', '')
        self.assertEqual(output,'ATTAGACCTGCCGGAATAC')

    def test_all_inputs_are_in_output_string(self):
        input_file='coding_challenge_data_set.txt'       
        output_file="output_"+input_file
        input_path=test_data_sets_folder+input_file
        try:
            os.remove(output_file)
        except OSError:
            pass
        args=['',input_path, output_file]
        print("args: ", args)
        name_list,seq_list=reconstruct.read_input(input_path) 
        reconstruct.main(args)
        output=''
        with open(output_file, 'r') as myfile:
            output=myfile.read().replace('\n', '')
        count=0   
        for seq in seq_list:
            count+=1
            print("count: ", count, ". seq: ", seq)
            self.assertIn(seq,output)

    def test_all_rows_are_in_output_string(self):
        input_file='coding_challenge_data_set.txt'       
        output_file="output_"+input_file
        input_path=test_data_sets_folder+input_file
        try:
            os.remove(output_file)
        except OSError:
            pass
        args=['',input_path, output_file]
        print("args: ", args)
        all_lines=[]
        with open(input_path) as f:
            for line in f:
                all_lines.append(line.replace('\n', ''))
        reconstruct.main(args)
        output=''
        with open(output_file, 'r') as myfile:
            output=myfile.read().replace('\n', '')
        count=0   
        for line in all_lines:
            if line.startswith('>'):
                count+=1
            else:
                self.assertIn(line,output)
            print("subseq_num: ", count, ". subseq: ", line)


    def test_all_inputs_are_in_output_string_in_order(self):
        input_file='in_order_easy_data_set.txt'       
        output_file="output_"+input_file
        input_path=test_data_sets_folder+input_file
        try:
            os.remove(output_file)
        except OSError:
            pass
        args=['',input_path, output_file]
        print("args: ", args)
        name_list,seq_list=reconstruct.read_input(input_path) 
        reconstruct.main(args)
        output=''
        with open(output_file, 'r') as myfile:
            output=myfile.read().replace('\n', '')
        count=0   
        for seq in seq_list:
            count+=1
            print("count: ", count, ". seq: ", seq)
            self.assertIn(seq,output)
 

if __name__ == '__main__':
    unittest.main()