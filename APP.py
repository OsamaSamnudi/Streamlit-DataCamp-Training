import streamlit as st
import pandas as pd
import plotly.express as px

st.cache_data()

# Sidebar :
st.sidebar.title("About Cheat Sheet")
st.sidebar.write('''
DataCamp Streamlit ChatSheet :
1) Display texts with Streamlit
2) Disply images and vedios
3) Input widgets (1) :
    - Check/select/multiselect box , box , radio , slider
4) Input widgets (2) :
    - input data , Uploading , color selction
5) Display progress and status with Streamlit
6) with st.spinner('Wait for it...)
7) Sidebar and container
8) Container
9) Display graphs with Streamlit
    1) Histogram
    2) Line Chart
10) Bar Chart
11) Area Chart
12) altair_chart
13) graphviz_chart
14) Display maps with Streamlit'
15) Run the Application
''')
st.title("DataCamp : Streamlit ChatSheet")
URL = "https://www.datacamp.com/tutorial/streamlit"
st.markdown(URL)
# st.markdown(f'[Click here to go to Google]({url})')
st.code("""
%%writefile APP.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.cache_data()

st.sidebar.title("About Data")
st.sidebar.write('''
DataCamp Streamlit ChatSheet :
1) Display texts with Streamlit
2) Disply images and vedios
3) Input widgets (1) :
    - Check/select/multiselect box , box , radio , slider
4) Input widgets (2) :
    - input data , Uploading , color selction
5) Display progress and status with Streamlit
6) with st.spinner('Wait for it...)
7) Sidebar and container
8) Container
9) Display graphs with Streamlit
    1) Histogram
    2) Line Chart
10) Bar Chart
11) Area Chart
12) altair_chart
13) graphviz_chart
14) Display maps with Streamlit'
15) Run the Application
''')
st.title("DataCamp : Streamlit ChatSheet")
""")
st.write('................................................................................................................................................................................')

# Display texts with Streamlit
st.write("Hello ,let's learn how to build a streamlit app together")
st.title("1) Display texts with Streamlit")
st.markdown('Markdown')
st.header('Header')
st.subheader('Subheader')
st.caption('Caption')
st.code('x=2022')
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.code(""" 
st.title('Title')
st.markdown('Markdown')
st.header('Header')
st.subheader('Subheader')
st.caption('Caption')
st.code('x=2022')
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
""")
st.write('................................................................................................................................................................................')

# Disply images and vedios
st.title("2) Disply images and vedios")
st.subheader('img osama)')
st.image("WinPhoto.jpg")
st.subheader('Audio : ربع تعالوا اتلوا ما حرم ربكم عليكم بصوت الشيخ اسماعيل علي')
st.audio('ربع تعالوا.m4a')
st.subheader('vedio : سورة الكهف بصوت الشيخ اسماعيل علي')
st.video("https://www.youtube.com/watch?v=Oo1IigalO50")

st.code("""
st.title("2) Disply images and vedios")
st.subheader('img osama)')
st.image("WinPhoto.jpg")
st.subheader('ربع تعالوا اتلوا ما حرم ربكم عليكم')
st.audio('ربع تعالوا.m4a')
st.subheader('vedio')
st.video("https://www.youtube.com/watch?v=Oo1IigalO50")
""")
st.write('................................................................................................................................................................................')

# Input widgets (Check/select/multiselect box , box , radio , slider)
st.title("3) Input widgets (Check/select/multiselect box , box , radio , slider)")
st.checkbox('YES')
st.button ('CLICK')
st.radio('Select you gender', ["Male" , "Female"])
st.selectbox ('Select your favorite place' , ["النيل" , "الازهر" , "البحر"])
st.multiselect ('Select your favorit country' , ["مكة" , "المدينة" , "مصر"] )
st.select_slider ("Pick Mark" , ["FAIR" , "GOOD" , "V GOOD"])
st.slider('Pick a number ' , 0 ,15)

st.code("""
st.checkbox('YES')
st.button ('CLICK')
st.radio('Select you gender', ["Male" , "Female"])
st.selectbox ('Select your favorite place' , ["النيل" , "الازهر" , "البحر"])
st.multiselect ('Select your favorit country' , ["مكة" , "المدينة" , "مصر"] )
st.select_slider ("Pick Mark" , ["FAIR" , "GOOD" , "V GOOD"])
st.slider('Pick a number ' , 0 ,15)
""")
st.write('................................................................................................................................................................................')

# Input widgets (input data , Uploading , color selction)
st.title("4) Input widgets (input data , Uploading , color selction)")
st.number_input('select a number' , 0 ,12)
st.text_input('enter you eamil')
st.date_input('Enter your birthdate')
st.time_input('your work time')
st.text_area('Your KPIs')
st.file_uploader('upload a photo')
st.color_picker('select your favorit color')

st.code("""
st.number_input('select a number' , 0 ,12)
st.text_input('enter you eamil')
st.date_input('Enter your birthdate')
st.time_input('your work time')
st.text_area('Your KPIs')
st.file_uploader('upload a photo')
st.color_picker('select your favorit color')
""")
st.write('................................................................................................................................................................................')

