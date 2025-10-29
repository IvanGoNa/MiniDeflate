
from src.LZ77 import LZ77, LZ77decompressor

def testLZ77(string_list, lab_length, sb_length):
    for index, string in enumerate(string_list):
        print("---------------- TEST ", index ," -----------------")
        print("String to compress: ", string)
        print("Result of compression: ", string_compressed := LZ77(string, lab_length, sb_length))
        print("Result of decompression: ", string_decompressed :=LZ77decompressor(string_compressed), "\n")
        assert string == string_decompressed


testing_list = ["ABAB", "ABCDEFABC", "ABABABABA", "AAAAAAA", "ABCDEFG", "ABABXABABY"]
testLZ77(testing_list, 4, 6)