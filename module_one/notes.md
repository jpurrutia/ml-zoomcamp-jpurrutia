# Module 1


### Intro to Machine Learning
- Predicting the price of a car:

```
features = ["mileage", "make", "model", "year"]
target = "price"
X = df[features]
y = df[target]
```

### Machine Learning vs Rule-Based Systems

- A rule-based system for spam detecion
- using ML for spam detection
- Extracting features for ML

#### Email System


send and receive emails
spam or fraudulent emails

Rules
- if send = promotions@online.com then "spam"
- if title contains "tax review" and sender domain is "online.com" then "spam" otherwise, "good email"



Use machine learning to learn the rules from data
- get data
- define and calculate features
- train and use a model

data ----------------------> 
outcome (spam/not spam) -> ML -> Model 

Data + Model -> Prediction (spam/not spam)


### Supervised Machine learning

what is supervised machine learning?

Examples
- regression
- classification
- ranking


Feature (data) -> Target (outcome)
            (deposit)
[1, 1, 0, 0, 1, 1]
[0, 0, 1, 1, 0, 0]
[0, 1, 0, 1, 0, 1] 

Feature matrix (X)

Target vector (y)

function   g   ( X ) = y
        model features   target


Types of Supervised Machine Learning
- Regression - g function is predicting a value (car price)
- Classification - g function is predicting a class (spam/not spam) (binary)
- Multiclass classification - g function is predicting one of several classes (cat, dog, mouse)
- Ranking - g function is predicting a rank (search results - ranking a list of items I would want to buy)

### CRISP-DM
cross industry standard process for data mining - how ML projects should be organized


1. Business understanding - define a measurable goal. Ask: do we need ML?
2. Data understanding - do we have the data? is it good?
3. Data preparation - transform data into a table, so we can put it into ML
4. Modeling - to select the best model, use the valiation set
5. Evaluation - validate that the goal is reached
6. Deployment - roll out to production to all the users

#### Spam Detection Example

Business understanding
- is the spam detection system important for the business?
- do we need ML

Identify Data Sources
- we have a report spam button
- is the data behind this button good enough?
- it it reliable?
- do we track it correctly?
- is the dataset large enough?
- do we need tog et more data?

Data Preparation
- clean the data
- build the pipelines
- convert into tabular form
X, y

Modeling
- Which model to choose?
    - Logit
    - Decision tree
    - neural network
    - or many others

Evaulation
Is the model good enough?
    - Have we reached the goal?
    - Do our metrics improve? 

Goal: reduce the amount of spam by 50%

- Have we reduced it? By how much?
- (Evaluate on the test group)


Evaluation + Deployment
- online evaluation: evaluation of live users
- it means: deploy the model, evaluate it

Deployment
- Roll the model to all users
- proper monitoring
- ensuring quality and maintainability


Iterate!
Start simple learn from feedback

### Modeling - Model Selection Process

Selecting the best model

80% Train
20% Test or Validation

yhat = g(X)
prediction v target variable to measure performance

Multiple comparisons problem 
- use many models and validate on the same validation set
- if we try many models, we will find one that works well on the validation set by chance
- we need to have a test set that is not used during model selection

Validation & Test
60 % - train
20% - validation 
20% - test - hide this before model selection

### model selection process
1. Split the dataset
2. Train many models on the training set
3. Evaluate on the validation set - record accuracy
(2 and 3) many times
4. Select the best model based on validation accuracy
5. Apply the best model on the test set - report test accuracy
6. Check if test accuracy is close to validation accuracy - if not, we overfit the validation set

.