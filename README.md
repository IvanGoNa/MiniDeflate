# MiniDeflate : LZ77 + Huffman Compressor

## Description

This is a lightweight educational project aimed at understanding how data compression algorithms work. It implements LZ77 and Huffman coding in Python, as is similarly done in Deflate algorithm.

## Installation and Requirements

With Python 3.6 or higher should work fine. 

Clone the repository and navigate into it:

```
git clone https://github.com/tuusuario/MiniDeflate.git
cd MiniDeflate
```

No external dependencies are required.

## Features: What is implemented to this point?

For the moment the list below is implemented:
- **LZ77 compression**
- **LZ77 decompression**
- **MiniDeflate to compress any file**: It will generate a binary file named `output.lz77`
- **MiniDeflate to decompress `output.lz77`:** It generates a Markdown file named `dec.md`. 
- **MiniDeflate can be used with a Command-line interface with argparse**
- **testLZ77**: A simple test to ensure LZ77 compression and decompression works well with simple strings converted to bytes.
- **testRecovery**: A simple test to ensure compression and decompression works well with real markdown files.

>[!WARNING]
>This means compression and decompression is only fully implemented for Markdown files and only using LZ77 algorithm.

>[!NOTE] testRecovery
>This tests only ensures that a file that has been compressed and decompressed is identical to the original one. Usage: `python -m tests.testRecovery 'filename'`
## How to use MiniDeflate

MiniDeflate has to possibilites right now: compression and decompression. Currently is only using LZ77 algorithm. 

In order to compress a file, option `-c` or `--compress` should be used, the following instruction shows it:

```bash
python -m MiniDeflate -c 'filename'
```

This will generate a binary file called `output.lz77`, 

`output.lz77` content is the one that should be used to recover the original file. This is done with the option `-d` or `--decompress`, as shown in the instruction below:

```bash
python -m MiniDeflate -c 'output.lz77' #Or another filename, if is has been changed"
python -m MiniDeflate --decompress 'output.lz77'
```

## Roadmap: Next Steps

- Implement Huffman coding for compression
- Implement CRC for error detection
- Extend MiniDeflate to be able to handle other formats
- Encryption options 