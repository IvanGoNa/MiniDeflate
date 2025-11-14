import argparse
from src.lz77 import LZ77

parser = argparse.ArgumentParser(prog ='testRecovery', 
                                     description='A test command to prove is the result of MiniDeflate after decompression remains identical to the original file', 
                                     add_help=True)
parser.add_argument('filename', help="Input file path")
args = parser.parse_args()
compressor = LZ77()
######################### COMPRESSION #################################

with open(args.filename, "rb") as file:
            data = file.read()

compressed_data = compressor.compress(data)
compressor.write("output.lz77", compressed_data)


######################### DECOMPRESSION #################################
compressed_data = compressor.read("output.lz77")

decompressed = compressor.decompress(compressed_data)

with open("dec.md", "wb") as output:
    output.write(decompressed)


######################### ARE BOTH FILES IDENTICAL? #################################
with open(args.filename, "rb") as f1, open("dec.md", "rb") as f2:
    a = f1.read()
    b = f2.read()

for i, (x, y) in enumerate(zip(a, b)):
    if x != y:
        print(f"Different byte found in position {i}: {x} vs {y}")
        break
else:
    print("Files are Identical")