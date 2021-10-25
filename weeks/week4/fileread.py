filename = "texto.txt"

# try:
#     with open(filename) as data_file:
#             for line in data_file:
#                 print(line.strip())

#             #contents = data_file.read(1)
#             #content2 = data_file.readlines()
#             #content3 = data_file.read()
            
#             print(contents)
#             #print(content2)
#             #print(content3)
# catch FileNotFoundError:
#     print("File not found")


line = "Joe Bloggs,A00654321,80.5,77.5"
#name,student_id,ai,cdd = line.split(",")

#print(cdd)
#print(type(cdd))
name,student_id,results = line.split(",")


# name,student_id,results = line.split(",", maxsplit=2)

# print(results)
# print(type(results))        

       