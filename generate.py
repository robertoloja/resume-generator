#!/usr/local/bin/python3
import math
import json

number_of_columns = 3

def readHTML(file):
    with open(file) as f:
        return f.readlines()


def renderToFile(file, template, c, JSON):
    """Write to file, based on template, arranged into c columns, from JSON."""
    with open(file, "w+") as output:
        for line in template:
            if "<%--" in line:
                print(generateHTML(JSON, line.split(" ")[1], c),
                      file=output)
            else:
                print(line, file=output)


def generateHTML(JSON, section, c):
    """Return c columns of html, corresponding to section of JSON."""
    html = ""
    for i in range(c):
        html += "<ul class='talent'>"
        size = int(math.ceil(len(JSON[section]) / c))
        col = [JSON[section][x] for x in range(i, len(JSON[section]), c)]

        for j in range(size - 1):
            html += "<li>" + col[j] + "</li>"

        html += "<li class='last'>"
        html += col[-1] if len(col) == size else ""
        html += "</li></ul>"
    return html


with open("contents.json") as f:
    content = json.load(f)

for medium in ["print", "web"]:
    renderToFile("resume-" + medium + ".html", readHTML("templates/" + medium +
                 "_template.html"), number_of_columns, content)
