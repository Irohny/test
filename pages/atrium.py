import streamlit as st
from utils import get_image

def main():
    cols = st.columns([5, 1])
    cols[0].image(get_image('images/Atrium.jpg'))

    if cols[1].button('Raum 1'):
        st.switch_page('pages/festsaal.py')
    if cols[1].button('Raum 2'):
        st.switch_page('pages/libary.py')
    if cols[1].button('Raum 3'):
        st.switch_page('pages/kirche.py')
    if cols[1].button('Raum 4'):
        st.switch_page('pages/alchemie.py')
    if cols[1].button('Raum 5'):
        st.switch_page('pages/kitchen.py')

if __name__ == '__main__':
    main()