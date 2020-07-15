# Saturdays.ai Team Stress Detection.

The following repository contains the final project part of Saturdays.AI (https://www.saturdays.ai/) build with other three alumni.

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
