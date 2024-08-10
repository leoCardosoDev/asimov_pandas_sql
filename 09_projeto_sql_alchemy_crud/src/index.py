import streamlit as st

from crud import read_usuario

def login():
    with st.container(border=True):
        st.markdown('Bem-vindo a tela de login')

def main():
    login()

if __name__ == '__main__':
    main()
