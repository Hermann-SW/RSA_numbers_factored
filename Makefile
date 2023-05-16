
all: eslint


eslint: sq2.eslint sq2_mpzjs.eslint

%.eslint: %.js
	@eslint $<

sq2: sq2.js
	@nodejs $< > /tmp/out
	@diff python/sq2.py.out /tmp/out
	@rm -f /tmp/out

sq2_: sq2.js
	@node $< > /tmp/out
	@diff python/sq2.py.out /tmp/out
	@rm -f /tmp/out

sq2_mpzjs: sq2_mpzjs.js
	@nodejs $< > /tmp/out
	@diff python/sq2.py.out /tmp/out
	@rm -f /tmp/out

sq2_mpzjs_: sq2_mpzjs.js
	@node $< > /tmp/out
	@diff python/sq2.py.out /tmp/out
	@rm -f /tmp/out
