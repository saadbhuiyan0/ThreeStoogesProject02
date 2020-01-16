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

## [Video Demo](https://www.youtube.com/watch?v=Iwuy4hHO3YQ)
Link to be updated by 08:00 EST Friday, January 17th, 2020.

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
- Clone the project from [here](https://github.com/saadbhuiyan0/ThreeStoogesProject02).
- Next you will need to generate a key for the [LocationIQ API](doc/411_locationiq.pdf).
    - Start by signing up on their [website](https://locationiq.com/register).
    - After you register, it will take you to your dashboard where you will see a token field - that is your API key.
    - Save the API key in a txt file named `api_key.txt` in the ThreeStoogesProject02 directory.
- In your terminal - within the ThreeStoogesProject02 directory - run: `virtualenv venv`
- Then: `source venv/bin/activate`
- Then: `pip install -r doc/requirements.txt`
- Then: `python3 app.py` to run the app.
- The first time you run the app, the database will take a substantial amount of time (over 2 minutes) to populate with the data from the APIs. This is due to the 2 API calls per second limit imposed by LocationIQ's free plan. After the database is populated once, the launch time should reduce drastically (<5 seconds).
- Finally you can head over to your local server and start making wack travel plans.
