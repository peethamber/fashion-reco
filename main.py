import streamlit as st
import os
from PIL import Image
import numpy as np
import pickle
import tensorflow
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input
from numpy.linalg import norm
from sklearn.neighbors import NearestNeighbors
import re

OG_codes_array = [
        "ROD",
        "RCB",
        "REL",
        "RCT",
        "RET",
        "RCD",
        "RED",
        "RKS",
        "RFT",
        "RFS",
        "RES",
        "RCS",
        "RCK",
        "RCP",
        "REP",
        "REG",
        "ROK",
        "RGB",
        "RJB",
        "RJN",
        "RJE",
        "RJS",
        "ROC",
        "REM",
        "RFC",
        "RMT",
        "RMS"

    ]
OG_codes_array_lower = [
        "rod",
        "rcb",
        "rel",
        "rct",
        "ret",
        "rcd",
        "red",
        "rks",
        "rft",
        "rfs",
        "res",
        "rcs",
        "rck",
        "rcp",
        "rep",
        "reg",
        "rok",
        "rgb",
         "rjb",
        "rjn",
        "rje",
        "rjs",
        "roc",
        "rem",
        "rfc",
        "rmt",
        "rms"

    ]

RB_codes_array = [
     "RKC",
     "RKF",

]

RB_codes_array_lower = [
     "rkc","rkf"
]

feature_list = np.array(pickle.load(open('embeddings.pkl','rb')))


filenames = pickle.load(open('filenames.pkl','rb'))


model = ResNet50(weights='imagenet',include_top=False,input_shape=(224,224,3))
model.trainable = False
model = tensorflow.keras.Sequential([
    model,GlobalMaxPooling2D()
])

st.set_page_config(layout="wide")

st.title("Designs Recommender")
st.subheader("Select your best picture from your device and see matching designs from our store")

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join("./",uploaded_file.name),'wb') as f:
            f.write(uploaded_file.getbuffer())
            return 1
    except:
        return 0

def feature_extraction(img_path, model):
    img = image.load_img(img_path,target_size=(224,224))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array,axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    result = model.predict(preprocessed_img).flatten()
    normalized_result = result/norm(result)

    return normalized_result

def check_sub(sub,filename):
    
    # if sub == "RKFCW" or sub == "rkfcw":
    #     if sub in os.path.basename(filename):
    #             ind = os.path.basename(filename).find(sub)
    #             sub1 = os.path.basename(filename)[ind:ind+8]
                
    #             sub1 = re.sub('-','',sub1)
    #             url = "https://www.rebblebee.com/AllProducts?"+sub1
                
    #             st.markdown(f'''
    #             <a href={url}><button style="background-color:Gray;">{sub1}</button></a>
    #             ''',
    #             unsafe_allow_html=True)

    # if sub == "RKFCTT" or sub == "rkfctt":
    #     if sub in os.path.basename(filename):
    #             ind = os.path.basename(filename).find(sub)
    #             sub1 = os.path.basename(filename)[ind:ind+9]
                
    #             sub1 = re.sub('-','',sub1)
    #             url = "https://www.rebblebee.com/AllProducts?"+sub1
                
    #             st.markdown(f'''
    #             <a href={url}><button style="background-color:Gray;">{sub1}</button></a>
    #             ''',
    #             unsafe_allow_html=True)

    # if sub == "REJS" or sub == "rejs":
    #     if sub in os.path.basename(filename):
    #             ind = os.path.basename(filename).find(sub)
    #             sub1 = os.path.basename(filename)[ind:ind+7]
                
    #             sub1 = re.sub('-','',sub1)
    #             url = "https://www.onati-global.com/AllProducts?"+sub1
               
    #             st.markdown(f'''
    #             <a href={url}><button style="background-color:Gray;">{sub1}</button></a>
    #             ''',
    #             unsafe_allow_html=True)
                
    # if sub == "RRBMS" or sub == "rrbms":
    #     if sub in os.path.basename(filename):
    #             ind = os.path.basename(filename).find(sub)
    #             sub1 = os.path.basename(filename)[ind:ind+8]
                
    #             sub1 = re.sub('-','',sub1)
    #             url = "https://www.onati-global.com/AllProducts?"+sub1
               
    #             st.markdown(f'''
    #             <a href={url}><button style="background-color:Gray;">{sub1}</button></a>
    #             ''',
    #             unsafe_allow_html=True)

    if sub in OG_codes_array:
         if sub in os.path.basename(filename):
                ind = os.path.basename(filename).find(sub)
                sub1 = os.path.basename(filename)[ind:ind+6]
                
                sub1 = re.sub('-','',sub1)
                url = "https://www.onati-global.com/AllProducts?"+sub1
               
                st.markdown(f'''
                <a href={url}><button style="background-color:Gray;">{sub1}</button></a>
                ''',
                unsafe_allow_html=True)

    if sub in OG_codes_array_lower:
         if sub in os.path.basename(filename):
                ind = os.path.basename(filename).find(sub)
                sub1 = os.path.basename(filename)[ind:ind+6]
                
                sub1 = re.sub('-','',sub1)
                url = "https://www.onati-global.com/AllProducts?"+sub1
                
                st.markdown(f'''
                <a href={url}><button style="background-color:Gray;">{sub1}</button></a>
                ''',
                unsafe_allow_html=True)

    if sub in OG_codes_array:
         if sub in os.path.basename(filename):
                ind = os.path.basename(filename).find(sub)
                sub1 = os.path.basename(filename)[ind:ind+6]
                
                sub1 = re.sub('-','',sub1)
                url = "https://www.onati-global.com/AllProducts?"+sub1
               
                st.markdown(f'''
                <a href={url}><button style="background-color:Gray;">{sub1}</button></a>
                ''',
                unsafe_allow_html=True)

    if sub in RB_codes_array_lower:
         if sub in os.path.basename(filename):
                ind = os.path.basename(filename).find(sub)
                sub1 = os.path.basename(filename)[ind:ind+6]
                
                sub1 = re.sub('-','',sub1)
                url = "https://www.rebblebee.com/AllProducts?"+sub1
                
                st.markdown(f'''
                <a href={url}><button style="background-color:Gray;">{sub1}</button></a>
                ''',
                unsafe_allow_html=True)

    if sub in RB_codes_array_lower:
         if sub in os.path.basename(filename):
                ind = os.path.basename(filename).find(sub)
                sub1 = os.path.basename(filename)[ind:ind+6]
                
                sub1 = re.sub('-','',sub1)
                url = "https://www.rebblebee.com/AllProducts?"+sub1
               
                st.markdown(f'''
                <a href={url}><button style="background-color:Gray;">{sub1}</button></a>
                ''',
                unsafe_allow_html=True)
         
         

