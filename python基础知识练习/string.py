#s='11abc22abc33abc44abc55'
#s1=s.replace('abc','')
#print s1
#s='11abc22abc33abc44abc55'
#first=s.find('abc')
#s1=s[first+3:]
#s1=s1.replace('abc','')
#s=s[0:first+3]+s1
#print s
s='11abc22abc33abc44abc55'
s1=s.find('abc')
s2=s[s1+3:]
s3=s2.replace('abc','')
s=s[:s1+3]+s3
print s


