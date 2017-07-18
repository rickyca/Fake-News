## Fake News

![alt text](https://raw.github.com/rickyca/Fake-News/master/images/wordclouds.png)

# Motivation 

Considering how social media affects our daily lives and how information is spread across it, some companies such as Facebook have been working on filtering ‘fake’ news. It is a difficult task, considering that people’s point of view should be taken into account when deciding which news sources are trustworthy or not. Different groups of people with different backgrounds and beliefs may disagree on what news are real or fake.

The goal of this project is to provide a model that can be trained according to a previous belief of what news are real or fake. I personally find it interesting when I read news from a different point of view, which focuses on different aspects of the same situation, disaster or event. 

# Data Collection 

The decision of what constitutes fake news was made by a web add-on called “B.S. Detector”. The data was obtain from kaggle.com. This dataset contains **only** fake news (according to the B.S. Detector) pulled from Webhose.io API by the end of 2016.

To obtain real news a few ‘trusted’ websites were selected. This was based on a study performed in 2014 aimed at understanding the nature and scope of political polarization in the American public:

“The American Trends Panel (ATP), created by the Pew Research Center, is a nationally representative panel of randomly selected U.S. adults living in households. Respondents who self-identify as internet users (representing 89% of U.S. adults) participate in the panel via monthly self-administered Web surveys, and those who do not use the internet participate via telephone or mail. The panel is being managed by Abt SRBI.

Data in this report are drawn from the first wave of the panel, conducted March 19-April 29, 2014 among 2,901 web respondents[...]”

# Repository organization

Each folder consists on a different part of the project.

 - Raw Data: Contains the original dataset from kaggle.com and the code used to pull 'real' news. This code was run on a Raspberry Pi, and pulled data periodically, every 5 hours, for over one month.
 - Parsing: Parses raw data into a .csv file matching information on the fake news dataset.
 - EDA: Some exploratory analysis was performed in order to understand what words or group or words are commonly used by the two news categories.
 - Modeling: Modeling was performed on Amazon Web Services (AWS). run_all.py was executed on an EC2 instance.
   - final_parse.ipynb joins the two datasets. 
   - model.py splits data into train/test, performs a grid search on the train data, using 3 folds. It test the model on the test data and saves the result in a .csv file.
   - options.py has the modeling options. Combinations of sklearn modeling objects and combination of parameters for the grid search
   - run_all.py runs all possible combination for the models and logs their success or failure.

Next image shows possible combinations for modeling
![alt text](https://raw.github.com/rickyca/Fake-News/master/images/model.png)
