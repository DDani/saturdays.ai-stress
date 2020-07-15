# Saturdays.ai Team Stress Detection.

The following repository contains the final project part of Saturdays.AI (https://www.saturdays.ai/) build with other three alumni.

The contribuitors of this project are:

* [Jose Antonio Vives](https://www.linkedin.com/in/jose-antonio-vives-gonzalez-83724a6a/)
* [Dani Castro Garcia](https://www.linkedin.com/in/castrodani/)
* [Francisco Arenas Afán de Rivera](https://www.linkedin.com/in/fran-arenas-afán)



# Introduction

Happyforce (www.myhappyforce.com) is a Employee Engagement platform used by companies to measure the level of engagement of their employees, allowing managers and teams to improve in order to improve, motivate and retain talent.

Unlike a climate survey (which is usually annual), Happyforce carries out a continuous measurements of different employee engagement dimensions (https://en.wikipedia.org/wiki/Employee_engagement) via pulse surveys and a daily check-in question.

![Happyforce](img/hf-app.png?raw=true)


This provides and unvaluable dataset for research correlation and predictions based on previous gathered data.

Inside all dimensions measured by Happyforce, there is one that is a perfect match for the values that we must chase on a Saturday.ai project: a social aspect. 

![Happyforce](img/indicadores-happyforce.png?raw=true)

This dimension is **Employee Stress**.

### Challenge and objective:

Stress has been described as the health epidemic of the 21th century.

![Imagen 1](img/stress-img.png?raw=true)

Being the workplace as one of the biggest source of stress:

![Imagen 2](img/workplace-stress.jpg?raw=true)


**With this project we will try to determine which variables mainly affect to employee's stress**, and we will try to build a model for predicting when an employee will suffer stress on the following months.


# The Dataset:

The dataset is composed by two files, and can be found in the /data directory on this repository.

This first file, `scores.csv`, contains all the answers to the different questions of the different dimensions measured by Happyforce (more info about the dimensions here: https://myhappyforce.com/en/measure/). The number of votes recorded is 103.330, the number of participants (employees) is 6419, while the number of companies on the file is 72. On this file, we can find what it will become our target variable: stress.

Also, a second file is provided: `hi.csv`. This file contains the votes to the daily question "How are you today?" of the employees that have participated on any of the scores.csv. file. This file contains the 847.935 entries.

_PD: A first cleanup, shows that there are duplicates on each file, due the export procedure performed by Happyforce. The numbers exposed above are after droping the duplicates._


# The Definitions:

The Happyforce stress question is formulated on a scale between 1 and 10, where 1 is high stressed and 10 is low stressed. 

Knowing that, the first decision we took is to define what is an stressed employee. Based on the answers to the question:

**"On a scale from 1 to 10, how would you rate the work-related stress?"**

![Happyforce](img/stress_votes_distribution.png?raw=true)

We divided the scale in three as:

 - 1-3 stressed
 - 4-6 neutral
 - 7-10 not stressed.
 
By setting the threshold below 3 (included), a 50.3% of the employees have expressed at some point that they felt stressed, which gives us a balanced dataset.


# The Approach:

### EDA (Exploratory Data Analysis)

Any DS project starts with data exploration, in order to find patterns and prepare the data for ML tasks. 

This has been the most extensive phase of the project and one of the most critical as analyzing the data in one way or another 
can dramatically change the strategy for applying the models to our data.

The first phase, was to check the structure of the two provided files.

![Happyforce](img/hf-score-questions.png?raw=true)

In the `scores` dataset each record represents an employee's answer to a given question. For each record we found enough variables to identify the company, the sector to which the company belongs, the id of the question, the id of the factor to which the question is associated and the date on which the question is answered, in addition to the score answer of the employee (from 1 to 10).

The `hi` dataset contains the answers to the Happyness Index. Each record represents one vote of an employee on a given date. The values of the HI range from 1 to 4, with 4 being the most positive rating.

### Data preparation

Both datasets are date based, and our objective was to be able to give a prediction on if a employee will suffer stress.

For that to happen we needed to build a new dataset where we have all the information related to all other variables prior to the date where an employee answer to the stress question.

That means (as an example):
 * If an employee voted x on the stress question on May... how was his/her Happiness Index 3 months ago?
 * If an employee voted x on the stress question on May... what she/he voted on any other pulse question 6 months ago? 

So, we crunched the data by building a function for generate that new dataset. As result we got a Dataframe with:

For each employee, that vote to the stress question on X:

* For each question on the scores file, what she/he voted 2, 3 and 6 months before.
* For each factor on the scores file, her/his average 2, 3 and 6 months before.
* For the HI on the hi file , her/his average HI 2, 3 and 6 months before.

Also we added the Industry to that new dataset.
 
Finally,in order to proper work, we factorized the dataframe for prepare it for the different models, 
and removed our target variable. Also we removed the factor that includes that question.

### Looking for correlation.

A first check of the correlation...

![Happyforce](img/df_corr.png?raw=true)

... and filtering by any variable where the correlation is between the -6% and the 6% shows that:

* The Happiness Index question (in any of the different timeframes) has the biggest correlation over stress.
* Also the following questions have also a higher correlation:
    * The business goals and strategies set by senior leadership are taking |COMPANY_NAME| in the right direction.
    * |COMPANY_NAME| communicates in a clear and effective way us.
    * I trust that the people I work with are committed to do a good job
    * On a scale from 0-10, how would you rate the benefits |COMPANY_NAME| offers?
    * On a scale from 1 to 10, how likely are you to recommend |COMPANY_NAME| as good place to work?
    * I would rate the processes for determining pay in |COMPANY_NAME| as:
    * I would rate the amount of resources, people and efforts that |COMPANY_NAME| invests to achieve its goals as:
    * My teammates, welcome opinions different from their own.
    * Do you have the tools and resources you need to do your job?

* Employees working on FINANCIAL_SERVICES_INSURANCE seems to reflect more stress than others. On the other hand, 
MANAGMENT_CONSULTING and COMPUTER_SOFTWARE_IT_SERVICES have a negative correlation which shows that they suffer less stress.

# Modeling

With the data ready for the game, we deceided to focus on supervised algorithms:

* Decision tree.
* Random forest.
* Logistic Regression.

### Decision Tree

### Random Forest

### Logistic Regression

EDA para conseguir una base con todos los indicadores disponibles a nivel empleado.

Intentaremos identificar los factores principales con RandomForest.

Random Forest
El random forest es una metodología de clasificación que consiste en la combinación de árboles de decisión que actúan como un conjunto. El concepto es simple pero potente. Un número elevado de modelos (árboles) no correlacionados entre sí y utilizados de forma paralela, nos asegura, en principio, un resultado generalizado.

Feature Importance


Hiperparámetros


Cluster




Regresión



Red Neuronal


Resultados



Conclusiones







Looking correlation:

1- Vamos a construir un dataset, que dada la variable objetiva (Stress), tiene para cada empleado como era su HI:
	HI -> el mes anterior.
	HI -> tres meses.
	HI -> seis meses.

* companyId, sector, stress, promedio HI último 3 meses, promedio 6 meses, promedio 12 meses

Vamos  iterar sobre este concepto, buscando correlaciones o clusters entre estas features

Bibliografía
Random forest
https://towardsdatascience.com/understanding-random-forest-58381e0602d2
https://towardsdatascience.com/decision-tree-and-random-forest-explained-8d20ddabc9dd
https://www.analyticsvidhya.com/blog/2016/04/tree-based-algorithms-complete-tutorial-scratch-in-python/#nine

Cluster
https://www.aprendemachinelearning.com/k-means-en-python-paso-a-paso/
https://medium.com/machine-learning-for-humans/unsupervised-learning-f45587588294


# The Outcomes & Next steps:

### The Sample project

Under the app directory, you will find a [Streamlit](https://www.streamlit.io) demp app that calculates 
the probability of suffer stress on the following months. 

The app uses the persisted generated model of the Random Forest Classifier that you can find on the [notebook](stress_study.ipynb)


### The Future for Happyforce

Traditionally the results of any employee surveys, purse surveys are left just the table of HR or managers.
No outcomes but action plans that are not always fulfilled or have an impact on employees.

But... 

What if we were able to give value to employees automatically to all the contributions they make in surveys or pulses?
Or if we were able to tell a particular employee what will "hurt" him or her in the future, and how to act before it happens?

The practical implications of this project are much broader than stress. In the employee's day-to-day life, and throughout our professional career
we live hundreds of situations and feelings that we have to face, and skills (soft skills) to develop or improve.

One of the best outcomes of this project may be the inclusion of these models in Happyforce, thus supporting its mission of helping employees and organizations to be better, and impacting directly on employees life.

![Happyforce](img/happyforce-me.png?raw=true)

