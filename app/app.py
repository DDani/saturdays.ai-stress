import streamlit as st
import matplotlib.pyplot as plt
import pickle
import pandas as pd
import numpy as np

import warnings

warnings.filterwarnings('ignore')

# Just some variables for the selector
industry_types = {
    "ACCOMMODATION_AND_FOOT_SERVICES": "Accommodation and food services",
    "ARTS_ENTERTAINMENT_RECREATION": "Arts, entertainment and recreation",
    "COMPUTER_SOFTWARE_IT_SERVICES": "Computer software, IT & services",
    "CONSTRUCTION": "Construction",
    "EDUCATIONAL_SERVICES": "Educational services",
    "FINANCIAL_SERVICES_INSURANCE": "Financial Services, Insurance",
    "HEALTH_CARE_SOCIAL_ASSISTANCE": "Health care and social assistance",
    "MANAGEMENT_CONSULTING": "Management Consulting",
    "MANUFACTURING": "Manufacturing",
    "MARKETING_ADVERTISING": "Marketing & Advertising",
    "NATURAL_RESOURCES": "Natural Resources",
    "NON_PROFIT_ORGANIZATION": "Non-profit organization",
    "PROFESSIONAL_SCIENTIFIC_AND_TECHNICAL_SERVICES": "Professional, scientific and technical services",
    "PUBLIC_AND_GOVERMENT_ADMINISTRATION": "Public and government administration",
    "REAL_ESTATE_RENTAL_AND_LEASING": "Real estate and rental and leasing",
    "TRANSPORTATION_AND_WAREHOUSING": "Transportation and warehousing",
    "UTILITIES_AND_SERVICES": "Utilities & services",
    "WHOLESALE_AND_RETAIL_TRADE": "Wholesale and retail trade"
}


def getIndustryLabel(key):
    return industry_types.get(key)


def loadModel():
    # Load the model
    return pickle.load(open('random_forest.sav', 'rb'))


# Let's start to build the Streamlint UI

st.title('Stress predictor')

industry = st.sidebar.selectbox(
    label='Select your Industry',
    options=list(industry_types.keys()),
    format_func=getIndustryLabel
)

months = [2, 3, 6]
factors = 19
questions = 55
window = 99

# para preguntas 'HI' asignamos '1' a las respuestas con valor 1 o 2
limite_hi=2
# para stress (variable objetivo) asignamos '1' a las respuestas con valor 1, 2 o 3
limite_stress=3
# para el resto de preguntas asignamos '1' para valores inferiores o iguales a 5.
limite_resto=5

# Add the HI Sliders
st.sidebar.markdown('Happiness Index')
hi_options = {}
for i in months:
    key = 'vote_hi_M{}_{}'.format(i, window)
    hi_options[i] = st.sidebar.slider(
        'HI {} months ago?'.format(i),
        1, 4,
        key=key
    )

st.sidebar.markdown('Factors Index')
factor_options = {}
for i in range(factors):
    for j in months:
        key = 'vote_{}_f_M{}_{}'.format(i, j, window)
        factor_options[key] = st.sidebar.slider(
            'Factor {}, {} months ago?'.format(i, j),
            1, 10,
            key=key
        )

st.sidebar.markdown('Question Index')
question_options = {}
for i in range(questions):
    for j in months:
        key = 'vote_{}_q_M{}_{}'.format(i, j, window)
        question_options[key] = st.sidebar.slider(
            'Question {}, {} months ago?'.format(i, j),
            1, 10,
            key=key
        )

# Load the model
model = loadModel()


def build_parameters():
    # Build the paramerrs key:

    variables = {}

    variables['vote_stress_cat'] = 1;

    variables['month_1'] = 1;

    for key, value in industry_types.items():
        variables[key] = (industry == key)

    for key, value in hi_options.items():
        variables[key] = (1 if value <= limite_hi else 0)

    for key, value in factor_options.items():
        variables[key] = (1 if value <= limite_resto else 0)

    for key, value in question_options.items():
        variables[key] = (1 if value <= limite_resto else 0)

    parameters = pd.DataFrame(variables, index=[0])
    return parameters


analysis = build_parameters();

estimate = model.predict_proba(analysis)[0][0]
error = str(round(1 - model.oob_score_, 2)).ljust(4, '0')
importances= model.feature_importances_

if (estimate < 0.3):
    st.balloons()
    st.success('🕺 Nice, it seems that you will not suffer stress in the following months')
elif (estimate < 0.5):
    st.warning('🙏🏻 Watch out!, you can suffer stress on the following months')
else:
    st.error('🚨 Take care of yourself, with high probability you will suffer in the following months')

my_bar = st.progress(estimate)

st.text(f"You have a probability of {(estimate * 100):.2f}% of suffer stress")

st.text(f"with an error of {error}")
