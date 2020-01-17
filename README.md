# Wack Travel Plans by Three Stooges

## Roster
* Saad Bhuiyan -- Project Manager & Database
* Benjamin Avrahami -- Frontend
* Hannah Fried -- Backend

## What is Wack Travel Plans?
Wack Travel Plans is your premier site for all things travel related. 
Make an account to find nations to travel to, our site will provide you with all the information you need.
You will find a ton of useful data from land area to population.
We'll recommend places to go in the capital too!
We even give our own fun little rating.
Before you even think about your next vacation, just browse the site for a few minutes! 
You can thank us later.

## [Video Demo](https://youtu.be/2EFh2xcgY8w)
YouTube link for demo as a video.

## APIs Implemented
- [REST Countries](https://docs.google.com/document/d/1aQRi7FIILs_x3RE5i65KHuuy49Rt05ZqERKqZjOGiJw/edit)
    - We used REST Countries to get data for each included nation.
    - The data we stored includes the nations' alpha-2 code, flag, capital, population, and land area.
    - This data is used in multiple pages on our website.
- [LocationIQ](https://docs.google.com/document/d/1i6Zl1cfnEr_u9oqvk1XbwJWGMqf8Vp2IdQzUf2InGek/edit)
    - LocationIQ provides us with the latitude and longitude for each nation's capital and center point.
    - We also used the API to generate maps with markers using the data we stored.
- [MetaWeather](https://docs.google.com/document/d/18uyXB5XPFQoGFJpoa2yQvRPhevc3HaBU4kO-OYN-ieY/edit#heading=h.3zf63kd5qt0p)
    - MetaWeather provides us with updated weather information for each nation's page.
    - We use it to get weather for the capital city of the nation by latitude and longitude search.

## Launch Codes
- First you will want to open Git Bash.
- Go to the directory where you would like to clone the project.
- Then clone the project from [here](https://github.com/saadbhuiyan0/ThreeStoogesProject02).
- Next you will need to generate a key for the [LocationIQ API](doc/411_locationiq.pdf).
    - Start by signing up on their [website](https://locationiq.com/register).
    - After you register, it will take you to your dashboard where you will see a token field - that is your API key.
- In your terminal - within the ThreeStoogesProject02 directory - run: `python3 -m venv hero`
- Then: `. hero/Scripts/activate`
- Then: `pip3 install -r doc/requirements.txt`
- Then: `python3 app.py` to run the app.
- If it is your first time running the app, api_key.txt will be empty so the terminal will prompt you to input the API key you generated for LocationIQ.
    - Paste your API key, and hit enter. This should save the API key in api_key.txt.
- If you do not have a populated database in the directory, the database will take a substantial amount of time (over 2 minutes) to populate the database with the data from the APIs. This is due to the 2 API calls per second limit imposed by LocationIQ's free plan. After the database is populated, the launch time should reduce drastically (<5 seconds).
- Then you can finally head over to your local server and start making wack travel plans.
