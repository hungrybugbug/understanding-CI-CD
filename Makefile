install:
	pip install -r requirements.txt
run:
	python3 app.py
	flask run
test:
	pytest test_app.py		