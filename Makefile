CWD="`pwd`"
MODVIS_HOME ?= $(CWD)
MODVIS_CODE=$(MODVIS_HOME)
NEW_PYTHONPATH=$(MODVIS_CODE):$(PYTHONPATH)

setup:
	pip install -r requirements.txt

run:
	@sh -ac 'PYTHONPATH=$(NEW_PYTHONPATH) python app/server.py'