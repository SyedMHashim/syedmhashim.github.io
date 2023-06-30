""" Script to convert Markdown files into HTML files"""
import sys

import markdown


def convert(file_name):
    """ 
    Convert a Markdown file into HTML file, 
    where `file_name` is the path to the Markdown file to be converted.
    """
    with open(file_name, "r", encoding="UTF-8") as file:
        text = file.read()
        html = markdown.markdown(
            text,
            extensions=[
                "attr_list",
                "md_in_html",
                "markdown.extensions.tables",
                "pymdownx.superfences",
            ],
        )
        ## Formatting fixes
        fix_list = [
            ("./docs/", ""),
            ("<code>", "<pre>"),
            ("</code>", "</pre>"),
        ]
        for fix_item in fix_list:
            html = html.replace(fix_item[0], fix_item[1])

        return html


if __name__ == "__main__":
    FILE_NAME = sys.argv[1]
    print(convert(FILE_NAME))
