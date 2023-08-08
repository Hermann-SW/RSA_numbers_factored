
all:
ifneq ($(shell uname -m),x86_64)
	@echo "for x86_64 only"
else
	rm -rf llr38lsrc
	unzip -x llr38lsrc.zip 2>&1 > /dev/null
	patch llr38lsrc/Llr.c < patchfile 2>&1 | cat > /dev/null
	cd llr38lsrc/gwnum; make -f make64 2>&1 | cat > /dev/null
	cd llr38lsrc/linux64llr; make sllr64 2>&1 | cat > /dev/null
	cp llr38lsrc/linux64llr/sllr64 .
	./sllr64 -d -q"33218925*2^169690+1" 2>err
	tail -4 err | cut -b-50
ifneq ($(shell which python),)
	python verify.py err 33218925 169690
endif
endif

clean:
	rm -rf llr38lsrc
	rm -f sllr64 err lresults.txt
