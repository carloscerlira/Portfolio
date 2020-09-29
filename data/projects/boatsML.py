boatsML = {
    'title': 'Boat detection using a CNN',
    'software': 'Kaggle | Pandas | Scikit Learn | PyTorch ',
    'img': 'https://raw.githubusercontent.com/carloscerlira/Boat-detection-CNN/master/dataset/scenes/sf_1.png',
    'icons': {
        "fab fa-github": 'https://github.com/carloscerlira/Boat-detection-CNN/tree/master/dataset',
        "fa fa-google": None
    }
}

boatsML['content'] = """ 
Planet is a US company that delivers daily satellite images from California.
Due to the high amout of data that is generated each day computer vision 
algorithms are used to automate the analysis task. For this project I used a 
Convulutional Neural Network to identify boats using over 40,000 images from 
California Bay Area. The dataset was created using Planet's API by kaggle 
user Bob Hammell.   
"""

boatsML['projectChallenges'] = [
""" 
Selecting a CNN arquitecture.
""",
"""
Selecting metrics for model.
"""
]
boatsML['mySolution'] = [
""" 
I used LeNet-5 arquitecture because of the small dataset.
""",
""" 
I added dropout as it proved to prevent overfitting in the test fase.
""",
""" 
For metrics I used acuarracy on validation data and confusion matrix as I noticed at the start my 
model acuarracy was high, but the amount of false positive cases was high too.
"""
]