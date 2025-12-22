

import argparse

from src.huffman import Huffman
from src.lz77 import LZ77

def main():
    parser = argparse.ArgumentParser(prog ='MiniDeflate', 
                                     description='A mini-compressor for text files using LZ77 and Huffmann coding', 
                                     add_help=True)
    
    #We either have to compress or decompress
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c', '--compress', action="store_true", help="Compress file")
    group.add_argument('-d', '--decompress', action="store_true", help="Decompress file")


    parser.add_argument('filename', help="Input file path")

    args = parser.parse_args()
    compressor = Huffman()

    if args.compress:

        with open(args.filename, "rb") as file:
            data = file.read()
            
        compressed_data = compressor.compress(data)

        with open("output.mdf", "wb") as file:
            file.write(compressed_data)

    if args.decompress:

        with open(args.filename, "rb") as file:
            data = file.read()

        decompressed = compressor.decompress(data)

        with open("dec.md", "wb") as output:
            output.write(decompressed)


if __name__=="__main__":
    main()