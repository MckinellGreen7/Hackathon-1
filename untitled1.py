import streamlit as st
import pandas as pd
import pathlib
#import matplotlib.pyplot as plt 
#import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
#from sklearn.metrics import confusion_matrix, classification_report
#from sklearn.metrics import precision_score, recall_score,f1_score
#from sklearn.metrics import plot_roc_curve
from streamlit_lottie import st_lottie
import requests
import PIL.Image
st.set_page_config(page_title="FitOps", page_icon=":tada:", layout= "wide")

#from PIL import Image
#image = Image.open(r"C:\Users\hp\Desktop\Water-Potability\photo1.png")
#i#mage2 = Image.open(r"C:\Users\hp\Desktop\Water-Potability\photo2.png")
header = st.container()
STREAMLIT_STATIC_PATH = pathlib.Path(st.__path__[0]) / 'static'
#print(STREAMLIT_STATIC_PATH/"Untitled-1.css")
#from PIL import Image
CSS_PATH = (STREAMLIT_STATIC_PATH / "Untitled-1.css")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write('##')
        original_title = '<p style=" text-align: left; background: linear-gradient(to right, #a8c0ff, #3f2b96);color:transparent;background-clip:text;-webkit-background-clip: text; font-weight: Bold; font-size: 70px;" class = "heading">FitOps</p>'
        st.markdown(original_title, unsafe_allow_html=True)
    #with right_column:
        #st.image(image2, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_nw19osms.json")
current_dir = pathlib.Path(__file__).parent if "__file__" in locals() else pathlib.Path.cwd()
print(current_dir)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
#local_css(r"C:\Users\hp\Desktop\Water-Potability\Untitled-1.css")
local_css(current_dir/"Untitled-1.css")


    #original_script = '<p style=" text-align: center; font-family:Lato; font-size: 18px; font-weight: Bold; border-width:3px; border-style:solid; border-color:#FF0000; padding: 1em;">   In this project we will find out whether the water is potable or not.</p>'
    #st.markdown(original_script, unsafe_allow_html=True)

with st.container():
    st.subheader("#")
    st.title("Introducing Kidney Disease Prediction to Everyone")
    st.write("Get a free report regarding your Kidney functionality on our Machine Learning model based on real life datasets.")
with st.container():
    st.write("...")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Chronic Kidney Diseases are Life Threatening.")
        st.write("##")
        st.write(
        """
 Chronic kidney disease, also called chronic kidney failure, involves a gradual loss of kidney function. Your kidneys filter wastes and excess fluids from your blood, which are then removed in your urine. Advanced chronic kidney disease can cause dangerous levels of fluid, electrolytes and wastes to build up in your body.

In the early stages of chronic kidney disease, you might have few signs or symptoms. You might not realize that you have kidney disease until the condition is advanced. Use our page to get accurate results. 
        """
        )
    with right_column:
            st_lottie(lottie_coding, height = 500, quality="high", key="AI powered predictor")





dataset = st.container()
features = st.container()
inputs = st.container()
time = st.container()





    






#@st.cache(for running it for one time if the file name is same then its not going to run again)
#def get_data():
#  taxi_data=pd.read_csv

# For customization u can use css:
# =============================================================================
# st.markdown(
#     """
#     <style>
#     .main {
#     background-color:#F5F5F5;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True)
# ============================================================================
    
#st.markdown("![Alt Text](https://www.edureka.co/blog/wp-content/uploads/2018/08/Insurance-Leadspace-Aniamted.gif)")
    

st.write("###")
st.write("###")
st.write("###")

st.write("###")
st.write("###")
st.write("###")
with dataset:
    st.header("Kidney Patients Dataset")
    
    
    df=pd.read_csv(current_dir/"kidney1.csv")
    st.write(df.head())
    st.text("Courtesy: Kaggle")
    st.subheader("Predicting Kidney Disease")
    a=df['class'].value_counts()
    st.bar_chart(a,height=500)
    
    
    
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_5tl1xxnz.json")




st.write("###")
with st.container():
    with left_column:
        st.header("The features on which the model is trained")
        st.markdown('* Age')
        st.markdown('* Blood Pressure')
        st.markdown('* Albumin count')
        st.markdown('* Puss Cell Clumps count')
        st.markdown('* Blood Glucose Random number')
        st.markdown('* Blood Urea number')
        st.markdown('* Serum Creatinine count')
        st.markdown('* Haemoglobin')
        st.markdown('* Packed Cell Volume')
        st.markdown('* HyperTension')
        
    with right_column:
            st_lottie(lottie_coding, height = 600, quality="high", key="AI powered")
    
    
    

    
with inputs:
    st.text("Enter the inputs according to your test values")
    
    sel_col,disp_col = st.columns(2)
    
    age=sel_col.slider('Age',min_value=0,max_value=110,value=51)
    bp=sel_col.slider('Blood Pressure',min_value=50,max_value=180,value=76,step=10)
    al=sel_col.selectbox("Albumin",options=[0,1,2,3,4,5],index=0)
    pcc=sel_col.selectbox("Puss Cell Clumps",options=[0,1],index=0)
    bgr=sel_col.slider('Blood Glucose Random',min_value=20,max_value=500,value=150,step=10)
    bu=sel_col.slider('Blood Urea',min_value=1,max_value=400,value=60,step=1)
    sc=sel_col.slider('Serum Creatinine',min_value=1,max_value=80,value=3,step=1)
    hemo=sel_col.slider('Haemoglobin',min_value=2,max_value=20,value=12,step=1)
    pcv=sel_col.slider('Packed Cell Volume',min_value=9,max_value=54,value=37,step=1)
    htn=sel_col.selectbox('HyperTension',options=[0,1],index=0)
    dm=sel_col.selectbox('Diabetes Mellitus',options=[0,1],index=0)
    appet=sel_col.selectbox('Appetite',options=[0,1],index=0)    
    #n_estimators=sel_col.slider('How many trees should be there', min_value=10,max_value=1000,value=200,step=10)
    arr=[[age,bp,al,pcc,bgr,bu,sc,hemo,pcv,htn,dm,appet]]
    #input_feature = sel_col.text_input("Which feature should be used as the input feature","pH")
    
    clf=LogisticRegression()
    X=df.drop('class',axis=1)
    y=df['class']
    clf.fit(X,y)
    
    st.write("###")
    y_pred=clf.predict(arr)
    print(y_pred)
    if y_pred==0:
        import time
        with st.spinner(text='Calculating..'):
            time.sleep(1)
            st.success('### Result : You are doing well')
        #st.write("""""")
    else:
        import time
        with st.spinner(text='Calculating..'):
            time.sleep(1)
            st.error('###  Result : The patient might have chronic Kidney disorder.')
            st.write('##')
            st.header("Plan of Action")
            st.write("Refer to link : [link]https://dvha.vermont.gov/sites/dvha/files/documents/providers/VCCI/kidney-disease-action-plan-1.pdf")
            st.write("Please contact a doctor immediately.")
            st.header("Want to collaborate with our projects in Future!\nThen get in Touch with us ")
            st.write("##")
            contact_form = '''
            <form action="https://formsubmit.co/mckinellgreen7@gmail.com" method="POST">
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

