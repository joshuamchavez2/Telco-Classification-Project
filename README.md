
Plan
Step 1
     Create a new repository, update the .gitignore, create a README.md with the data dictionary, project and business goals, and come up with initial hypotheses.

Step 2
     Explore the SQL Codeup database. Create a SQL script to select all the features and observations. Create a function in python called get_telco_data() that uses the previously defined SQL script to pull the data from the Codeup database then save the new file as acquire.py.

Step 3
     Create a function and name it clean_telco(). This function will drop any useless features, remove duplicates, double check data-types, find any null values, decide what do with null values, and encode the features using pd.get_dummies(). This clean data function will be saved on a new file called prepare.py

Step 4
     On the same prepare file, create split_telco_data(). This function will split the cleaned data into three data sets named train, validate, and test. Lastly, create prep_telco_data() that will call clean_telco() and split_telco_data(). It will return the three data sets train, validate, and test.

Step 5
     In the explore phase, I plan on running the predefined explore_univariate(), explore_bivariate(), and explore_multivariate() by importing the explore.py file. I plan on looking through the graphs and evaluate each feature to see if they play a part in churn. Exploration will also include two hypotheses, setting of alpha, statistical tests, rejecting or failing to reject the null hypothesis, and documentation of the findings and takeaways.

Step 6
     Once exploration is complete and I have defined which features I plan on using I will then create three machine learning models plus my baseline model. I will establish a baseline accuracy and document well. For my machine learning models, I will be using a DecisionTreeClassifier, RandomForestClassifier, and KNeighborsClassifier. After I MAKE the models I will FIT the models and then I will USE the models. I will use the accuracy of the train and validate data to determine if the difference is within my predefined threshold. Once I have filtered out the models that have passed, I can then pick the model with highest validate accuracy to run on my final test data.

Step 7
     Create csv file with the measurement id, the probability of the target values, and the model's prediction for each observation in my test dataset.

Step 8
     Lastly, I will document conclusions, recommendations, and takeaways in the final report notebook.

Summarize your findings at the beginning like you would for an Executive Summary. Just because you don't have a slide deck for this presentation, doesn't mean you throw out everything you learned from Storytelling.

Walk us through the analysis you did to answer our questions and that lead to your findings. Relationships should be visualized and takeaways documented. Please clearly call out the questions and answers you are analyzing as well as offer insights and recommendations based on your findings.

For example: If you find that month-to-month customers churn more, we won't be surprised, but Telco is not getting rid of that plan. The fact that customers churn is not because they can; it's because they can and they are motivated to do so. We want your insights into why they are motivated to do so. We realize you will not be able to do a full causal experiment, but we would like to see some solid evidence of your conclusions.

Finish with key takeaways, recommendations, and next steps and be prepared to answer questions from the data science team about your project.

Remember you have a time limit of 5 minutes for your presentation. Make sure you practice your notebook walkthrough keeping this time limit in mind; it will go by very quickly.