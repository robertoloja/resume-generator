#!/usr/local/bin/python3
import math
import json

number_of_columns = 3

def openHTML(file):
    with open(file) as f:
        return f.readlines()


def renderToFile(file, template, inputJSON):
    with open(file, "w+") as output:
        for line in template:
            if "<%" in line: #TODO: Turn this into <%-- section -->
                generateHTML(inputJSON, line.split(" ")[1], output, number_of_columns)
            else:
                print(line, file=output)


def generateHTML(inputJSON, section, output, numcols):
    for i in range(numcols):
        print("<ul class='talent'>", file=output)
        colsize = int(math.ceil(len(inputJSON[section]) / numcols))

        col = [inputJSON[section][x] for x in range(i, len(inputJSON[section]),
            numcols)]

        for j in range(colsize - 1):
            print("<li>" + col[j] + "</li>", file = output)

        print("<li class='last'>" +
                (col[-1] if len(col) == colsize else "") + "</li>",
                file = output)
        print("</ul>", file = output)


with open("contents.json") as f:
    content = json.load(f)

print_template = openHTML("templates/print_template.html")
web_template = openHTML("templates/web_template.html")

renderToFile("resume-print.html", print_template, content)
renderToFile("resume-web.html", web_template, content)
