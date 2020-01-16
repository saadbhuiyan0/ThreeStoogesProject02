# Wack Travel Plans by Three Stooges

## Roster
* Saad Bhuiyan -- Project Manager & Database
* Benjamin Avrahami -- Frontend
* Hannah Fried -- Backend

## What is Wack Travel Plans?
Wack Travel Plans is your premier site for all things travel related. 
Make an account to find nations to travel to, our site will provide you with all the information you need.
You will find a ton of data from weather to population.
We even give our own little rating.
Before you even think about your next vacation, just browse the site for a few minutes! 
You can thank us later.

## APIs Implemented
- [REST Countries](doc/411_restcountries.pdf)
- [LocationIQ](doc/411_locationiq.pdf)
- [MetaWeather](doc/411_metaweather.pdf)
- [Wikipedia](doc/411_wikipedia.pdf)

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
