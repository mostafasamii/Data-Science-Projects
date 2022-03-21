# Predicting-a-Startup-s-Acquisition-Status
**The goal of this project is to predict a former startup’s acquisition status based on a company’s financial statistics.**

# Abstract:
Start-ups are companies that make items that wander to an zone or showcase in ways that haven’t been done some time recently. This makes start-ups unsafe and unusual as a modern item or benefit may not work among its clear clients and may require consistent alterations some time recently it gets product/market fit. Eventually, a start-up could be a high-risk company that's within the to begin with arrange of operations and commonly related to innovation as a item or a benefit.
Startups are important and the motor for the economy of the countries. Over the past decade, many countries have seen an exponential growth in start-up arrangements. In this way, it appears a significant challenge understanding what makes this type of high-risk wanders effective and as such, appealing to financial specialists and business visionaries. 
Success for a start-up is characterized here as the occasion that gives a expansive whole of cash to the company’s founders, speculators and early representatives. The capacity to foresee victory is an invaluable competitive advantage for venture capitals on the rummage around for ventures since first-rate targets are those who have the potential for developing quickly before long, which eventually, permits financial specialists to be one step ahead of competition.

# Objectives:
The present work has as the main objective, the development of a predictive model to classify a startup whether it is (Operating, IPO, Acquired, or closed). The most important step to get into startip's acquisitions is knowing its financial statistics such as total funding dollars, funding dates, number of funding rounds and headquarter locations, also the IPO is an important feature to consider.
An Initial Public Offering **(IPO)** refers to the process of offering shares of a private corporation to the public in a new stock issuance.

Previous studies tend to center primarily on administrative highlights and regularly outline the affect of monetary highlights related with funding (specially from Wander Capital reserves). It is planning to bridge this crevice by making funding-oriented features with great prescient affect in classifying effective companies. Also, there's room to make strides the quality of the test by being more particular with companies or by way better treating the sum of meager information which is characteristic of this dataset.

# Dataset:
* The dataset used for this project is a kaggle dataset sourced from Crunchbase called: “Crunchbase 2013- Companies, Investors, etc.”
* There are nearly 196553 rows and 15 columns, each row of the dataset contains a startup’s 	information.
* The dataset labels show that the dataset is extremely biased. 
As shown in the table below. With the “Operating” class is over-presented.
--insert the image here--

#### **Original Features**
- category_code
- status 
- founded_at 
- closed_at
- country_code
- funding_rounds
- funding_total_usd
- first_milestone_at
- last_milestone_at
- milestones
- relationships
- lat
- lng

#### **Generated Features**
- Active days
- Milestones advancement ratio

#### **Removed Features**
- ROI 
- first_investment_at 
- investment_rounds 
- last_investment_at
- first_funding_at
- last_funding_at
- created_by
- state_code
- created_at
- updated_at
- city
- region
- id 
- invested_companies
- Unnamed: 0.1
- entity_type
- entity_id
- parent_id
- name
- normalized_name
- permalink
- domain
- homepage_url
- twitter_username
- logo_url
- logo_widthlogo_height
- short_description
- description
- overview
- tag_list

# Data Cleaning:
The first step in data cleaning was to remove the irrelevant and redundant information from the Crunchbase dataset. As the dataset has several columns and instances that doesn't match the purpose of prediction the success of the startup.
*Steps:*
* Dropping unnecessary columns.
* Removing duplicates.
* Removing rows from dataset that their founded_at date comes after closed_at date
* Applying some data imputation, its better to do imputation rather than dropping the rows or columns. But with columns have NaN values more than 80% of NaN it's better to drop the column
* Removing outliers from two of the numerical columns(funding_rounds, and funding_total_usd)
* Creating features:
  * Active days column: which is how many days the company has been running, so we subtract the founded_at date from the closed_at date.
  * advance ratio in milestones: which is the rate of advancement the company makes.

# EDA:
Exploratory Data Analysis (EDA) is an approach/philosophy for data analysis that employs a variety of techniques (mostly graphical) to maximize insight into a dataset, extract important insights, and uncover underlying structure.
For the EDA there is three questions we want to answer:
* Research Question 1: How many startups was funded over the years? and which year has the most funded number of startups?
* Research Question 2: What is the number of startups in every country?
* Research Question 3: Which startup's category advances faster?

# Feature Engineering:
The goal of feature engineering is simply to make your data better suited to the problem at hand.
You might perform feature engineering to:
* improve a model's predictive performance
* reduce computational or data needs
* improve interpretability of the results

What is done on the dataset so far:
- Applying Log transform on (funding_total_usd, and milestone_adv_ratio)
- One Hot Encoding for the categorical features
- Standard Scaler for the numerical features 

# Modeling:
#### Random Forest
Random Forest model is an ensemble learning methods for classifcation and regression tasks that operates by constructing a multitude of decision trees at training time. For classification tasks that we are performing in this project, the output of the random forest is the class selected by most trees.
#### XGboost
XGBoost is a decision-tree-based ensemble Machine Learning algorithm that uses a gradient boosting framework, also it is the leading model for working with standard tabular data.

# Ensembling:
The goal of ensemble methods is to combine the predictions of several base estimators built with a given learning algorithm in order to improve generalizability / robustness over a single estimator.

On this project we used **VotingClassifier**. The idea behind the VotingClassifier is to combine conceptually different machine learning classifiers and use a majority vote or the average predicted probabilities (soft vote) to predict the class labels. Such a classifier can be useful for a set of equally well performing model in order to balance out their individual weaknesses.

# Model Evaluation:
Model Evaluation is an integral part of the model development process. It helps to find the best model that represents our data and how well the chosen model will work in the future.

**Confusion Matrix**
A confusion matrix is a correlation between the predictions of a model and the actual class labels of the data points.

# Deployment
Heroku is a cloud platform as a service (PaaS) supporting several programming languages. One of the first cloud platforms. Also it lets companies build, deliver, monitor and scale apps in a fast way to go from idea to URL, by passing all those infrastructure headaches.
