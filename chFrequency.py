word = input("Enter Word: ")
ch_freq_count = {} 
for ch in word:
    if ch not in ch_freq_count:
        ch_freq_count[ch] = 1
    else:
        ch_freq_count[ch] = (ch_freq_count[ch] + 1)
print(ch_freq_count)
    