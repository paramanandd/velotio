
def rev_string():
  sample = "reverse"
  str = ""
  for a in sample:
    str = a + str
  return str

print(rev_string())
sample = "reverse"
count = 0
for a in sample:
  count += 1
print(count)

#should be min 8 char
#atleast 1 special chr
#atleast 1 symbol

sample_string = "CHec@k125"
string_lower = sample_string.lower()
contains_letter = string_lower.islower()
if contains_letter == True:
  print("String contains character")

special_characters = "!@#$%^&*()-+?_=,<>/"
for c in sample_string:
  if c in special_characters:
    print("special character exist")
