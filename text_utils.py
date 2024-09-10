def count_chars(text):
    file = open(text, 'r')  # opens file
    data = file.read()      # reads file
    file.close()            # closes file
    return len(data)        # returns the character count

def count_words(text):
    number_of_words = 0 
    file = open(text, 'r')     # opens file
    data = file.read()
    words = data.split()       # splits the words
    number_of_words += len(words)  # counts the number of words
    file.close()
    return number_of_words

def count_sentences(text):
    file = open(text, 'r')
    lines= list(file)
    file_contents = file.read()
    file.close()
    words_all = 0
    for line in lines: 
        words_all = words_all + len(line.split())  # splits each line
    full_stops = 0
    for stop in lines:
        full_stops = full_stops + len(stop.split('.')) # seperates each sentence and counts them
    return full_stops

def count_lines(text):
  file = open(text, 'r')    
  lines = file.readlines()     
  linelist = []                # creates a list
  for line in lines:
    linelist.append((line))    # appends each line
  file.close()                 
  x = (int(len(linelist)))     # counts the lines
  return x   

