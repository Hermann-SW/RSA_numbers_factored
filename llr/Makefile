
405:
ifneq ($(shell uname -m),x86_64)
	@echo "for x86_64 only"
else
	rm -rf llr405src
	cat llr405src.zip.xaa llr405src.zip.xab > llr405src.zip
	unzip -x llr405src.zip 2>&1 > /dev/null
	#patch llr405src/Llr.c < patchfile 2>&1 | cat > /dev/null
	cd llr405src/linux64llr; make sllr64 2>&1 | cat > /dev/null
	cp llr405src/linux64llr/sllr64 .
	./sllr64 ${t} -d -q"33218925*2^169690+1" -oSVtsqrtm1=16
ifneq ($(shell which gp),)
	./gp_verify 33218925 169690 tsqrtm1_9441050
endif
endif

381:
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
	rm -rf llr38lsrc llr405src llr405src.zip
	rm -f sllr64 err lresults.txt llr.ini z*
