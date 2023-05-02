
all:
	@echo "targets: doc|doc_diff|pylint|black|validate|clean"

doc: docs/RSA_numbers_factored.py.md RSA_numbers_factored.py

doc_diff: docs/RSA_numbers_factored.py.md
	git diff $< | grep -v "^[-+]<a href" | \
            grep -v "^ ## <kbd>" | \
            grep -v "^ ### <kbd>" | \
            grep -v "^@@ " | \
            grep -v "^ $$" | \
            grep -v "^ ---"

docs/RSA_numbers_factored.py.md: RSA_numbers_factored.py Makefile
	lazydocs $<
	sed -i "s# \(\`\`\`\)\$$#\n\1#;s#\(\*\*Example.*:\*\*\)#\1\n#;s#<b>\`_\`</b>:##" $@

pylint: RSA_numbers_factored.py
	pylint --ignore-long-lines="\d{92}" --max-module-lines=2500 $<

black: RSA_numbers_factored.py
	black $<
	make validate

validate: RSA_numbers_factored.py
	python $< > /tmp/out
	diff validate.good /tmp/out
	rm -f /tmp/out

clean:
	rm -f docs/*.py.md /tmp/out
