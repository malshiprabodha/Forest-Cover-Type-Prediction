import streamlit as st
import pandas as pd
import joblib


model = joblib.load("forest_cover_model.pkl")

st.set_page_config(
    page_title="Forest Cover Type Prediction",
    page_icon="🌲",
    layout="centered"
)

st.title("🌲 Forest Cover Type Prediction")
st.write("Predict the forest cover type based on environmental features.")


elevation = st.number_input("Elevation", min_value=0, value=2500)
aspect = st.number_input("Aspect", min_value=0, max_value=360, value=180)
slope = st.number_input("Slope", min_value=0, max_value=90, value=10)

h_dist_hydro = st.number_input(
    "Horizontal Distance To Hydrology",
    min_value=0,
    value=100
)

v_dist_hydro = st.number_input(
    "Vertical Distance To Hydrology",
    value=0
)

h_dist_road = st.number_input(
    "Horizontal Distance To Roadways",
    min_value=0,
    value=1000
)

hillshade_9am = st.number_input(
    "Hillshade 9am",
    min_value=0,
    max_value=255,
    value=200
)

hillshade_noon = st.number_input(
    "Hillshade Noon",
    min_value=0,
    max_value=255,
    value=220
)

hillshade_3pm = st.number_input(
    "Hillshade 3pm",
    min_value=0,
    max_value=255,
    value=180
)

h_dist_fire = st.number_input(
    "Horizontal Distance To Fire Points",
    min_value=0,
    value=1000
)


wilderness_area = st.selectbox(
    "Wilderness Area",
    [1, 2, 3, 4]
)

soil_type = st.selectbox(
    "Soil Type",
    list(range(1, 41))
)

if st.button("Predict Forest Cover Type"):

    sample = {
        "Elevation": elevation,
        "Aspect": aspect,
        "Slope": slope,
        "Horizontal_Distance_To_Hydrology": h_dist_hydro,
        "Vertical_Distance_To_Hydrology": v_dist_hydro,
        "Horizontal_Distance_To_Roadways": h_dist_road,
        "Hillshade_9am": hillshade_9am,
        "Hillshade_Noon": hillshade_noon,
        "Hillshade_3pm": hillshade_3pm,
        "Horizontal_Distance_To_Fire_Points": h_dist_fire,
    }

   
    for i in range(1, 5):
        sample[f"Wilderness_Area{i}"] = 1 if i == wilderness_area else 0

    
    for i in range(1, 41):
        sample[f"Soil_Type{i}"] = 1 if i == soil_type else 0

    sample_df = pd.DataFrame([sample])

    prediction = model.predict(sample_df)[0]

    cover_types = {
        1: "Spruce/Fir",
        2: "Lodgepole Pine",
        3: "Ponderosa Pine",
        4: "Cottonwood/Willow",
        5: "Aspen",
        6: "Douglas-fir",
        7: "Krummholz"
    }

    st.success(
        f"Predicted Cover Type: {prediction} - {cover_types[prediction]}"
    )