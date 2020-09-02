# Read from the file file.txt and output the tenth line to stdout.
# This will get to the 10th line, immediately quit, and delete the line which prints it too.
sed '10q;d' file.txt
