default:
	python3 generate-manifest-with-key.py

old-reddit-redirect.zip: *.json *.js img/* *.md *.txt
	zip -r old-reddit-redirect.zip * -x .git/* -x img/screenshot.png -x .gitignore -x Makefile

clean:
	rm -f *.zip
	rm -f manifest.json 
