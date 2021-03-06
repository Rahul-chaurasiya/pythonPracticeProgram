s1 = "geeks"
print(len(s1))

s2 = s1.upper()
print(s2)

s3 = s2.lower()
print(s3)
print(s1.islower())
print(s2.isupper())

#############################################

s = "GeeksforGeeks Python Course"

print(s.startswith("Geeks"))
print(s.endswith("Course"))
print(s.startswith("Geeks", 1))     # start index
print(s.startswith("Geeks",8,len(s)))   # start index, last-index

#########################################################

s1 = "geeks for geeks"
print(s1.split())   # split by space ' '

s2 = "geeks, for, geeks"
print(s2.split(','))        # split by comma ','

l = ["geeksforgeeks","python","course"]

print(" ".join(l))          # join by space
print(", ".join(l))         # join by comma

#######################################################

s1 = "__geeksforgeeks___"

print(s1.strip("_"))   # strip from both side
print(s1.lstrip('_'))  # strip from left side
print(s1.rstrip("_"))   # strip from right side

######################################################

s1 = "geeks for geeks"
s2 = "geeks"

print(s1.find(s2))
print(s1.find("gfg"))

n = len(s1)
print(s1.find(s2,1,n))