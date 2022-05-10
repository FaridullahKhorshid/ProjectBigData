import streamlit as st
import navigation

# setup broweser tab title
st.set_page_config(page_title="Big Data", layout="wide")

# add css to document
st.markdown(
    """ 
    <style>
        .block-container {padding-bottom:1rem; }
        iframe[title="streamlit_option_menu.option_menu"] {position:fixed; top:0;right: 0;left: 0;width: 100%;z-index:9999999;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style> """,
    unsafe_allow_html=True,
)

# load navigation options and content
navigation.load()


# from db import connection
# if connection.is_connected():
#     cursor = connection.cursor()
#     cursor.execute("select database();")
#     print("You're connected to database in main: ", cursor.fetchone())


# dit hebben we niet meer nodig

# # 2. horizontal menu with custom style
# selected = option_menu(
#     menu_title=None,  # required
#     options=["Home", "Prediction", "Contact"],  # required
#     icons=["house", "book", "envelope"],  # optional
#     menu_icon="cast",  # optional
#     orientation="horizontal",
#     styles={
#         "container": {"padding": "0 !important", "margin": "0", "max-width": "100%", "border-radius": "0"},
#         "icon": {"color": "orange", "font-size": "25px"},
#         "nav-item": {
#             "flex-grow": "unset",
#             "flex-basis": "unset",
#         },
#         "nav-link": {
#             "font-size": "25px",
#             "text-align": "left",
#             "margin": "0px",
#             # "--hover-color": "#eee",
#         },
#         "nav-link-selected": {"background-color": "#073045"},
#     },
# )

# header = st.container()
# dataset = st.container()

# amsterdam_data = pd.read_csv("data/h-amsterdam.csv")
# map_data = amsterdam_data

# # with header:
# #     st.title("Hallo Big Data")
# # selected1 = nav.streamlit_menu(example=2)
# # selected2 = nav.streamlit_menu(example=3)

# if selected == "Home":
#     # home.load_view()
#     st.title(f"You have selected {selected}")
#     map_data.rename(columns={"Lat": "lat", "Lon": "lon"}, inplace=True)

#     st.map(map_data)
# if selected == "Prediction":
#     prediction.load_view()
#     # st.title(f"You have selected {selected}")
#     # ch_data = amsterdam_data
#     # # ch_data["PriceRoom"] = ch_data["Price"] / 100 / ch_data["Room"]

#     # chart_data = pd.DataFrame(amsterdam_data, columns=["Price", "Room"])

#     # st.line_chart(chart_data)

# if selected == "Contact":
#     st.title(f"You have selected {selected}")


# with dataset:
#     st.write(amsterdam_data.head(100))


# map = folium.Map(
#     location=[
#         map_data.lat.mean(),
#         map_data.lon.mean(),
#     ],
#     zoom_start=14,
#     control_scale=True,
# )

# m = folium.Map(
#     location=[45.523, -122.675],
#     zoom_start=2,
#     tiles="https://api.mapbox.com/v4/mapbox.streets/{z}/{x}/{y}.png?access_token=mytoken",
#     attr="Mapbox attribution",
# )

# st.write(m)


# map.Choropleth(name="test", data=map_data)
