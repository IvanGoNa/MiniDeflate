# MiniDeflate : LZ77 + Huffman Compressor

## Description

This is a lightweight educational project aimed at understanding how data compression algorithms work. It implements LZ77 and Huffman coding in Python, as is similarly done in Deflate algorithm.

## Installation and Requirements

Works with Python 3.8 or later

Clone the repository and navigate into it:

```
git clone https://github.com/IvanGoNa/MiniDeflate.git
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

> ⚠️ **Warning:** This means compression and decompression is only fully implemented for text files and only using LZ77 algorithm.

> 🧪 **Test note - testRecovery:** This tests only ensures that a file that has been compressed and decompressed is identical to the original one. Usage: `python -m tests.testRecovery 'filename'`

## How to use MiniDeflate

MiniDeflate currently supports two operations: compression and decompression. Currently, it only uses LZ77 algorithm. 

In order to compress a file, option `-c` or `--compress` should be used, the following instruction shows it:

```bash
python -m MiniDeflate -c 'filename'
```

This will generate a binary file called `output.lz77`, 

`output.lz77` content is the one that should be used to recover the original file. This is done with the option `-d` or `--decompress`, as shown in the instruction below:

```bash
python -m MiniDeflate -d 'output.lz77' #Or another filename, if it has been changed
python -m MiniDeflate --decompress 'output.lz77'
```

## Examples

As an example of compression effectiveness up to this point, the first seven chapters of *Don Quixote* by Miguel de Cervantes has been used. It can be found in `./examples/quixote.txt`. The compressed file can be found in `./examples/compressedQuixote.lz77` as well as the result of the decompression `./examples/decompressedQuixote`.

- Original file size: 83.7KB
- Compressed file size: 63.9KB (76.3% of the original size)

After running testRecovery the following output is obtained:

```console
$~ python -m tests.testRecovery '.\examples\quixote.txt'
Files are Identical
```
## Roadmap: Next Steps

- Implement Huffman coding for compression
- Implement CRC for error detection
- Extend MiniDeflate to be able to handle other formats
- Encryption options 

## License 

This project is licensed under the [MIT License](./LICENSE).


Developed by Iván Gómez as part of a personal learning project of data compression