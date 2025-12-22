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
- **Huffman compression**
- **Huffman decompression**
- **mini_deflate to compress any file**: It will generate a binary file named `output.mdf`
- **mini_deflate to decompress `output.mdf`:** It generates a Markdown file named `dec.md`. 
- **mini_deflate can be used with a Command-line interface with argparse**
- **test_lz77**: A simple test to ensure LZ77 compression and decompression works well with simple strings converted to bytes.
- **test_recovery**: A simple test to ensure compression and decompression works well with real markdown files.

> ⚠️ **Warning:** This means compression and decompression is only fully implemented for text files and using LZ77 or Huffman algorithm separately. For the moment The only way to choose if LZ77 or Huffman coding is used for compression and decompression is by modifying line 22 in mini_deflate.py

> 🧪 **Test note - test_Recovery:** This tests only ensures that a file that has been compressed and decompressed is identical to the original one. Usage: `python -m tests.test_recovery 'filename'`

## How to use MiniDeflate

MiniDeflate currently supports two operations: compression and decompression. Currently, it only uses LZ77 or Huffman coding  algorithm separately. 

In order to compress a file, option `-c` or `--compress` should be used, the following instruction shows it:

```bash
python -m mini_deflate -c 'filename'
```

This will generate a binary file called `output.mdf`, 

`output.mdf` content is the one that should be used to recover the original file. This is done with the option `-d` or `--decompress`, as shown in the instruction below:

```bash
python -m mini_deflate -d 'output.mdf' #Or another filename, if it has been changed
python -m mini_deflate --decompress 'output.mdf'
```

## Examples

As an example of compression effectiveness up to this point, using LZ77, the first seven chapters of *Don Quixote* by Miguel de Cervantes has been used. It can be found in `./examples/quixote.txt`. The compressed file can be found in `./examples/compressedQuixote_lz77.mdf` as well as the result of the decompression `./examples/decompressedQuixote_lz77.md`.

- Original file size: 83.7KB
- Compressed file size: 63.9KB (76.3% of the original size)

There is included as well an example of a compression using Huffman coding, with the same file. The compressed file can be found in `./examples/compressedQuixote_huffman.mdf` as well as the result of the decompression `./examples/decompressedQuixote_huffman.md`. 

- Original file size: 83.7KB
- Compressed file size: 47.5KB (56.8% of the original size)

After running testRecovery with both cases (Huffman and LZ77) the following output is obtained:

```console
$~ python -m tests.test_recovery '.\examples\quixote.txt'
Files are Identical
```

For the moment, if it is desired to change which method test_recovery.py uses,  it should be chosen inside the code (modifying line 10 in test_recovery.py).
## Roadmap: Next Steps

- Unify Huffman and LZ77
- Implement CRC for error detection
- Extend MiniDeflate to be able to handle other formats
- Encryption options 

## License 

This project is licensed under the [MIT License](./LICENSE.md).


Developed by Iván Gómez as part of a personal learning project of data compression