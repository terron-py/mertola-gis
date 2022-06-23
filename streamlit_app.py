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
    André Sanches: <https://wetlands.io>
    [GitHub](https://github.com/terron-py) | [LinkedIn](https://www.linkedin.com/in/andre-sanches/)
    """
)

# Customize page title
st.title("Streamlit for Geospatial Applications")

st.markdown(
    """
    This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://github.com/giswqs/streamlit-multipage-template).
    """
)

st.header("Instructions")

markdown = """
1. For the [GitHub repository](https://github.com/giswqs/streamlit-multipage-template) or [use it as a template](https://github.com/giswqs/streamlit-multipage-template/generate) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
