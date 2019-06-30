# `OCR` application
## HU AAI IPASS 2019

**_De app_**<br>
Deze applicatie is een wrapper van 3 verschillende OCR libraries. Deze app maakt het mogelijk om zonder al te veel moeite op een **Windows PC**, met **Python 3.7** gebruik te maken van deze 3 OCR libraries zonder te veel kennis over OCR.

**_Systeem installatie_**
Om de applicatie werkend te krijgen op een Windows PC zult u de volgende stappen moeten uitvoeren. 
1. De **Git repo (https://github.com/Maerecque/IPASS)** moet gefetched of gepulled worden.

Voor de pip-commands die nodig zijn voor gebruik, zullen de volgende commando's gebruikt worden:
	`pip install pyocr`<br>
	`pip install numpy`<br>
	`pip install requests`<br>
	`pip install SequenceMatcher`<br>
	`pip install PyPDF2`<br>
	`pip install pytesseract`<br>
    (`pip install git+https://github.com/Maerecque/IPASS.git)

2. Voor het werken van de OCR engine zult u een OCR geïnstalleerd moeten hebben, voor de testfase van deze app is de volgende OCR engine geïnstalleerd op de PC: **https://github.com/UB-Mannheim/tesseract/wiki**. Het is belangrijk dat u de OCR engine in de volgende map plaats 'C:\Program Files\', anders zal het script niet bij de OCR engine kunnen komen. 

