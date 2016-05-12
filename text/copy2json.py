#!/usr/bin/python
# encoding: utf8

import json

jlist = []
with open('copy.md', 'r') as copyfile:
    words = copyfile.read().split("\n\n")
    for word in words:
        w_dic = {}
        w_parts = word.split('\n')
        # Split first part
        first_line = w_parts[0]
        first_space = first_line.find(' ')
        w_dic['id'] = first_line[1:first_space]

        first_lbracket = first_line.find('[')
        w_dic['word'] = first_line[first_space+1:first_lbracket].strip()

        w_dic['phonetic'] = first_line[first_lbracket+1:-1]

        # Second part
        w_dic['meaning'] = w_parts[1].split("=")[1][1:]

        # Third part
        w_dic['explanation'] = w_parts[2]

        # Extra
        w_dic["audio-file"] = "{0}{1}.mp3".format(w_dic['id'], w_dic['word'].replace(' ', ''))
        w_dic["share-url"] = "{0}.html".format(w_dic['word'])
        jlist.append(w_dic)

with open('copy.json', 'w') as joutput:
    json.dump(jlist, joutput, indent=2)

print jlist
