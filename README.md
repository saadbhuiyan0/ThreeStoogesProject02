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

## APIs Implemented
- [REST Countries](doc/411_restcountries.pdf)
    - We used REST Countries to get data for each included nation.
    - The data we stored includes the nations' alpha-2 code, flag, capital, population, and land area.
- [LocationIQ](doc/411_locationiq.pdf)
    - LocationIQ provides us with the latitude and longitude for each nation's capital and center point.
    - We also used the API to generate maps with markers using the data we stored.
- [MetaWeather](doc/411_metaweather.pdf)
    - MetaWeather provides us with updated weather information for each nation's page.

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
- Then you can head over to your local server and start making wacky travel plans.
