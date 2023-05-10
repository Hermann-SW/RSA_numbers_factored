
all:

sq2: sq2.cc.out
	@./sq2.cc.out > /tmp/out
	@diff ../python/sq2.py.out /tmp/out
	@rm /tmp/out

sq2.cc.out: sq2.cc
	g++ -O3 $< -lgmpxx -lgmp -o $<.out

cpplint: sq2.cc
	cpplint --filter=-legal/copyright $<

cppcheck: sq2.cc
	cppcheck --enable=all --suppress=missingIncludeSystem $< --check-config

clean:
	rm -f sq2.cc.out /tmp/out
