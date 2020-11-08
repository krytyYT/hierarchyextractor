import re

for line in [x.strip() for x in open(f'tokens.txt', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    file_object = open('kek.txt', 'a')
                    file_object.write("\n"+token)
                    file_object.close()