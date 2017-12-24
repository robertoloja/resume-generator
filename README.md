## Goals
1. Separate content from presentation in my resume.
2. Files should be read and used to generate both web and print versions.
3. Auto-generate pdf, without having to open the html file and print as pdf.

## Approach
The contents.json file holds the values of fields, corresponding to tags in
templates/*.html. The tags are of form <%i-- field -->.

contents.json looks like this:

{
    "Languages": [
        "COBOL",
        "FORTRAN",
        "etc..."
    ],

    "Databases": [
        "SQL",
        "etc..."
    ],

    "etc...": [
        "etc..."
    ]
}

## TODO
1. Don't just insert the lists of languages, skills, etc, but also name, contact 
   information, and education (and publications? work experience? projects?).
2. 