# Display progress and status with Streamlit
st.title("5) Display progress and status with Streamlit")
st.balloons()
st.subheader('waiting ...')
st.progress(10)
st.subheader('wating again ...')
st.code("""
st.balloons()
st.subheader('waiting ...')
st.progress(10)
st.subheader('wating again ...')
""")
st.write('................................................................................................................................................................................')


# with st.spinner('Wait for it...'):
st.title("6) with st.spinner('Wait for it...')")
# time.sleep(10) Not working
st.success('Done!')
st.error('error')
st.warning('warning')
st.info('FYI')
st.exception(RuntimeError('RuntimeError'))
st.code("""
st.success('Done!')
st.error('error')
st.warning('warning')
st.info('FYI')
st.exception(RuntimeError('RuntimeError'))
""")
st.write('................................................................................................................................................................................')

# Sidebar and container
st.title(' 7) Sidebar and container')
st.sidebar.title('Hello in sidebar')
st.sidebar.button('click')
st.sidebar.radio('Pick your gender' , ["Male" , "Female"])
st.code("""
st.sidebar.title('Hello in sidebar')
st.sidebar.button('click')
st.sidebar.radio('Pick your gender' , ["Male" , "Female"])
""")
st.write('................................................................................................................................................................................')

# Container
st.title('8) Container')
container = st.container()
container.write('This is a container')
st.write('wring your cv')
st.subheader('container end')
st.code("""
container = st.container()
container.write('This is a container')
st.write('wring your cv')
st.subheader('container end')
""")
st.write('................................................................................................................................................................................')

# Display graphs with Streamlit
st.title('9) Display graphs with Streamlit')
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Histogram
st.subheader('1) Histogram')
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)
st.code("""
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)
""")
st.write('................................................................................................................................................................................')

# Line Chart
st.subheader('2) Line Chart')
df = pd.DataFrame(np.random.randn (10 , 2) , columns=['x' , 'y'])
st.line_chart(df)
st.code("""
df = pd.DataFrame(np.random.randn (10 , 2) , columns=['x' , 'y'])
st.line_chart(df)
""")
st.write('................................................................................................................................................................................')

# Bar Chart
st.title('10) Bar Chart')
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(10 , 2) , columns= ['x' , 'y'])
st.bar_chart(df)
st.code("""
df = pd.DataFrame(np.random.randn(10 , 2) , columns= ['x' , 'y'])
st.bar_chart(df)
""")
st.write('................................................................................................................................................................................')

# Area Chart
st.title('11) Area Chart')
st.area_chart(df)
st.code("""
st.area_chart(df)
""")
st.write('................................................................................................................................................................................')

# altair_chart
st.title('12) altair_chart')
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

df = pd.DataFrame(np.random.randn(500, 3),columns=['x','y','z'])
c = alt.Chart(df).mark_circle().encode(x='x', y='y', size='z', color='z', tooltip=['x', 'y', 'z'])
st.altair_chart(c, use_container_width=True)

st.code ("""
df = pd.DataFrame(np.random.randn(500, 3),columns=['x','y','z'])
c = alt.Chart(df).mark_circle().encode(x='x', y='y', size='z', color='z', tooltip=['x', 'y', 'z'])
st.altair_chart(c, use_container_width=True)
""")
st.write('................................................................................................................................................................................')

# st.graphviz_chart()
st.title("13) graphviz_chart")
import graphviz as graphviz
st.graphviz_chart("""
digraph {
    DataCollection -> ETL
    ETL -> EDA
    EDA -> FeatureEngenieer
    FeatureEngenieer -> MLModels
    MLModels -> MLValidation
    MLValidation -> MLModelTuning
    MLModelTuning -> MLPipLine
    MLPipLine -> MLDeployment
}
""")
st.code("""
import graphviz as graphviz
st.graphviz_chart('''digraph {
    DataCollection -> ETL
    ETL -> EDA
    EDA -> FeatureEngenieer
    FeatureEngenieer -> MLModels
    MLModels -> MLValidation
    MLValidation -> MLModelTuning
    MLModelTuning -> MLPipLine
    MLPipLine -> MLDeployment}''')
""")
st.write('................................................................................................................................................................................')

# Display maps with Streamlit
st.title('14) Display maps with Streamlit')
import pandas as pd
import numpy as np
import streamlit as st

df = pd.DataFrame(np.random.randn(500 , 2)/[50,50]+[37.76 , -122.4] , columns= ['lat' , 'lon'])
st.map(df)
st.code("""
df = pd.DataFrame(np.random.randn(500 , 2)/[50,50]+[37.76 , -122.4] , columns= ['lat' , 'lon'])
st.map(df)
""")
st.write('................................................................................................................................................................................')

# Finally , Run our App :
st.title("15) Run the application")
st.code("""
!streamlit run APP.py
""")
st.write('GOOD JOB BROTHER')
st.write('................................................................................................................................................................................')
