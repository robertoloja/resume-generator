import json

resume_content_file = "contents.json"
print_template = "templates/print_template.html"
web_template = "templates/web_template.html"
resume = "resume.html"

with open(resume_content_file) as file:
    content = json.load(file)

with open(print_template) as file:
    pTemplate = file.read()

print(pTemplate)

# Overwrite/create file
with open(resume, "w+") as file:
