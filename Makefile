
all: eslint


eslint: sq2.eslint sq2_mpzjs.eslint

%.eslint: %.js
	@eslint $<

sq2: sq2.js
	@nodejs $< > /tmp/out
	@diff python/sq2.py.out /tmp/out
	@rm -f /tmp/out

sq2_mpzjs: sq2_mpzjs.js
	@nodejs $< > /tmp/out
	@diff python/sq2.py.out /tmp/out
	@rm -f /tmp/out
