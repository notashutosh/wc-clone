import argparse


def count_file(filepath: str):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='wc',
        description='outputs character, word and line counts',
        epilog='https://codingchallenges.fyi/challenges/challenge-wc'
    )

    parser.add_argument('filename')
    parser.add_argument('-L',
                        help='Write the length of the line containing the most bytes (default) or characters (when -m is provided) to standard output.')
    parser.add_argument('-c',
                        help='The number of bytes in the input file is written to the standard output.')
    parser.add_argument('-l',
                        help='The number of lines in the input file is written to the standard output.')
    parser.add_argument('-m',
                        help='The number of characters in each input file is written to the standard output.  If the current locale does not support multibyte characters, this is equivalent to the -c option.')
    parser.add_argument('-w',
                        help='The number of words in each input file is written to the standard output.')

    args = vars(parser.parse_args())

    count_file(args['filename'])
