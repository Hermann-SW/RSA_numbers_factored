
all: docs/RSA_numbers_factored.py.md

docs/RSA_numbers_factored.py.md: RSA_numbers_factored.py
	lazydocs $<
	sed -i "s# \(\`\`\`\)\$$#\n\1#;s#\(\*\*Example.*:\*\*\)#\1\n#" $@

clean:
	rm docs/*.py.md
