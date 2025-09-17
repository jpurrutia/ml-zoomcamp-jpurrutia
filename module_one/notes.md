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

