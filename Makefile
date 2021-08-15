install:
	echo "Installing tool"
	python3 -W ignore -m pip install . -q
	which shazam-charts
	echo "Installed"

test:
	echo "Running tests"
	python3 -m unittest "tests/cli_test.py"
	python3 -m unittest "tests/results_test.py"