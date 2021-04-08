import numpy 

def get_flag(data_lst):
    """compares machine's score and human's score stored in lists of list, 
    and returns flags which are indicated by the comparison.
    data_lst list"""
    flag_lst = []
    for scores in data_lst:
        # 1st is machine score, 2nd is human score 
        machine_score = scores[0]
        human_score = scores[1]
        # if machine score is greater or equal to human score,
        # assign the flag as "Machine"
        if machine_score >= human_score:
            flag_lst.append("Machine")
        # otherwise, as "Human"
        else:
            flag_lst.append("Human")
    return flag_lst

def write_out_flags(flag_lst, file_name):
    """writes out the flag list into a txt file.
    flag_lst list
    file_name string"""
    with open(f'{file_name}', 'w') as f:
        for flag in flag_lst:
            f.write('%s\n' % flag)

def main():
    # reads npy files to get results
    data_2400 = numpy.load('2400_test-probs.npy').tolist()
    data_800 = numpy.load('800_test-probs.npy').tolist()
    # gets flag lists 
    flags_2400 = get_flag(data_2400)
    flags_800 = get_flag(data_800)
    # writes out flags into correspinding txt files
    write_out_flags(flags_2400, "2400flags.txt")
    write_out_flags(flags_800, "800flags.txt")

if __name__ == "__main__":
    main()
