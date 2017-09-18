#!/usr/local/bin/python3
import math
import json

number_of_columns = 3

def readHTML(file):
    with open(file) as f:
        return f.readlines()

def renderToFile(file, template, numcols, input):
    with open(file, "w+") as output:
        for line in template:
            if "<%" in line: #TODO: Turn this into <%-- section -->
                generateHTML(input, line.split(" ")[1], output, numcols)
            else:
                print(line, file=output)

def generateHTML(input, section, output, numcols):
    for i in range(numcols):
        print("<ul class='talent'>", file=output)
        colsize = int(math.ceil(len(input[section]) / numcols))

        col = [input[section][x] for x in range(i, len(input[section]), numcols)]

        for j in range(colsize - 1):
            print("<li>" + col[j] + "</li>", file = output)

        print("<li class='last'>" +
                (col[-1] if len(col) == colsize else "") + "</li>",
                file = output)
        print("</ul>", file = output)

with open("contents.json") as f:
    content = json.load(f)

for medium in ["print", "web"]:
    renderToFile("resume-" + medium + ".html",
                 readHTML("templates/" + medium + "_template.html"),
                 number_of_columns,
                 content)
