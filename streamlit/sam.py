import streamlit as st
st.title("r y")                               #title
st.header('i am')                             #header
st.subheader("sub header")                    #subheader
st.text('text ->gfg')                         #text
st.markdown("# i am good")                    #markdown
st.markdown("## i am good")
st.markdown("### i am good")
st.markdown("#### i am good")
st.markdown("##### i am good")

st.success('success command')                 #success
st.info("info command ")                      #info
st.warning("warming")                         # WARNING:
st.error("error")                             #error

st.exception(ZeroDivisionError('Division not possible with 0'))         #exception
st.help(ZeroDivisionError)                   #help

st.write("range(1,10)")                      #write
st.write(range(1,10))
st.write('1+2+3')
st.write(1+2+3)

st.code('x=10 \n'                           #code
         'for i in range(x):\n'
          '\tprint(i)')

st.checkbox('male')                        #checkbox
if(st.checkbox('female')):                 #checkbox with validation
    st.write("you're an adult")

st.subheader('Radio Button')
radioButton=st.radio('select: ',{'male','female','other'})  #radio button
if(radioButton=='male'):
    st.write("you're a male")
elif(radioButton=='female'):
    st.write("you're a female")
elif(radioButton=='other'):
    st.write("you're an other gender")

st.subheader("Select Box")
selectBox=st.selectbox('Data Science : ',['Data Analysis','Machine Learning',
                                          "Web scraping","natural Language processing",
                                          'Computer Vision'])
st.write('you have selceted :', selectBox)

st.subheader("MultiSelect Box")               #MultiSelectBox
multislect=st.multiselect('Data Science : ',['Data Analysis','Machine Learning',
                                          "Web scraping","natural Language processing",
                                          'Computer Vision'])

st.write('you have selceted :', len(multislect),"multiselect")


st.subheader('Button')                      #button

if (st.button('Click Me')):
    st.write('thanks for clicking me')

st.subheader("Slider")                       #slider
st.slider('Selcet the level',1,10,step=1)

st.subheader('text input')                   #text-Input
username=st.text_input("Name")
password=st.text_input("Password", type='password')

st.subheader("Text Area")                   #text-area
st.text_area("write something ...")

st.subheader("Input Number")                #input-Number
st.number_input('Select your age ',18 ,110)

st.subheader("Input Date")                 #input- time
st.date_input("Date")

st.subheader("Input time")                #input-time
st.time_input('Time ')
