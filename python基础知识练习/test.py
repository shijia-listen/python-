import re

#print(re.findall("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>"))
#print(re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>"))
#print(re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>"))
re.search('(?P<name>[a-z]+)(?P<age>\d+)','jenny20danny23').group()

