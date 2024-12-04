import streamlit as st
import pandas as pd
import numpy as np

st.title('This is a title')
# Header
st.header('This is a header')
#Subheader
st.subheader('This is a subheader')
#Text
st.text('This is a text')
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
# Usage of multiselect widget
import streamlit as st

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue','Pink','Purple','Grey','Navy Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)
from PIL import Image
image = Image.open('sunrisemountain.jpg')
st.image("sunrisemountain.jpg", caption="Sunrise and Mountain")
