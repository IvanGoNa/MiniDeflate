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
            compressed = compressor.compress(data)
            file.close()

with open("output.lz77", "wb") as file:
    for p,n,c in compressed:
        file.write(p.to_bytes(2,'big'))
        file.write(n.to_bytes(2,'big'))
        if c is not None:
            file.write(c.to_bytes(1,'big'))

    file.close()


######################### DECOMPRESSION #################################
with open("output.lz77", "rb") as file:
    compressed = []
    while True:
        #Each tuple in our compressed files were 5 bytes long
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
        
    decompressed = compressor.decompress(compressed)
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