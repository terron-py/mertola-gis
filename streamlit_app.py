import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("Sobre")
st.sidebar.info(
    """
    Web App URL: <https://terron-py-mertola-gis-streamlit-app-l6gxrw.streamlitapp.com/>
    GitHub repository: <https://github.com/terron-py/mertola-gis>
    """
)

st.sidebar.title("Contacto")
st.sidebar.info(
    """
    André Sanches
    [GitHub](https://github.com/terron-py) | [LinkedIn](https://www.linkedin.com/in/andre-sanches/)
    """
)

# Customize page title
st.title("GIS do concelho de Mértola")

st.markdown(
    """
    Projecto de informação geográfica open-souce para o concelho de Mértola!
    """
)

#st.header("Instructions")

#markdown = """
#1. For the [GitHub repository](https://github.com/giswqs/streamlit-multipage-template) or [use it as a template](https://github.com/giswqs/streamlit-multipage-template/generate) for your own project.
#2. Customize the sidebar by changing the sidebar text and logo in each Python files.
#3. Find your favorite emoji from https://emojipedia.org.
#4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.

#"""

#st.markdown(markdown)

m = leafmap.Map(center=[37.64, -7.65], zoom=10.5)
m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)


