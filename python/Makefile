
all:
	@echo "targets: doc|pylint|validate"

doc: docs/RSA_numbers_factored.py.md

docs/RSA_numbers_factored.py.md: RSA_numbers_factored.py Makefile
	lazydocs $<
	sed -i "s# \(\`\`\`\)\$$#\n\1#;s#\(\*\*Example.*:\*\*\)#\1\n#;s#<b>\`_\`</b>:##" $@

pylint: RSA_numbers_factored.py
	pylint --ignore-long-lines="\d{30}" $<

validate: RSA_numbers_factored.py
	@python $<

clean:
	rm docs/*.py.md
