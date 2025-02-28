import streamlit as st
import time as t
# st.image("st.png")
# this is way to define title
st.title(" Welcome to my app ('_')")
# header
st.header(" Machine learning ")
# sub header
st.subheader(" learn skill and make youself proud ")
# to give info
st.info(" This is used top give information ")
# warning
st.warning(" you have to come in class on time otherwise you will mark absent ")   
# write
st.write(" Employee name ")
st.write(range(50))
# eror
st.error(" Wrong password ")
# success
st.success(" your password is correct ")
# markdown it is used for text size adjustment 
st.markdown(" # intellipaat ")
st.markdown(" ## intellipaat ")
st.markdown(" ### intellipaat ")
# markdown alse used for getting emojies in the app
st.markdown(":heart:")
 
# text oi sused to write a simple text 
st.text(" a+bx^2+d ")

# caption is used to write a caption 
st.caption(" caption ")

# to write mat expression we use lattex
st.latex(r'''a+bx^2+d''')

#widgets 

# checkbox
st.checkbox('login')

# button create a button
st.button("click me")

# radio is used to pick out the one from options 
st.radio("select your gender",["Male","Female","Others"])

# selectbox is used to pick out one from dropdown menu 
st.selectbox("pick your course",["Machine learning","Computer Sciencee","Information On Technology"])

# multiselect is used to choose multiple option 
st.multiselect("Pick your interest",["data scientist","software","Web Dev"])

# selectslidebar is used to gave ration and all or may be setting price according to budget
st.select_slider("rating",["Good","Best","Excellent","Outstanding"])

#  to just select number
st.slider("Edit you number",1,100)

#take user input
st.text_input("Enter your email")

# take numeric input
st.number_input("pick number",1,100)

# date input
st.date_input("opening ceramony")

# time input
st.time_input("hey time")

# text area for writing something
st.text_area("enter your text")

# upload any file
st.file_uploader("upload your file")
st.file_uploader(
           "Choose a CSV file", accept_multiple_files=True
)

# color picker
st.color_picker("color")

# progress 
st.progress(9)

# spinner is used to wait for somw time  to show loading process
# def myfun():
#     return ("## Succesfully done")
# with st.spinner("Just wait.."):
#     #  now we have to use here time with it to tell how time it should wait
#     t.sleep(3)
#     st.write(myfun())

def custom_action():
    st.write("Button was clicked! Performing an action...")
    def myfun():
        return ("## Succesfully done")
    with st.spinner("Just wait.."):
        t.sleep(3)
        st.write(myfun())    

# Create a button
if st.button('Click Me'):
    custom_action()