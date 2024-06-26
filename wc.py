import argparse
import os
import sys


def count_file(filepath: str, multi_byte=False):
    with open(filepath, 'r') as file:
        max_line_length = 0
        line_count = 0
        multibyte_char_count = 0
        word_count = 0
        word_count = 0
        for line in file.readlines():
            line = line.strip()
            line_count += 1
            multibyte_char_count += len(line)
            word_count += len(line.split())
            if l := len(line) > max_line_length:
                max_line_length = l

        return {
            'line_count': line_count,
            'word_count': word_count,
            'char_count': multibyte_char_count if multi_byte else os.path.getsize(filepath),
        }


def parse_input(args=None):
    parser = argparse.ArgumentParser(
        prog='wc',
        description='outputs character, word and line counts',
        epilog='https://codingchallenges.fyi/challenges/challenge-wc'
    )

    parser.add_argument('filename')
    parser.add_argument('-c',
                        help='The number of bytes in the input file is written to the standard output.', action='store_true')
    parser.add_argument('-l',
                        help='The number of lines in the input file is written to the standard output.', action='store_true')
    parser.add_argument('-m',
                        help='The number of characters in each input file is written to the standard output.  If the current locale does not support multibyte characters, this is equivalent to the -c option.', action='store_true')
    parser.add_argument('-w',
                        help='The number of words in each input file is written to the standard output.', action='store_true')
    if args:
        return vars(parser.parse_args(args))
    else:
        return vars(parser.parse_args())


if __name__ == '__main__':
    if len(sys.argv) < 3:
        file_contents = sys.stdin.read()
        args = parse_input([file_contents, sys.argv[1]])
        f = open('input.tmp', 'w')
        f.write(file_contents)
        f.close()
        counts = count_file('input.tmp', args['m'])
    else:
        args = parse_input()
        counts = count_file(args['filename'], args['m'])

    # If all argument switches are false, then display standard info
    if len(list(filter(lambda i: False if i[0] == 'filename' else i[1] if i[1] == True else False, args.items()))) == 0:
        print(
            f"{counts['line_count']}\t{counts['word_count']}\t{counts['char_count']}\t{args['filename']}")
    else:
        # display only data that's requested
        print(
            f"{str(counts['line_count']) + "\t" if args['l'] is True else ''}{str(counts['word_count']) + "\t" if args['w'] is True else ''}{str(counts['char_count']) + "\t" if args['c'] is True else ''}{args['filename']}")
