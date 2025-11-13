
def LZ77(info, lab_length, sb_length):

    search_buffer= bytearray()
    look_ahead_buffer = info[0:lab_length] 
    compressed = []

    n_byte = 0; 
    while n_byte < len(info):
        
        byte_to_add = info[n_byte]
        distance_to_beginning = 0
        sequence_length = 0
        
        #If the byte byte_to_add is not in the search buffer we append (0,0,byte_to_add) 
        if byte_to_add in search_buffer:
            #We find the longest coincident sequence of the search buffer that imitates
            #the beginning of the look_ahead_buffer. 
            beginning, sequence_length= length_of_longest_coincident_sequence(search_buffer, look_ahead_buffer)      
            distance_to_beginning = len(search_buffer)-beginning
            byte_to_add = info[n_byte+sequence_length]  if (n_byte+sequence_length) < len(info) else None

        #We add to the search buffer those bytes present in the sequence found (if found)
        for i in range(0, sequence_length+1):
                if (n_byte + i) < len(info):
                    search_buffer.append(info[n_byte+i])

        n_byte += sequence_length + 1
        search_buffer = search_buffer[-sb_length:]
        look_ahead_buffer = info[n_byte: n_byte+lab_length]

        tuple = (distance_to_beginning, sequence_length, byte_to_add)
        compressed.append(tuple)

    return compressed

def length_of_longest_coincident_sequence(search_buffer, look_ahead_buffer):
    maximum_length = 0
    beginning_index = 0

    for sequence_length in range(0,len(look_ahead_buffer)):
            #Find the last position in search_buffer where the first sequence_length bytes of look_ahead_buffer appear.
            start_index = search_buffer.rfind(look_ahead_buffer[0:sequence_length])   
            if start_index != -1:
                maximum_length = sequence_length
                beginning_index = start_index
            else:
                break

    return beginning_index, maximum_length

def LZ77decompressor(compressed):
    decompressed = bytearray()
    for token in compressed:
        distance_to_beginning,sequence_length,byte_to_add = token
        #If sequence_length > 0, we copy sequence_length elements from the decompressed buffer, starting distance_to_beginning positions backwards.
        for _ in range(0,sequence_length):
            decompressed.append(decompressed[-distance_to_beginning])
        
        if byte_to_add != None:
            decompressed.append(byte_to_add)

    return decompressed