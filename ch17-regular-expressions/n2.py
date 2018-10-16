import re

wordsnums = 'Arizona 479, 501, 870. California 209, 213, 650'

m = re.findall('\d', wordsnums)

print(m)
