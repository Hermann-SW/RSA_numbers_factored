
all:

validate: RSA_numbers_factored.gp
	echo "\q" | gp -q $< 2>&1 | cat > /tmp/out
	diff validate.good /tmp/out
	rm -f /tmp/out
