"""
Create a new file by adding line number to the end of a line and title it
"""

def titled_file(old, new):
    with open (old, mode='r') as reader, open (new, mode='w') as writer:
        count = 0
        while True:
            line = reader.readline()
            if (len(line) == 0):
                break
            writer.write(line.rstrip().title() + " {}\n".format(count))
            count += 1

titled_file("txt_A.txt", "txt_D.txt")
                
            
