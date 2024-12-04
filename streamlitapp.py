import streamlit as st
import pandas as pd
import numpy as np
st.title("I'm sorry")
# Header
st.header('Apology letter')
#Subheader
#Text
st.text(""I hope you're doing okay. I've been thinking a lot about us lately, and there's something I need to get off my chest. I want to start by saying how sorry I am. I know I've been too clingy and always wanting to be around you, and I didn't realize how that might have been overwhelming.

The truth is, I just care about you so much that sometimes I forget you need your own space and time to focus on your life too. It wasn't fair of me to make you feel like you had to constantly be there for me, and I'm truly sorry for that. I never want you to feel like I don't respect your independence or your need to breathe.

I promise to work on giving you the space you deserve and trusting that we're strong enough to be apart when we need to. I just hope you can forgive me and understand that I'm coming from a place of love, even if I didn't express it the right way.

Thank you for being patient with me. I'm so lucky to have you in my life, and I'll do my best to show you that in a healthier way moving forward."")

options = st.multiselect(
    'Kesalahan pacar kamu apa aja?',
    ['Ignorant', 'Mean and selfish', 'bpd', 'Annoying','Self-centered','Bad Hygience (We both know thats now true)','Jelek','Abuser'],
    ['Ignorant', 'bpd'])

st.write('You selected:', options)

# Latex widget example
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# to display pandas dataframe object

df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df)  


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)



# radio widget to take inputs from mulitple options
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")


