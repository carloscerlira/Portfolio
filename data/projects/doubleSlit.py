doubleSlit = {
    'title': 'Numeric solution to Schrödinger equation, simulation for double slit experiment',
    'software': 'OpenFrameworks | C++ ',
    'img': 'https://camo.githubusercontent.com/ff4d8239d6c9c51825cd08049d0ad6d47ab85e2c/68747470733a2f2f696d6775722e636f6d2f436b75794643632e706e67',
    'icons': {
        "fab fa-github": 'https://github.com/carloscerlira/Schrodinger-equation-numerical-solution',
        "fas fa-file-pdf": 'https://github.com/carloscerlira/Schrodinger-equation-numerical-solution/blob/master/paper.pdf'
    }
}

doubleSlit['content'] = """ 
The Schrödinger equation describes the way particles such as electrons interact with the 
world. The double slit experiment, one of the most beautiful and famous experiments in all physics.
Turns out there is not an analytical solution for this experiment, so I decided to 
solve it numerically.  
"""

doubleSlit['projectChallenges'] = """ 
Find right algorithm to solve Schrödinger equation, naive implementation proves to be too slow.
"""

doubleSlit['mySolution'] = """ 
After doing a lot of research and with the help of people at physics exchange I figure out how RK4 can be applied to the problem.
"""