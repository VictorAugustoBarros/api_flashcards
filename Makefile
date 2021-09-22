black:
	black --line-length 110 --target-version py37 Flashcards/ Card/

pydocstyle:
	pydocstyle Flashcards/ Card/

run:
	python manage.py runserver 0.0.0.0:8001
