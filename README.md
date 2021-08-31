## Telco Churn Classification Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Project Summary
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

#### Project Objectives
> - Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.
> - Create modules (acquire.py, prepare.py) that make your process repeateable.
> - Construct a model to predict customer churn using classification techniques.
> - Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your target audience.
> - Answer panel questions about your code, process, findings and key takeaways, and model.

#### Business Goals
> - The project and goal is to find and document drivers for customer churn at Telco and to construct a machine learning classification model that accurately predicts customer churn.
> - Document your process well enough to be presented or read like a report.

#### Audience
> - Codeup Data Science students

#### Project Deliverables
> - A final report notebook 
> - A final report notebook presentation
> - All necessary modules to make my project reproducible

#### Project Context
> - The telco churn dataset I'm using came from the Codeup database.


#### Data Dictionary

| Feature                    | Datatype               | Description                                                           |
|:---------------------------|:-----------------------|:----------------------------------------------------------------------|
| customer_id                | 7043 non-null: object  | Identification number for customer                 |
| gender                     | 7043 non-null: object  | Customer gender, male or female                    |
| senior_citizen             | 7043 non-null: int64   | Yes or No, is the customer a senior citizen        |
| partner                    | 7043 non-null: object  | Yes or No, does the customer customer has a parter |
| dependents                 | 7043 non-null: object  | Number of dependents a customer has                |
| tenure                     | 7043 non-null: int64   | Months a customer has been with the company        |
| phone_service              | 7043 non-null: object  | Phone Service plan, Yes or No                      |
| multiple_lines             | 7043 non-null: object  | Multiple lines, Yes or No                          |
| internet_service_type_id   | 7043 non-null: int64   | 1, 2, 3                                            |
| online_security            | 7043 non-null: object  | Yes, no, or no internet service                    |
| online_backup              | 7043 non-null: object  | Yes, no, or no internet service                    |
| device_protection          | 7043 non-null: object  | Yes, no, or no internet service                    |
| tech_support               | 7043 non-null: object  | Yes, no, or no internet service                    |
| streaming_tv               | 7043 non-null: object  | Yes, no, or no internet service                    |
| streaming_movies           | 7043 non-null: object  | Yes, no, or no internet service                    |
| contract_type_id           | 7043 non-null: int64   | 1, 2, 3                                            |
| paperless_billing          | 7043 non-null: object  | Yes or no, customer uses paperless billing         |
| payment_type_id            | 7043 non-null: int64   | 1, 2, 3, 4                                         |
| monthly_charges            | 7043 non-null: float64 | Monthly charges the customer pays                  |
| total_charges              | 7043 non-null: object  | Total charges the customer has paid                |
| churn                      | 7043 non-null: object  | Yes or no, whether or not the customer has churned |
| contract_type_id.1         | 7043 non-null: int64   | 1, 2, 3                                            |
| contract_type              | 7043 non-null: object  | Month-to-month, One year, Two year                 |
| internet_service_type_id.1 | 7043 non-null: int64   | 1, 2, 3                                            |
| internet_service_type      | 7043 non-null: object  | DSL, Fiber Optic, or None                          |
| payment_type_id.1          | 7043 non-null: int64   | 1, 2, 3, 4                                         |
| payment_type               | 7043 non-null: object  | E-check, mailed check, bank transfer, credit card  |


#### Initial Hypotheses

> - **Hypothesis 1 -**
> - alpha = .05
> - $H_0$: Churned customers average total charges is less than or equal to average total charges not churned customers.  
> - $H_a$: Churned customers average total charges is greather than average total charges for not churned customers 
> - Outcome: I failed to rejected the Null Hypothesis; Churned customers average total charges is LESS than or equal to average total charges not churned customers.

