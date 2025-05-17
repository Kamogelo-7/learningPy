import re

txt = "They better stay alive i've seen the end, ooh, ohh"
text = [x for x in txt if "they" in x]
reveal = re.findall("^The.alive", text)

print(type(reveal))
