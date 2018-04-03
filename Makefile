.PHONY = init install clean test venv

bin/buildout=bin/buildout -Nt 4
bin/instance=bin/instance fg

bin/pip:
	@if test -f bin/pip; then echo "Virtualenv already created"; \
		else virtualenv-2.7 --no-setuptools . ; fi

bin/buildout: bin/pip
	./bin/pip install -r requirements.txt

start:
	$(bin/instance)

install: bin/buildout
	$(bin/buildout)

buildout: install

test: install
	bin/test

cleanall:
	rm -rf include bin parts lib develop-eggs
	rm -f .buildout.cfg .installed.cfg .mr.developer.cfg
