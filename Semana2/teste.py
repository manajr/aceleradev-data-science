import streamlit as st
import pandas as import import pd

def main():
    st.title('Hello World')
    # st.header('This is a header')
    # st.subheader('This is a sub header')
    # st.text('This is a text')
    # #st.image('/data.jpg')
    # #st.audio()
    # #st.video()
    st.markdown("Botão")
    botao = st.button('Botão')
    if botao:
        st.markdown('Clicado')
    check_box = st.checkbox('Checkbox')
    if check_box:
        st.markdown('Clicado')
    radio = st.radio("Escolha as opções", ('Opt 1', 'Opt 2'))
    if radio == 'Opt 1':
        st.markdown('Opt 1')
    if radio == 'Opt 2':
        st.markdown('Opt 2')
    select = st.selectbox('Choose opt', ('Opt 1 ', 'Opt 2'))
    if select == 'Opt 1':
        st.markdown('Opt 1')
    if select == 'Opt 2':
        st.markdown('Opt 2')
    
    multi = st.multiselect('Choose :', ('Opt 1', 'Opt 2'))
    if multi == 'Opt 1':
        st.markdown('Opt 1')
    if multi == 'Opt 2':
        st.markdown('Opt 2')

    files = st.file_uploader("Choose your FILES: ", type = 'csv')
    if files is not None:
        st.markdown('Files é vazio')

if __name__ == '__main__':
    main()

