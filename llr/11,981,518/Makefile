
all:

validate: validate.cc.out
	./validate.cc.out

validate.cc.out: validate.cc
	g++ -O3 $< -lgmpxx -lgmp -o $<.out

cpplint: validate.cc
	cpplint --filter=-legal/copyright $<

cppcheck: validate.cc
	cppcheck --enable=all --suppress=missingIncludeSystem $< --check-config

clean:
	rm -f validate.cc.out
