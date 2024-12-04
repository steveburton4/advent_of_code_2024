install_requirements:
	pip3 install -r requirements.txt

get_answer:
	python3 "Day $(day)/day$(day).py"

run_tests:
	pytest -v -s

run_tests_for_day:
	pytest -v -s "Day $(day)/day$(day)_test.py"
