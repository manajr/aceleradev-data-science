import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns

def criar_Outro(coluna, df, sliderH):
    #codigo TODO
    pass

def criar_histograma(coluna, df, sliderH):
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X(coluna,bin=alt.Bin(base = sliderH, extent=[1,40000])),
        y='count()', tooltip=[coluna, 'count()']
    ).properties(width=600, height=600).interactive()
    return chart

def criar_barras(coluna_num, coluna_cat, df):
    bars = alt.Chart(df, width = 600).mark_bar().encode(
        x=alt.X(coluna_num, stack='zero'),
        y=alt.Y(coluna_cat),
        tooltip=[coluna_cat, coluna_num]
    ).interactive()
    return bars

def criar_boxplot(coluna_num, coluna_cat, df):
    boxplot = alt.Chart(df).mark_boxplot().encode(
        x=coluna_num,
        y=coluna_cat
    ).properties(width=600,height=600)
    return boxplot

def criar_scatterplot(x, y, color, df):
    scatter = alt.Chart(df, width=800, height=400).mark_circle().encode(
        alt.X(x),
        alt.Y(y),
        color = color,
        tooltip = [x, y]
    ).interactive()
    return scatter

def cria_correlationplot(df, colunas_numericas):
    cor_data = (df[colunas_numericas]).corr().stack().reset_index().rename(columns={0: 'correlation', 'level_0': 'variable', 'level_1': 'variable2'})
    cor_data['correlation_label'] = cor_data['correlation'].map('{:.2f}'.format)  # Round to 2 decimal
    base = alt.Chart(cor_data, width=500, height=500).encode( x = 'variable2:O', y = 'variable:O')
    text = base.mark_text().encode(text = 'correlation_label',color = alt.condition(alt.datum.correlation > 0.5,alt.value('white'),
    alt.value('black')))

# The correlation heatmap itself
    cor_plot = base.mark_rect().encode(
    color = 'correlation:Q')

    return cor_plot + text


def main():
    #st.image('logo.png', width=200)
    st.title('AceleraDev Data Science')
    st.subheader('Semana 3 - Análise de dados exploratória')
    st.image('https://media.giphy.com/media/R8bcfuGTZONyw/giphy.gif', width=200)
    file  = st.file_uploader('Escolha a base de dados que deseja analisar (.csv)', type = 'csv')
    if file is not None:
        st.subheader('Estatística descritiva univariada')
        df = pd.read_csv(file)
        aux = pd.DataFrame({"colunas": df.columns, 'tipos': df.dtypes})
        colunas_numericas = list(aux[aux['tipos'] != 'object']['colunas'])
        colunas_object = list(aux[aux['tipos'] == 'object']['colunas'])
        colunas = list(df.columns)
        col = st.selectbox('Selecione a coluna :', colunas_numericas)
        if col is not None:
            st.markdown('Selecione o que deseja analisar :')
            mean = st.checkbox('Média')
            if mean:
                st.markdown(df[col].mean())
            median = st.checkbox('Mediana')
            if median:
                st.markdown(df[col].median())
            desvio_pad = st.checkbox('Desvio padrão')
            if desvio_pad:
                st.markdown(df[col].std())
            kurtosis = st.checkbox('Kurtosis')
            if kurtosis:
                st.markdown(df[col].kurtosis())
            skewness = st.checkbox('Skewness')
            if skewness:
                st.markdown(df[col].skew())
            describe = st.checkbox('Describe')
            if describe:
                st.table(df[colunas_numericas].describe().transpose())
        st.subheader('Visualização dos dados')
        st.image('https://media.giphy.com/media/Rkoat5KMaw2aOHDduz/giphy.gif', width=200)
        st.markdown('Selecione a visualizacao')
        histograma = st.checkbox('Histograma')
        if histograma:
            col_num = st.selectbox('Selecione a Coluna Numerica: ', colunas_numericas,key = 'unique')
            sliderH = st.slider('Bin' ,min_value = 1, max_value = 10)
            st.markdown('Histograma da coluna : ' + str(col_num) + str(type(col_num))+str(df[col_num].count()))
            st.write(criar_histograma(col_num, df,sliderH))
        barras = st.checkbox('Gráfico de barras')
        if barras:
            col_num_barras = st.selectbox('Selecione a coluna numerica: ', colunas_numericas, key = 'unique')
            col_cat_barras = st.selectbox('Selecione uma coluna categorica : ', colunas_object, key = 'unique')
            st.markdown('Gráfico de barras da coluna ' + str(col_cat_barras) + ' pela coluna ' + col_num_barras)
            st.write(criar_barras(col_num_barras, col_cat_barras, df))
        boxplot = st.checkbox('Boxplot')
        if boxplot:
            col_num_box = st.selectbox('Selecione a Coluna Numerica:', colunas_numericas,key = 'unique' )
            col_cat_box = st.selectbox('Selecione uma coluna categorica : ', colunas_object, key = 'unique2')
            st.markdown('Boxplot ' + str(col_cat_box) + ' pela coluna ' + col_num_box)
            st.write(criar_boxplot(col_num_box, col_cat_box, df))
        scatter = st.checkbox('Scatterplot')
        if scatter:
            col_num_x = st.selectbox('Selecione o valor de x ', colunas_numericas, key = 'unique')
            col_num_y = st.selectbox('Selecione o valor de y ', colunas_numericas, key = 'unique')
            col_color = st.selectbox('Selecione a coluna para cor', colunas)
            st.markdown('Selecione os valores de x e y')
            st.write(criar_scatterplot(col_num_x, col_num_y, col_color, df))
        correlacao = st.checkbox('Correlacao')
        if correlacao:
            st.markdown('Gráfico de correlação das colunas númericas')
            st.write(cria_correlationplot(df, colunas_numericas))


if __name__ == '__main__':
    main()
