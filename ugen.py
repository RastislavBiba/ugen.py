import sys, getopt

def help():
    """
    :return: Instruction text
    """
    return("this is instructions for you:\n")

def nickname(forename, middle, surname):
    """
    Generate nickname from input parameters
    :param forename:
    :param middle:
    :param surname:
    :return: nickname
    """
    forename_short = forename[0]
    surname_short = surname[0:6:1]
    if middle != '':
        middle_short = middle[0]
        nickname = forename_short+middle_short + surname_short
        nickname = nickname.lower()
    else:
        nickname = forename_short + surname_short
        nickname = nickname.lower()
    return nickname

count_arguments = len(sys.argv)
def main():
    """
    Main function to open I/O files from arguments using getopt
    :return:
    output file with list of nickanmes
    """

    if len(sys.argv)>1:

        #getopt function
        inputfiles= []
        try:
            argv = sys.argv[1:]
            opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
        except getopt.GetoptError:
            print(help())
            sys.exit(2)

        for opt, arg in opts:
            if opt == '-h':
                help()
                sys.exit()
            elif opt in ("-i", "--ifile"):
                inputfiles.append(arg)


            elif opt in ("-o", "--ofile"):
                outputfile = arg


        # write to opend output file
        output_file = open(outputfile, 'w')

        #read input line by line and split if :
        for inputfile in inputfiles:
            with open(inputfile, 'r') as f:

                for index, line in enumerate(f):
                    x = line.split(":")
                    if len(x)>3:
                        #indexing parts of nickname
                        forename = x[1]
                        middlename = x[2]
                        surname = x[3]
                        #insert nickname into list
                        x.insert(1, nickname(forename, middlename, surname))
                    output = ':'.join(map(str, x))
                    output_file.write(output)
                output_file.write("\n")

    else:
        print(help())


if __name__ == '__main__':
    main()