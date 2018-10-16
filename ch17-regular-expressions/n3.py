import re

sentence = 'The ghost that says boo haunts the loo.'

booo = re.findall('.oo', sentence)

print(booo)
