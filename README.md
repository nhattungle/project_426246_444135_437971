# Run scrapers:
Please read description.pdf to understand this project, as well as the tools we used to practice.

## Summary of steps required for experimentation:

### With BeautifulSoup:
+ Step 1: Download all the code in the soup folder
+ Step 2: Install related libraries:
          
          - pip install beautifulsoup4            https://pypi.org/project/beautifulsoup4/
          - pip install urllib3                   https://pypi.org/project/urllib3/
          - pip install pandas                    https://pypi.org/project/pandas/

+ Step 3: Run python code
          
          python .\ScrapingWithBeautifulSoup.py
          
+ Step 4: Using SQLiteStudio to check the scraped data on the table product_beautifulsoup
          
## With Selenium:

+ Step 1: Download all the code in the selenium folder
+ Step 2: Install related libraries:
          
          - pip install boto                      https://pypi.org/project/boto/
          - pip install selenium                  https://pypi.org/project/selenium/

+ Step 3: Run python code
          
          python .\ScrapingWithSelenium.py
          
+ Step 4: Using SQLiteStudio to check the scraped data on the table product_selenium

## With Scrapy:


+ Step 1: Download all the code in the scrapy folder
+ Step 2: Preparing the Splash server

          INSTALL DOCKER & LINUX WSL
                    Install Docker Desktop: https://docs.docker.com/desktop/windows/install/
                    Linux-kernel: https://docs.microsoft.com/en-us/windows/wsl/install-manual
                    Install linux: user: wne, password: 123456
                    Rundocker: & "C:\Program Files\Docker\Docker\DockerCli.exe" -SwitchDaemon
          
          INSTALL AND RUN SCRAPY-SPLASH DOCKER (https://github.com/scrapy-plugins/scrapy-splash)
                    pip install scrapy-splash
                    docker pull scrapinghub/splash
                    docker run -p 8050:8050 scrapinghub/splash
          
+ Step 3: Configuration for the Scrappy project (settings.py):

                    SPLASH_URL = 'http://localhost:8050/'
                    DOWNLOADER_MIDDLEWARES = { 
                        'scrapy_splash.SplashCookiesMiddleware': 723, 
                        'scrapy_splash.SplashMiddleware': 725, 
                        'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810, 
                    }

+ Step 4: Install related libraries:
          
          - pip install scrapy                      https://pypi.org/project/Scrapy/
          - pip install scrapy-splash               https://pypi.org/project/scrapy-splash/

+ Step 5: Run stage by stage
          
          scrapy crawl link_page -o link_pages.csv
          scrapy crawl link_product -o link_products.csv
          scrapy crawl product_detail -o product_details.csv
          
+ Step 6: Transfer data from CSV to Database

          python .\ScrapingWithScrapy.py     

+ Step 7: Using SQLiteStudio to check the scraped data on the table product_scrapy

