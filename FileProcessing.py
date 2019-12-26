'''
Author : Shyam Ramkumar
Given a source file and target file, the program compares the files and provides an output.
The output contains each line of source and how many times have the occured in a given target file.
'''
import glob
import csv
import time
#from re import search
def main():
	'''
	Main function to be called in the python program.
	Contains:
		input file path or source file path
		Target directory path containing list of files to be read and compared with
		Output file path to write the output of the program
	'''
	input_file_path = r"C:\Users\sramkumar\Desktop\customer\Sheik\Folder.txt"
	target_dir = r"C:\Users\sramkumar\Desktop\customer\Sheik\comparison"
	output_file_path = r"C:\Users\sramkumar\Desktop\customer\Sheik\output.txt"
	Anomalypath = []
	target_comp_files = []
	#Open the input file
	fin = open(input_file_path,'r')
	#Read lines and store it in a variable 'input'
	for item in fin:
		Anomalypath.append(item)
	fin.close()
	#For target file paths in a folder:
		#store file paths in a variable
	for filepath in glob.glob(target_dir+"\*.*"):
		target_comp_files.append(filepath)

	Fileprocessing(target_comp_files,Anomalypath,output_file_path)
		

def Fileprocessing(target_comp_files,inputfile_lines,output):
	'''
	Compare two list and output occurence of each item in list 1 in list 2 to a dictionary
	'''
	dictout = {}
	for item in target_comp_files:
		target_path_list = []
		print("Processing File: ", item)
		#Open target file
		ftarget = open(item,'r')
		#Read lines in the file and store in a variable 'target#'
		for line in ftarget:
			target_path_list.append(line)
		ftarget.close()
		#For each line in 'input':
		#Set counter to 0
		#If line is matching with corresponding line in 'target#'
			#increment the count
		#add line in 'input' to dictionary - line and count
		for line in inputfile_lines:
			#print("Source: ",line)
			#time.sleep(1)
			counter = 0
			for target in target_path_list:
				#print("target: ",target)
				#time.sleep(1)
				#print("Result: ",line in target)
				#if line in target: #due to some reason I get false all the time
				#if search(str(line),str(target)):
				if target.find(line.strip()) !=-1:
					#print(line)
					#print(target)
					counter += 1 
			dictout[line.strip()] = counter
	fout = open(output,'+a',newline='')
	#fout.write(item)
	#fout.write("\n") 
	#fout.write("\n") 
	dic = csv.writer(fout)
	#fout.write(dictout) cannot write dictionary using write function. This function writes only strings.
	for key,val in dictout.items():
		dic.writerow([key,val])
	fout.close()	
	

main()