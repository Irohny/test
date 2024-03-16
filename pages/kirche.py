import streamlit as st
from utils import get_image

def main():
    cols = st.columns([5, 1])
    cols[0].image(get_image('images/Kapelle.jpg'))

    if cols[1].button('Zurück'):
        st.switch_page('pages/atrium.py')
    
if __name__ == '__main__':
    main()