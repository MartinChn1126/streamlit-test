import streamlit as st

st.set_page_config(page_title=None,layout='wide')
st.markdown(
    """
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {visibility:hidden,disply:None}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>""", 
    unsafe_allow_html=True
)


from work import main_page
def login_page():
    
    # create the login_in page
    with st.container(border=True):
        with st.form(key='login_form',border=False):
            username = st.text_input('Name',key='name')
            password = st.text_input('Password',key='password',type='password')
            submit = st.form_submit_button('Sign in',on_click=login_test,args=(username,password))

        st.markdown("Don't have an account?[sign up]()")

    if submit:
        leglly = login_test(username,password)
        if leglly:
            st.session_state['logged_in'] = True
            st.session_state['account'] = username
            # st.rerun()
        else:
            st.session_state['logged_in'] = False



def login_test(username:str|None,password:str)->bool:

    # need to add code to query sql about the account logging information and create a variable `legally` to store the legally of logging, then return the variable `legally`

    if username:
        leglly = True
    else:
        leglly = False
    if leglly:
        st.session_state['logged_in'] = True
        st.session_state['account'] = username
    else:
        pass

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False


if st.session_state['logged_in']:
    work = st.Page(main_page)
    sample_image = st.Page('image sample.py')
    pg = st.navigation([work,sample_image])
    
else:
    log_page = st.Page(login_page)
    pg = st.navigation([log_page])

pg.run()