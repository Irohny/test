import streamlit as st
from utils import get_image

def main():
    cols = st.columns([5, 1])
    cols[0].image(get_image('images/Castle.jpg'))

    if cols[1].button('Wald'):
        st.switch_page('app.py')
    if cols[1].button('In die Burg'):
        st.switch_page('pages/atrium.py')

if __name__ == '__main__':
    main()