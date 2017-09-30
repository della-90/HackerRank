for _ in range(int(input())):
    s = input()
    inverse_chars = list(s[::-1])
    
    # find the first index where there is a letter followed by a lower one (in reversed string)
    index = None
    for i in range(len(inverse_chars)-1):
        if inverse_chars[i+1] < inverse_chars[i]:
            index = i+1
            break
            
    if not index:
        print("no answer")
    else:
        # letter to be replaced
        letter = inverse_chars[index]
        
        # find lowest greater letter (the replacement)
        remaining_chars = inverse_chars[index-1::-1]
        replacement = min(filter(lambda x: x>letter, remaining_chars))
        
        # start building output
        result = "".join(inverse_chars[:index:-1])
        result += replacement
        
        # the last part of the result needs to be sorted
        del inverse_chars[inverse_chars.index(replacement)]
        result += "".join(sorted(inverse_chars[:index]))
        print(result)
        
