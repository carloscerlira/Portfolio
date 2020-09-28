nBody = {
    'title': 'N-body problem',
    'software': 'OpenFrameworks | C++',
    'img': 'https://camo.githubusercontent.com/a281ebf883864098b2e770b2db2fdbecbd2c5f8d/68747470733a2f2f696d6775722e636f6d2f68576b486b30582e706e67',
    'icons': {
        "fab fa-github": 'https://github.com/carloscerlira/N-body-problem',
        "fas fa-file-pdf": 'https://github.com/carloscerlira/N-body-problem/blob/master/proyecto%20fisica%20computacional.pdf'
    }
}

nBody['content'] = """ 
The N-body is the problem about describing a system of particles interacting by a Newton like force,
by describing I mean knowing the position for every particle at each instant in time. A perfect example 
is a planetary system or even a galaxy. A naive numeric implementation for this problem has O(n^2) time complexity, 
this can be improved to O(nlogn) using the Barnes–Hut algorithm.
"""

nBody['projectChallenges'] = """ 
The main challenge for this project was understanding Barnes–Hut algorithm.
"""

nBody['mySolution'] = [
""" 
I was able to check correctnes of my solution by playing a coreography.
""",
"""
I was able to run at 30 fps a system of 50k particles.
"""]