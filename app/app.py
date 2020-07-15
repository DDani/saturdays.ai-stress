import streamlit as st
import numpy as np
import pandas as pd


industry_types = {
    "ACCOMMODATION_AND_FOOT_SERVICES": "Accommodation and food services",
    "ARTS_ENTERTAINMENT_RECREATION":"Arts, entertainment and recreation",
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
    "REAL_ESTATE_RENTAL_AND_LEASING":  "Real estate and rental and leasing",
    "TRANSPORTATION_AND_WAREHOUSING": "Transportation and warehousing",
    "UTILITIES_AND_SERVICES": "Utilities & services",
    "WHOLESALE_AND_RETAIL_TRADE": "Wholesale and retail trade"
}

def getIndustryLabel(key):
    return industry_types.get(key)


st.title('Stress predictor')

add_selectbox = st.sidebar.selectbox(
    label='Select your Industry',
    options=list(industry_types.keys()),
    format_func=getIndustryLabel
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0, 4
)