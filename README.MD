This functionality's created for Avito Service scrapping.

Libraries used:
    PySide6
    lxml
    beautifulsoup4
    fake-useragent
    aiohttp[speedups]
    selenium
    selenium-stealth
    xmltodict
    openpyxl
    pandas
    python-rucaptcha
    2captcha-python

So, as you see, this scrapping script's provided with PySide simple interface.
Main library that used for scrapping is Selenium, also i used aiohttp to collect cities and regions.
Usage of Selenium ain't random or prefered to use, this is the only way to make scrapping because of
http requests blocked state at the beginning of script working.

To use this you need to:
    1. Activate virtualvenv:
        Linux - "source project/project_venv/bin/activate"
        Windows - "project/project_venv/Scripts/activate"

        Note: To deactivate - write "deactivate"
    
    2. Install requirements.txt
        pip install -r project/requirements.txt

    3. Set executable path to any browser driver .exe file
        Example:
            "C:\\Users\\user\\Desktop\\AvitoParser\\project\\ParserScripts\\Drivers\\firefox\\geckodriver.exe"

    4. Run "python project/main.py" file

        Note: use "python3" instead if you treat with python2 and python3 installed on your system

This work is free to use, so have fun :)
