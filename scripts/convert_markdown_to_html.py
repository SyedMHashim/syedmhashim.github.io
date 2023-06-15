import sys
import markdown


def convert(file_name):
    # Load Markdown content
    with open(file_name, "r", encoding="UTF-8") as f:
        text = f.read()
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
    file_name = sys.argv[1]
    print(convert(file_name))
