import argparse, text_utils        #imports the argparse and text ultilites libraries
parser = argparse.ArgumentParser()    #allows arguments for filename
parser.add_argument('filename', type=str, help="The name of the file")
args = parser.parse_args()    #allows you to use argparse in other functions easily

def average_words():
  average = text_utils.count_words(args.filename)/text_utils.count_lines(args.filename) #uses the other functions to devide them to get answer
  return(average)
average_words()            #calls function
