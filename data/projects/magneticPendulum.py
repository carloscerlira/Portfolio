magneticPendulum = {
    'title': 'Magnetic Pendulum',
    'software': 'CUDA | OpenFrameworks | C++',
    'img': 'https://camo.githubusercontent.com/3589cf8d248acb6e42e2c842d0d3e941d2284713/68747470733a2f2f696d6775722e636f6d2f63524a49384b792e706e67',
    'icons': {
        'fab fa-github': 'https://github.com/carloscerlira/Magnetic-Pendulum',
        'fas fa-file-pdf': 'https://github.com/carloscerlira/Magnetic-Pendulum/blob/master/poster.pdf'
    }
}

magneticPendulum['content'] = """ 
A Magnetic Pendulum is just like a normal pendulum at whose end there is a magnet, 
if we put three magents below it in a triangle shape, we got ourselfs a cahotic system. 
Take a random point in the grid and release the pendulum from there, the final state can not be determinated,
even the slightest change to the initial conditions have a dramatic impact in the final state. 
Because a differential equation needs to be solved for every point in 
a grid, I decided to use CUDA to paralelize this task. 
"""

magneticPendulum['projectChallenges'] = """
Understand CUDA arquitecture. 
"""

magneticPendulum['mySolution'] = """
I went through the examples given by NVIDIA and was able to 
find one close to what I needed.
"""