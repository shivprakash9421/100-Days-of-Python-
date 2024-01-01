# strings are immutable. 
name ="shivprakash"
print(name.upper())

word="ASkjfhSKFdjf"
print(word.lower())

a= "!!!!harry!!!!!!!"
print(a.rstrip("!"))

str3="   my sname is shiv  "
print(str3.strip())    #removes any white spaces before and after the string.

b="monkey"
print(b.replace("monkey", "donkey"))

print(a.replace("harry", "john"))

c = "shivprakash Dilip Chavan"
print(c.split(" "))

heading ="my NAME IS Shivprakash"
print(heading.capitalize())

line="2024 is year of success and hardwork!!!"
print(len(line))

print(line.center(55,"."))

print(len(line.center(55)))

print(line.endswith("!!!!!"))

print(line.endswith("of",4,15))

d='''The boy whose name is shivprakash is going to comebak in 2024 and 
he is following codwithharry '''

print(d.find("shivprakash"))
print(d.find("sumit"))

print(d.index("shivprakash"))
#print(d.index("rajesh")) it will give error

e="iwillscore100ineverysubject"
print(e.isalnum())

f="hardworkpaysoff110"
print(f.isalpha())

g="shivprakash is godfather"
print(g.islower())

h="CONSISTENSY IS KEY OF SUCCESS"
print(h.isupper())

str1 = "We wish you a Merry Christmas\n"
print(str1)
print(str1.isprintable())
#'\n', \'t', '\r', '\x16', '\xlf', and so on.

i="      "     #using spacebar or tab
print(i.isspace())

j="The Man With Vison Is Danger"
print(j.istitle())

str2="the man with vison is danger"
print(str2.title())

k="python is interprited language"
print(k.startswith("python"))

l="BREAKING BAD is THE best webseries FOR REAL"
print(l.swapcase())

m="SHE SELLS SEASHELLS ON THE SEA SHORE." #tounge twister
print(m.count("S"))

