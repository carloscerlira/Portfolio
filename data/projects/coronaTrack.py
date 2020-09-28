coronaTrack = {
    'title': 'COVID-19 Tracker',
    'software': 'Heroku | Flask | GitHub | HighCharts | Pandas',
    'img': 'https://raw.githubusercontent.com/carloscerlira/CoronaTrack/master/about/img/home.png',
    'icons': {
        "fas fa-globe": "https://world-covid-tracker.herokuapp.com/",
        'fab fa-github': 'https://github.com/carloscerlira/CoronaTrack'
    }
}

coronaTrack['content'] = """ 
Daily stats, graphs and general informaiton about COVID-19 for more than 150 
countries. Data comes from custom API and is updated daily by server.
"""

coronaTrack['projectChallenges'] = """
Create custom API, data has to be updated daily and comes 
from different sources.
"""

coronaTrack['mySolution'] = [
""" 
I primarily used Johns Hopkins University COVID-19 data, for countries
where I wanted to use a different source like Mexico (because I wanted updates right after publication), 
I had to transform to a similar format. 
""",
""" 
I used pandas to fetch and manipulate the data to generate custom metrics. 
""",
""" 
I used a GitHub repository as my API, updated daily by heroku server using pyGithub. 
"""
]