> - **Hypothesis 2 -** 
> - alpha = .05
> - $H_0$: Customers who churn average tenure greater than or equal the average tenure of those who do not churn.  
> - $H_a$: Customers who churn average tenure less than the average tenure of those who do not churn. 
> - Outcome: I rejected the Null Hypothesis; Customers who churn average tenure IS less than the average tenure of those who do not churn.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary - Conclusions & Next Steps
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> - My random forest classifier model accuracy was 80%, beating my baseline accuracy of 73%.

> - My model identified the most important features as Month-to-month, tenure, total_charges, and fiber in that order.

> - If I had more time, I would have liked to try a lot more combinations of features. I would have also liked to iterate through hyperparameters to boost accuracy.

> - The data suggests signing up new customers and current customers into a longer contract other than month-to-month and not suggesting fiber as an internet speed would lower the churn rate.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

##### Plan
> - Create a new repository, update the .gitignore, create a README.md with the data dictionary, project and business goals, and come up with initial hypotheses.

> - Explore the SQL Codeup database. Create a SQL script to select all the features and observations. Create a function in python called get_telco_data() that uses the previously defined SQL script to pull the data from the Codeup database then save the new file as acquire.py.

> - Create a function and name it clean_telco(). This function will drop any useless features, remove duplicates, double check data-types, find any null values, decide what do with null values, and encode the features using pd.get_dummies(). This clean data function will be saved on a new file called prepare.py

> - On the same prepare file, create split_telco_data(). This function will split the cleaned data into three data sets named train, validate, and test. Lastly, create prep_telco_data() that will call clean_telco() and split_telco_data(). It will return the three data sets train, validate, and test.

> - In the explore phase, I plan on running the predefined explore_univariate(), explore_bivariate(), and explore_multivariate() by importing the explore.py file. I plan on looking through the graphs and evaluate each feature to see if they play a part in churn. Exploration will also include two hypotheses, setting of alpha, statistical tests, rejecting or failing to reject the null hypothesis, and documentation of the findings and takeaways.

> - Once exploration is complete and I have defined which features I plan on using I will then create three machine learning models plus my baseline model. I will establish a baseline accuracy and document well. For my machine learning models, I will be using a DecisionTreeClassifier, RandomForestClassifier, and KNeighborsClassifier. After I MAKE the models I will FIT the models and then I will USE the models. I will use the accuracy of the train and validate data to determine if the difference is within my predefined threshold. Once I have filtered out the models that have passed, I can then pick the model with highest validate accuracy to run on my final test data.

> - Create csv file with the measurement id, the probability of the target values, and the model's prediction for each observation in my test dataset.

> - Lastly, I will document conclusions, recommendations, and takeaways in the final report notebook.
___

##### Plan -> Acquire
> - Store functions that are needed to acquire data from the telco churn database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
> - The final function will return a pandas DataFrame.
> - Import the acquire function from the acquire.py module
> - Complete some initial data summarization (`.info()`, `.describe()`, `.value_counts()`, ...).
> - Plot distributions of individual variables.
___

##### Plan -> Acquire -> Prepare
> - Store functions needed to prepare the iris data; make sure the module contains the necessary imports to run the code. The final function should do the following:
    - Split the data into train/validate/test.
    - Handle any missing values.
    - Handle erroneous data and/or outliers that need addressing.
    - Encode variables as needed.
    - Create any new features, if made for this project.
> - Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.
___

##### Plan -> Acquire -> Prepare -> Explore
> - Answer key questions, my hypotheses, and figure out the features that can be used in a classification model to best predict the target variable, species. 
> - Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
> - Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). The goal is to identify features that are related to species (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
> - Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model
> - Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
> - Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
> - Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
> - Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
> - Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver
> - Introduce myself and my project goals at the very beginning of my notebook walkthrough.
> - Summarize my findings at the beginning like I would for an Executive Summary.
> - Walk Codeup Data Science Team through the analysis I did to answer my questions and that lead to my findings.
> - Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [ ] Download the aquire.py, prepare.py, explore.py, and final.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the final_report.ipynb notebook