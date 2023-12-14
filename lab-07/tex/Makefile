.PHONY: rep clean

FILE = main

rep:
	tectonic $(FILE).tex
	mv main.pdf "7_Моделирование_ИУ7-76_КовельАД.pdf"

clean:
	rm *.aux *.bbl *.blg *.log *.out *.toc pages/*.aux inc/*.aux inc/*.bbl inc/*.blg inc/*.log inc/*.out inc/*.toc *.synctex.gz
	echo "Clear:Ready"