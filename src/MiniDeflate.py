

import argparse

from src.LZ77 import LZ77, LZ77decompressor


def main():
    #https://docs.python.org/es/3/library/argparse.html#argumentparser-objects
    parser = argparse.ArgumentParser(prog ='MiniDeflate', 
                                     description='A mini-compressor for text files using LZ77 and Huffmann coding', 
                                     add_help=True)
    
    #We either have to compress or decompress
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c', '--compress', action="store_true", help="Compress file")
    group.add_argument('-d', '--decompress', action="store_true", help="Decompress file")


    parser.add_argument('filename', help="Input file path")

    #https://ellibrodepython.com/python-argparse
    args = parser.parse_args()
    
    if args.compress:
        #https://www.w3schools.com/python/ref_func_open.asp
        with open(args.filename, "rb") as file:
            #utf-8 is giving problems, I'll have to fix that, for the moment latin1 is ok for testing
            data = file.read()
            compressed = LZ77(data, lab_length=17000, sb_length=32000)
            file.close()

        with open("output.lz77", "wb") as file:
            for p,n,c in compressed:
                #We use 2 bytes for numbers (n & p < 65.536)
                file.write(p.to_bytes(2,'big'))
                file.write(n.to_bytes(2,'big'))
                file.write(bytes([c]))

            file.close

    if args.decompress:
        with open(args.filename, "rb") as file:
            compressed = []
            while True:
                #Each tuple in our compressed files were 5 bytes long
                tuple = file.read(5)
                #We read until no more t
                if len(tuple) < 5:
                    break
                #https://www.geeksforgeeks.org/python/how-to-convert-bytes-to-int-in-python/
                p = int.from_bytes(tuple[0:2], "big")
                n = int.from_bytes(tuple[2:4], "big")
                #I get a strange error if done tuple[4].decode(...) -> tells me tuple[4] is an int
                c = tuple[4]#.to_bytes().decode("latin1")

                compressed.append((p,n,c))
            file.close
        
        #We encode it with latin1 and then we tell that the 
        decompressed =  LZ77decompressor(compressed)#.encode("latin1")
        with open("decompressed.md", "wb") as output:
            output.write(decompressed)
            output.close


if __name__=="__main__":
    main()