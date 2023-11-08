.PHONY: rep clean

FILE = main

rep:
	xelatex -synctex=1 -interaction=nonstopmode $(FILE).tex
	mv main.pdf "Моделирование_2_ИУ7-76_КовельАД.pdf"

clean:
	rm *.aux *.bbl *.blg *.log *.out *.toc pages/*.aux inc/*.aux inc/*.bbl inc/*.blg inc/*.log inc/*.out inc/*.toc *.synctex.gz
	echo "Clear:Ready"