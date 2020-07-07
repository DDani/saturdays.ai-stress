# Saturdays.ai Team Stress Detection.

The following repository contains the final project part of Saturdays.AI (https://www.saturdays.ai/) build with other three alumni.

# Introduction

Happyforce (www.myhappyforce.com) is a Employee Engagement platform used by companies to measure the level of engagement of their employees, allowing managers and teams to improve in order to improve, motivate and retain talent.

Unlike a climate survey (which is usually annual), Happyforce carries out a continuous measurements of different employee engagement dimensions (https://en.wikipedia.org/wiki/Employee_engagement) via pulse surveys and a daily check-in question.

This provides and unvaluable dataset for research correlation and predictions based on previous gathered data.

Inside all dimensions measured by Happyforce, there is one that is a perfect match for the values that we must chase on a Saturday.ai project: a social aspect. 
This dimension is Employee Stress. Stress has been described as the health epidemic of the 21th century.

# Challenge and objetive:

With this project we will try to determine which variables mainly affect to employee's stress, and we will try to build a model for predicting when an employee will suffer stress on the following months.

# Definitions:

The Happyforce stress question is formulated on a scale between 1 and 10, where 1 is high stressed and 10 is low stressed. We will set the threshold below 3 (included), to determine when an employee is stressed or not.

# Dataset:

Disponemos de base de datos de Happyforce con las diferentes preguntas/indicadores que han respondido los empleados con la fecha y la compañía a la que pertenecen.

# Approach:
Metodología:

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
