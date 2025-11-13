
from src.lz77 import LZ77

def testLZ77(string_list, lab_length, sb_length):
    compressor = LZ77()
    for index, string in enumerate(string_list):
        print("---------------- TEST ", index ," -----------------")
        print("String to compress: ", string)
        print("Result of compression: ", string_compressed := compressor.compress(string, lab_length, sb_length))
        print("Result of decompression: ", string_decompressed := compressor.compress(string_compressed), "\n")
        assert string == string_decompressed


testing_list = [b"ABAB", b"ABCDEFABC", b"ABABABABA", b"AAAAAAA", b"ABCDEFG", b"ABABXABABY"]
testLZ77(testing_list, 4, 6)