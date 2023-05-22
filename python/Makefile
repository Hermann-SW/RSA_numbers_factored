
all:
	@echo "targets: doc|doc_diff|pylint|black|validate|clean"

doc: docs/RSA_numbers_factored.py.md RSA_numbers_factored.py

doc_diff: docs/RSA_numbers_factored.py.md
	git diff $< | grep -v "^[-+]<a href" | \
            grep -v "^ ## <kbd>" | \
            grep -v "^ ### <kbd>" | \
            grep -v "^@@ " | \
            grep -v "^ $$" | \
            grep -v "^ ---"; true

docs/RSA_numbers_factored.py.md: RSA_numbers_factored.py Makefile
	lazydocs $<
	sed -i "s# \(\`\`\`\)\$$#\n\1#;s#\(\*\*Example.*:\*\*\)#\1\n#;s#<b>\`_\`</b>:##" $@

pylint: RSA_numbers_factored.pylint2 RSA_svg.pylint Pydroid3_demo.pylint sq2.pylint 10000.gaussian_gcd.pylint2

%.pylint2: %.py
	pylint --ignore-long-lines="\d{92}" --max-module-lines=2500 $<

%.pylint: %.py
	pylint $<

black: RSA_numbers_factored.py
	black $<
	make validate

validate: RSA_numbers_factored.py
	python $< > /tmp/out
	diff validate.good /tmp/out
	rm -f /tmp/out

sq2: sq2.py
	@python $< > /tmp/out
	@diff /tmp/out sq2.py.out
	@rm -f /tmp/out

sq2_gmpy2: sq2.py
	@python $< gmpy2 > /tmp/out
	@diff /tmp/out sq2.py.out
	@rm -f /tmp/out

clean:
	rm -f docs/*.py.md /tmp/out
