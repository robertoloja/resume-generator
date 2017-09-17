import json

resume_content_file = "contents.json"

with open(resume_content_file) as file:
    content = json.load(file)

print(content)
