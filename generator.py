import streamlit as st
import pandas as pd
import numpy as np
import random

st.title('Random Number Generator')

types = ["Ultra Lotto 6/58", "Grand Lotto 6/55", "Super Lotto 6/49", "Mega Lotto 6/45", "Lotto 6/42"]
quotes = ["With great power comes great responsibility. - Uncle Ben, Spiderman",
          "Dollar, dollars, dropping on my a$$ tonight! - Lisa Manoban",
          "Money is the opposite of the weather. Nobody talks about it, but everybody does something about it. - Rebecca Johnson",
          "The trick is to stop thinking of it as 'your' money. - an IRS auditor",
          "Too many people spend money they haven't earned, to buy things they don't want, to impress people they don't like. - Will Smith",
          "Money's only something you need in case you don't die tomorrow. - Carl Fox (played by Martin Sheen), Wall Street",
          "It's amazing how fast later comes when you buy now! - Milton Berle",
          "You can be young without money but you can't be old without it. - Tennessee Williams",
          "Money is like manure; it's not worth a thing unless it's spread around. - Brooke Astor",
          "Don't stay in bed, unless you can make money in bed. - George Burns"]

with st.form("factors"):
	lotto_type = st.selectbox("What type of lotto are you entering?", types)
	max_range = 58
	num_sets = st.number_input("How many sets do you want to fill in?", min_value=1, max_value=6, value="min", step=1, format="%d", key="sets")
	include_quotes = st.selectbox("Do you want a complementary inspirational quote with each set?", ["Yes", "No"])
	submit = st.form_submit_button("Generate numbers!")

if lotto_type == types[1]: # I am NOT typing "Grand Lotto 6/55" out.
    max_range = 55
elif lotto_type == types[2]:
    max_range = 49
elif lotto_type == types[3]:
    max_range = 45
elif lotto_type == types[4]:
    max_range = 42

if submit:
    for i in range(num_sets):
        cur_set = []
        j = 0
        while len(cur_set) < 6:
            num = random.randint(1, max_range)
            if num not in cur_set:
                cur_set.append(num)
        cur_set.sort()
        st.write(f"Set {i + 1}: {cur_set}")
        if include_quotes == "Yes":
            st.write(quotes[sum(cur_set) % 10])
