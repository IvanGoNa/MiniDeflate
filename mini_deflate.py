

import argparse

from src.lz77 import LZ77, LZ77decompressor


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
    
    if args.compress:
        with open(args.filename, "rb") as file:
            data = file.read()
            compressed = LZ77(data, lab_length=17000, sb_length=32000)
            file.close()

        with open("output.lz77", "wb") as file:
            for p,n,c in compressed:
                #We use 2 bytes for numbers (n & p < 65.536)
                file.write(p.to_bytes(2,'big'))
                file.write(n.to_bytes(2,'big'))
                if c is not None:
                    file.write(c.to_bytes(1,'big'))

            file.close()

    if args.decompress:
        with open(args.filename, "rb") as file:
            compressed = []
            while True:
                #Each tuple in our compressed files are 5 bytes long
                token = file.read(5)
                #We read until no more tuples are left
                if len(token) < 4:
                    break
                p = int.from_bytes(token[0:2], "big")
                n = int.from_bytes(token[2:4], "big")
                try:
                    c = token[4]
                except IndexError:
                    c = None

                compressed.append((p,n,c))
            file.close
        
        decompressed = LZ77decompressor(compressed)
        with open("dec.md", "wb") as output:
            output.write(decompressed)


if __name__=="__main__":
    main()