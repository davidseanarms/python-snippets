import os 

file1 = input("Enter file 1: ")
file2 = input("Enter file 2: ")

if not os.path.exists(file1) or not os.path.exists(file2):
    print("Error: Invalid file path!")
    exit()

fp1 = open(file1, 'r')
fp2 = open(file2, 'r')

fp1_size = len(fp1.readlines())
fp2_size = len(fp2.readlines())
if fp1_size != fp2_size:
    print("Error: Files are not of the same size!")
    exit()

fp1.seek(0) # reset the read pointer back to the beginning
lines1 = fp1.readlines()
lines2 = fp2.readlines()

difference_count = 0

for i in range(len(lines1)):
    if lines1[i] != lines2[i]:
        difference_count += 1
        print("Difference found at line number:", i+1)

print("Number of differences found:", difference_count)

fp1.close()
fp2.close()
