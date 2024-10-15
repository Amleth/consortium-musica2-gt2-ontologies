python3 concatenate_md.py
# pandoc output.md --pdf-engine=lualatex -o output.pdf -V geometry:margin=1in
pandoc output.md -o output.docx --filter=mermaid-filter
pandoc output.md -o output.html --filter=mermaid-filter