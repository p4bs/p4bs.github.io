#!/usr/bin/python
# encoding: utf8

data = [
    "After work",
    "Blåsväder",
    "Blunda",
    "Dåndimpen",
    "Duktig",
    "Dygna",
    "Fika",
    "Fulsnygg",
    "Harkla",
    "Hejhej",
    "Hen",
    "Hinna",
    "Jhu",
    "Jobbig",
    "Kaffegäsp",
    "Kramsnö",
    "Lördagsgodis",
    "Lagom",
    "Mysfaktor",
    "Ombudsman",
    "Orka",
    "Ovän",
    "Påtår",
    "Söndagsångest",
    "Skadeglädje",
    "Smörgåsbord",
    "Snackpåse",
    "Snuskhummer",
    "Spillevink",
    "Tappa sugen",
    "Tvättid",
    "Vabba",
    "Vabruari",
    "Vaska",
    "Vobba"
]

template =\
"""<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta property="og:url" content="http://takeovertheword.com/word_pages/{word_url}" />
        <meta property="og:title" content='{word}!' />
        <meta property='og:image' content='http://takeovertheword.com/word_pages/img/{image_file}' />
        <meta property="og:description" content="Time to start learning some Swedish." />
        <meta http-equiv="refresh" content="0; url=http://takeovertheword.com/" />
    </head>
    <body>
    </body>
</html>
"""

for word in data:
    with open("{0}.html".format(word), 'w') as word_file:
        word_file.write(template.format(word_url="{0}.html".format(word), word=word, image_file="{0}.png".format(word.lower())))
        print "http://takeovertheword.com/word_pages/{word_url}.html".format(word_url=word)