def do_all_code_checks(fname):
    # check_sub("RKFCW",fname)
    # check_sub("rkfcw",fname)

    # check_sub("RKFCTT",fname)
    # check_sub("rkfctt",fname)

    # check_sub("REJS",fname)
    # check_sub("rejs",fname)

    # check_sub("RRBMS",fname)
    # check_sub("rrbms",fname)

   
    for code in OG_codes_array:
         check_sub(code,fname)

    for code in OG_codes_array_lower:
         check_sub(code,fname)

    for code in RB_codes_array:
         check_sub(code,fname)

    for code in RB_codes_array_lower:
         check_sub(code,fname)
         

def recommend(features,feature_list):
    neighbors = NearestNeighbors(n_neighbors=8,algorithm='brute',metric='euclidean')
    neighbors.fit(feature_list)

    distances,indices = neighbors.kneighbors([features])
    return indices

uploaded_file = st.file_uploader("choose an image")

img_width = 230

if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        display_image = Image.open(uploaded_file)
        st.image(display_image,width=450)
        features = feature_extraction(os.path.join('./',uploaded_file.name),model)
        indices = recommend(features,feature_list)
        
        st.subheader("Design recommendations from us")

        col1,col2,col3,col4,col5,col6,col7 = st.columns(7)

        with col1:
            st.markdown('<style>.stMarkdown > div { border: 2px solid #000; }</style>', unsafe_allow_html=True)
            st.image(filenames[indices[0][0]],width = img_width)
            st.write(os.path.basename(filenames[indices[0][0]]))
            #do_all_code_checks(filenames[indices[0][0]])
            
            
        with col2:
            st.markdown('<style>.stMarkdown > div { border: 2px solid #000; }</style>', unsafe_allow_html=True)
            st.image(filenames[indices[0][1]],width = img_width)
            st.write(os.path.basename(filenames[indices[0][1]]))
            #do_all_code_checks(filenames[indices[0][1]])
            
        with col3:
            st.markdown('<style>.stMarkdown > div { border: 2px solid #000; }</style>', unsafe_allow_html=True)
            st.image(filenames[indices[0][2]],width = img_width)
            st.write(os.path.basename(filenames[indices[0][2]]))
            #do_all_code_checks(filenames[indices[0][2]])

        with col4:
            st.markdown('<style>.stMarkdown > div { border: 2px solid #000; }</style>', unsafe_allow_html=True)
            st.image(filenames[indices[0][3]],width = img_width)
            st.write(os.path.basename(filenames[indices[0][3]]))
            #do_all_code_checks(filenames[indices[0][3]])

        with col5:
            st.markdown('<style>.stMarkdown > div { border: 2px solid #000; }</style>', unsafe_allow_html=True)
            st.image(filenames[indices[0][4]],width = img_width)
            st.write(os.path.basename(filenames[indices[0][4]]))
            #do_all_code_checks(filenames[indices[0][4]])

        with col6:
            st.markdown('<style>.stMarkdown > div { border: 2px solid #000; }</style>', unsafe_allow_html=True)
            st.image(filenames[indices[0][4]],width = img_width)
            st.write(os.path.basename(filenames[indices[0][5]]))
            #do_all_code_checks(filenames[indices[0][5]])
        
        with col7:
            st.markdown('<style>.stMarkdown > div { border: 2px solid #000; }</style>', unsafe_allow_html=True)
            st.image(filenames[indices[0][4]],width = img_width)
            st.write(os.path.basename(filenames[indices[0][6]]))
            #do_all_code_checks(filenames[indices[0][6]])
      
    else:
        st.error("Error while uploading file")

