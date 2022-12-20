import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
#rom sklearn.metrics import confusion_matrix, classification_report
#rom sklearn.metrics import precision_score, recall_score,f1_score
#rom sklearn.metrics import plot_roc_curve
from streamlit_lottie import st_lottie
import requests
import pathlib

st.set_page_config(page_title="FitOps", page_icon=":tada:", layout= "wide")
STREAMLIT_STATIC_PATH = pathlib.Path(st.__path__[0]) / 'static'
#print(STREAMLIT_STATIC_PATH/"Untitled-1.css")
#from PIL import Image
CSS_PATH = (STREAMLIT_STATIC_PATH / "Untitled-1.css")
current_dir = pathlib.Path(__file__).parent if "__file__" in locals() else pathlib.Path.cwd()
print(current_dir)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
#local_css(r"C:\Users\hp\Desktop\Water-Potability\Untitled-1.css")
local_css(current_dir/"Untitled-1.css")

# from PIL import Image
# image = Image.open("C:\\Users\\Lenovo\\Desktop\\Hack1\\SmartSelect_20221216_135144_Canva.jpg")
header = st.container()
from PIL import Image
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write('##')
        original_title = '<p style=" text-align: left; background: linear-gradient(to right, #a8c0ff, #3f2b96);color:transparent;background-clip:text;-webkit-background-clip: text; font-weight: Bold; font-size: 70px;" class = "heading">FitOps</p>'
        st.markdown(original_title, unsafe_allow_html=True)
    # with left_column:
        # st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
# with st.container():
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.write('##')
#         original_title = '<p style=" text-align: left; background: linear-gradient(to right, #a8c0ff, #3f2b96);color:transparent;background-clip:text;-webkit-background-clip: text; font-weight: Bold; font-size: 70px;" class = "heading">FitOps</p>'
#         st.markdown(original_title, unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/temp/lf20_fPETSw.json")


with st.container():
    st.subheader("#")
    st.title("Introducing Health Prediction Model to everyone")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What is FitOps?")
        st.write("##")
        st.write(
        """
        “FitOps” is a machine learning model project that works to predict...........
        """
        )
    with right_column:
        st_lottie(lottie_coding, height = 500, quality="high", key="AI powered predictor")

dataset = st.container()
features = st.container()
inputs = st.container()
time = st.container()
st.write("###")
st.write("###")
st.write("###")
st.write("###")
st.write("###")
st.write("###")
with dataset:
    st.header("Heart Disease Classification Dataset")
    st.text("Dataset acquired from Kaggle")
    
    df=pd.read_csv(current_dir/"heart-disease.csv")
    st.write(df.head())
    
    st.subheader("Characteristics:")
    a=df['target'].value_counts()
    st.bar_chart(a,height=500)
  
  
  
st.write("###")
st.write("###")
st.write("###")
with st.container():
    with left_column:
        st.header("The features on which the model is trained")
        st.markdown('* Age')
        st.markdown('* Sex')
        st.markdown('* Chest Pain Type')
        st.markdown('* Resting Blood Pressure')
        st.markdown('* Serum Cholestoral')
        st.markdown('* Fasting Blood Sugar')
        st.markdown('* Resting electrocardiographic results')
        st.markdown('* Maximum heart rate achieved')
        st.markdown('* Enlarged hearts main pumping chamber')
        st.markdown('* ST Depression')
        st.markdown('* Slope of the peak exercise ST Segment')
        st.markdown('* Number of major vessels (0-3) colored by flourosopy')
        st.markdown('* Thalium stress result')
        
        

with inputs:
    st.header("Time to take input from the user")
    st.text("Enter the inputs according to the parameters considered")
    
    sel_col,disp_col = st.columns(2)
    
    
    age=sel_col.slider('Age',min_value=29,max_value=77,value=30)
    sex=sel_col.selectbox("Sex",options=[0,1],index=0)
    cp=sel_col.slider('Chest pain Type',min_value=0,max_value=3,value=1)
    trestbps=sel_col.slider('Resting blood pressure',min_value=94,max_value=200,value=131)
    chol=sel_col.slider('Serum Cholestoral',min_value=126,max_value=525,value=246)
    fbs=sel_col.selectbox('Fasting Blood Sugar',options=[0,1],index=0)
    restecg=sel_col.selectbox('Resting electrocardiographic results',options=[0,1,2],index=0)
    thalach=sel_col.slider('Maximum Heart Rate Achieved',min_value=70,max_value=202,value=149)
    exang=sel_col.selectbox('Enlarged heart main pumping chamber',options=[0,1],index=0)
    oldpeak=sel_col.slider('ST Depression',min_value=0.0,max_value=6.0,value=1.0,step=0.1)    
    slope=sel_col.selectbox(' Slope of the peak exercise ST Segment',options=[0,1,2],index=0)
    ca=sel_col.slider(' Number of major vessels (0-3) colored by flourosopy',min_value=0,max_value=4,value=1)
    thal=sel_col.selectbox('Thalium stress result',options=[0,1,2,3],index=0)
    #n_estimators=sel_col.slider('How many trees should be there', min_value=10,max_value=1000,value=200,step=10)
    arr=[[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]
    #input_feature = sel_col.text_input("Which feature should be used as the input feature","pH")
    
    clf=LogisticRegression()
    
    X=df.drop('target',axis=1)
    y=df['target']
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
    clf.fit(X_train,y_train)
    
    st.write("###")
    y_pred=clf.predict(arr)
    
    if y_pred==0:
        import time
        with st.spinner(text='Calculating..'):
            time.sleep(1)
            st.success('### You are doing well!')
        #st.write("""""")
    else:
        import time
        with st.spinner(text='Calculating..'):
            time.sleep(1)
            st.error('###  You might have Heart Disorder!')
            
            
            st.header("Plan of action")
            st.write("Please consult a doctor or Cardiologist immediately")
            st.write("Refer to link : [Link]https://dvha.vermont.gov/sites/dvha/files/documents/providers/VCCI/cad-heart-disease-action-plan.pdf")
            
    with st.container():
        st.write("###")
        st.write("###")
        st.header("Want to collaborate with our projects in Future!\nThen get in Touch with us ")
        st.write("##")
        contact_form = '''
        <form action="https://formsubmit.co/shivamanik593@gmail.com" method="POST">
        <input type ="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder = "Your Name" required>
        <input type="email" name="email" placeholder = "Your Mail_id" required>
        <textarea name = "message" placeholder="Your Message" required></textarea>
        <button type="submit">Send</button>
        </form>
        '''
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)

    

