import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Sigmoid Activation Function")

st.write("Sigmoid(x) = 1 / (1 + e^(-x))")

x = np.linspace(-10, 10, 400)
y = 1 / (1 + np.exp(-x))

plt.figure()
plt.plot(x, y)
plt.xlabel("Input (x)")
plt.ylabel("Output")
plt.grid(True)

st.pyplot(plt)
