#!/usr/bin/env python

"""First assignement
"""
import argparse
import logging
import time
import string

logging.basicConfig(level=logging.DEBUG)


def process(file_path):
    """Reads a text file and compile the letter statistics."""
    start_time = time.time()

    logging.info("Reading input file %s...", file_path)
    with open(file_path) as input_file:
        text = input_file.read()
    num_chars= len(text)
    logging.info("Done, %d charaters found.", num_chars)

    #char_dict = {chr(x): 0 for x in range(ord('a'), ord('z') +1)}
    char_dict = {ch: 0 for ch in string.ascii_lowercase}
    logging.info("%s", char_dict)
    for ch in text:
        ch = ch.lower()
        if ch in char_dict:
            char_dict[ch] += 1.0

    elapsed_time = time.time() - start_time
    logging.info("Done in %.3f seconds.", elapsed_time)
    num_letters = sum(char_dict.values())
    logging.info("Numero delle lettere totali %d", num_letters)

    for ch, num in char_dict.items():
        print("{} -> {:.3%}".format(ch, num/num_letters))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, help="Path to the input file")
    args = parser.parse_args()

    process(args.infile)
