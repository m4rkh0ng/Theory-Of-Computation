import re # module for processing regular expressions https://docs.python.org/3/library/re.html
import sys
import csv
if __name__ == '__main__':
  # Exit if command line args entered incorrectly
  if len(sys.argv) != 2:
    print("usage: extract_links.py [input_file]")
    sys.exit(0)

# Filename is 2nd command line arg
filename = sys.argv[1]

# TODO Read HTML file
# curl https://stackoverflow.com > stackoverflow.html
with open(filename, encoding="utf8") as f:
  matches = re.findall('"((http)s?://.*?)"', f.read())

# TODO Set up regex

# TODO Find links using regex, save in list called 'matches'


# Check matches, print results
print(matches)

# TODO Read in links from answers.txt (hint...this is a CSV file), 
# save in list called 'answer_data'
with open(filename, encoding="utf8") as f:
  answer_data = re.findall('"((http)s?://.*?)"', f.read())

# Compare answers with matches found using regex, print out any mismatches
# UNCOMMENT BELOW WHEN READY TO CHECK IF YOUR REGEX IS FINDING ALL THE LINKS
result = "All links matched!"
if len( matches ) != len( answer_data ):
  result = "Your regex found %i matches. There should be %i matches" %(len( matches ), len( answer_data ) )
else:
  for i in range( len(answer_data) ):
    if( matches[i] != answer_data[i] ):
      result = "Mismatched link. Got %s but expected %s" % ( matches[i], answer_data[i] )
      break
print( result )
# TODO Read HTML file
# curl https://stackoverflow.com > stackoverflow.html
with open(filename, encoding="utf8") as f:
  matches = re.findall('"((http)s?://.*?)"', f.read())

# TODO Set up regex

# TODO Find links using regex, save in list called 'matches'


# Check matches, print results
print(matches)

# TODO Read in links from answers.txt (hint...this is a CSV file), 
# save in list called 'answer_data'
with open(filename, encoding="utf8") as f:
  answer_data = re.findall('"((http)s?://.*?)"', f.read())

# Compare answers with matches found using regex, print out any mismatches
# UNCOMMENT BELOW WHEN READY TO CHECK IF YOUR REGEX IS FINDING ALL THE LINKS
result = "All links matched!"
if len( matches ) != len( answer_data ):
  result = "Your regex found %i matches. There should be %i matches" %(len( matches ), len( answer_data ) )
else:
  for i in range( len(answer_data) ):
    if( matches[i] != answer_data[i] ):
      result = "Mismatched link. Got %s but expected %s" % ( matches[i], answer_data[i] )
      break
print( result )