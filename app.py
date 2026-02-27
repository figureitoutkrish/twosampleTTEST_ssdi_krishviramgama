import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import t


def one_sample_t_test(data, pop_mean):
    data = np.array(data, dtype=float)
    n = len(data)
    df = n - 1
    x_bar = np.mean(data)
    sd = np.std(data, ddof=1)
    se = sd / np.sqrt(n)
    t_cal = (x_bar - pop_mean) / se
    p_val = 1 - t.cdf(t_cal, df)

    return {'t_stats': t_cal, 'p_val': p_val}


# Streamlit UI
st.title("One Sample T-Test Calculator")

st.write("Enter sample data separated by commas")

data_input = st.text_area("Sample Data (e.g., 100,110,105,115)")
pop_mean = st.number_input("Population Mean", value=108.0)

if st.button("Calculate"):

    if data_input:
        try:
            data = [float(x.strip()) for x in data_input.split(",")]

            result = one_sample_t_test(data, pop_mean)

            st.subheader("Results")
            st.write(f"T-Statistic: {result['t_stats']:.4f}")
            st.write(f"P-Value: {result['p_val']:.4f}")

        except:
            st.error("Please enter valid numeric values separated by commas.")
    else:
        st.warning("Please enter sample data.")