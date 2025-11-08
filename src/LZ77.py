
def LZ77(data, lab_length, sb_length):

    #info to compress
    info = data
    #seºarch_buffer of length sb_length
    search_buffer= bytearray()

    #look ahead buffer of length lab_length
    lab = info[0:lab_length] 

    #contains the compressed info
    compressed = []

    n_byte = 0; 
    while n_byte < len(info):
        
        c = info[n_byte]
        p = 0
        n = 0
        
        #If the byte c is not in the search buffer we return (0,0,c) if not, we continue
        if c in search_buffer:
            #We find the longest coincident sequence of the search buffer that imitates
            #the beginning of the lab. 

            #n -> length of that sequence (n <= len(lab))
            #beginning -> where does the sequence start in the search buffer
            beginning,n= lengthOfLongestCoincidentSequenceOptimized(search_buffer, lab)

            #p-> number of backwards jumps to do to get from the current byte to the byte were the sequence starts      
            p = len(search_buffer)-beginning

            #c-> new byte to add to the tuple, is byte 0 if there is no more bytes to add <- This will have to change
            c = info[n_byte+n]  if (n_byte+n) < len(info) else None

        #We add to the search buffer those bytes present in the sequence found (if found)
        for i in range(0, n
                       +1):
                if (n_byte + i) < len(info):
                    search_buffer.append(info[n_byte+i])

        #We update the byte number
        n_byte += n + 1
        #We update the search buffer (we get the last sb_length bytes)
        search_buffer = search_buffer[-sb_length:]
        #We update the lab (from the next byte to lab_length bytes ahead)
        lab = info[n_byte: n_byte+lab_length]
        tuple = (p,n,c)
        compressed.append(tuple)

    return compressed

def lengthOfLongestCoincidentSequenceOptimized(search_buffer, lab):
    maximum_length = 0
    beginning_index = 0

    for n in range(0,len(lab)):
            #https://docs.python.org/3/library/stdtypes.html#bytes.rfind
            #Find the last position in search_buffer where the first n bytes of lab appear.
            start_index = search_buffer.rfind(lab[0:n])   

            if start_index != -1:
                maximum_length = n
                beginning_index = start_index
            else:
                break

    return beginning_index, maximum_length

def isBetween(a, b, c):
    #returns true if an integrer a is between b and c
    return (a > b and a < c)


def LZ77decompressor(compressed):
    decompressed = bytearray()
    #We analyze one tuple at a time
    for token in compressed:
        p,n,c = token
        #If n > 0, we copy n elements from the decompressed buffer,
        #starting p positions backwards.
        for _ in range(0,n):
            decompressed.append(decompressed[-p])
        
        #Append the next literal symbol c
        if c != None:
            decompressed.append(c)

    return decompressed

''' 
THIS VERSION OF lengthOfLongestCoinciedentSequence IS NOT CURRENTLY USED, IT IS PRESERVED TEMPORALLY

def lengthOfLongestCoincidentSequence(search_buffer, lab):
    #Searches the longest coincident sequence between search_buffer and lab and returns its length
    #and the beginning index. The sequence should be at the beggining of lab so if search_buffer = [a,b,c,d,e,f,g]
    #and lab = [c,d,a,b,c,d], it returns 2.

    maximum_length = 0
    counter = 0
    beginning_index = 0
    for index, value in enumerate(search_buffer): 
        #We start or continue counting if the counter is 0 and the value in search_buffer is
        #the first of lab (we start counting a new sequence), or if the counter is between
        #0 and the length of lab (we continue counting coincidences in a sequence).
        if (counter == 0 and value == lab[0]) or isBetween(counter, 0, len(lab)):
            if value == lab[counter]:
                counter+=1
            elif value == lab[0]:
                counter=1
            else:
                counter=0

            if counter >= maximum_length:
                maximum_length = counter
                beginning_index = index - counter + 1

        #If the counter is bigger than the length of the look ahead buffer we cannot continue looking
        #for coincidences, but is interesting for us to restart it to see if we can find a sequence with
        #same length but a bit nearer to the lab.

        if counter >= len(lab):
            counter = 0;    

    #If counter is not 0, we have found at least the possibility of a new sequence
    #that started in the search_buffer but we can continue in the look_ahead_buffer
    
    initial_index = index - counter + 1
    if counter > 0:
        i = 0
        while counter < len(lab):
            if lab[counter] == lab[i]:
                i+=1
                counter+=1
                #maximum_length = max(maximum_length, counter)
                if counter >= maximum_length:
                    maximum_length = counter
                    beginning_index = initial_index
            else:
                break

    return beginning_index, maximum_length
'''