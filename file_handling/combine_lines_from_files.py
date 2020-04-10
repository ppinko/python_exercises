"""
Write a Python program to combine each line from first file with the
corresponding line in second file.
Additionally add line numbers to newly created file.
"""

def combined_file(first, second, new):
    with open (first) as f, open(second) as s, open (new, mode='w') as n:
        count = 0
        while True:
            l1 = f.readline()
            l2 = s.readline()
            if len(l1) == 0 and len(l2) == 0:
                break
            elif len(l1) == 0:
                n.write("{} ".format(count) + l2)
            elif len(l2) == 0:
                n.write("{} ".format(count) + l1)
            else:
                n.write("{} ".format(count) + l1.rstrip() + " " + l2)
                count += 1

combined_file("txt_A.txt", "txt_B.txt", "txt_C.txt")


                
            
