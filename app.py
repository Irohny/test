import streamlit as st
import matplotlib.pyplot as plt
from utils import get_image

def main():
    st.set_page_config('SplittermondStreamlit', layout='wide')
    cols = st.columns([5,1])
    cols[0].image('images/Intro.jpg')

    if cols[1].button(f'{"Weg Nord West":<30}'):
        st.switch_page('pages/castle.py')
    
    if cols[1].button(f'{"Weg Süden":<30}'):
        st.switch_page('pages/castle.py')

    if cols[1].button(f'{"Weg Nord Ost":<30}'):
        st.switch_page('pages/castle.py')

if __name__ == '__main__':
    main()