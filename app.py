import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import re
import numpy as np
import requests
from PIL import Image


@st.cache_data
def fetch_data():
    return pickle.load(open(r"data/gundam_recs.pkl", "rb"))


def return_results(gundams: list[str], gundam_df):

    gundam_copy = gundam_df.copy()
    similarities = []
    # gundam_copy = gundam_copy.drop(gundams, axis=0)

    for gundam in gundams:
        user_gundams = gundam_df.loc[gundam].values.reshape(1, -1)
        gundam_removed = gundam_copy.drop(gundam, axis=0)
        sim = cosine_similarity(user_gundams, gundam_removed)
        similarities.append(sim)

    avg_sim = np.mean(similarities, axis=0)

    gundam_copy = gundam_copy.drop(gundam, axis=0)

    new_result_df = pd.DataFrame(
        avg_sim.T,
        index=gundam_copy.index,
        columns=["Similarity Score"],
    )

    return new_result_df.sort_values(by="Similarity Score", ascending=False)[:10]


# def create_layout(name_image):
#     for i, col in enumerate(row1 + row2):

#         tile = col.container(height=400)
#         tile.markdown(name_image["full_name"][i][0])

#         text_img = re.sub(r"\/revision.*", "", name_image["image_link"][i][0])
#         if name_image["image_link"][i][0] is None:
#             st.image("")
#         else:
#             im = Image.open(requests.get(text_img, stream=True).raw)
#             tile.image(im, output_format="png", width=300)

#     return tile


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    gundam_recs = fetch_data()
    gundam_data = pd.read_csv("data/gundam_data_2.csv", index_col="id")
    st.title("Gunpla Recommender")
    st.write(
        "Having to decide which gunpla model can be tough, especially with thousands of variations of the same model. So, I created this website to help people to decide their next gundam model kit to work on, based on their available or soon-to-be available kit."
    )
    st.write(
        "Select or type your existing gunpla model kit you currently have or will have, press the button and get top 6 recommendations that follow"
    )
    st.write("Note : This is a project I made for fun and for non-profit use.")
    selected_gundams = st.multiselect("Choose your gundam", gundam_data.full_name)

    if st.button("Show me some Gundams"):
        select_gundams = pd.DataFrame(return_results(selected_gundams, gundam_recs))

        select_gundam_img = gundam_data[
            gundam_data["full_name"].isin(select_gundams.index)
        ]
        select_gundam_img = select_gundam_img.drop("Unnamed: 0", axis=1)

        row1 = st.columns(3)
        row2 = st.columns(3)

        name_image = {}
        images = []

        name_image["full_name"] = select_gundam_img[["full_name"]].values
        name_image["image_link"] = select_gundam_img[["image_link"]].values

        for i, col in enumerate(row1 + row2):

            tile = col.container(height=400)
            tile.markdown(name_image["full_name"][i][0])

            if name_image["image_link"][i][0] is np.nan:
                im = Image.open("data/error.png")
                tile.image(im, output_format="png", width=350)
            else:
                text_img = re.sub(r"\/revision.*", "", name_image["image_link"][i][0])
                im = Image.open(requests.get(text_img, stream=True).raw)
                tile.image(im, output_format="jpg", width=350)
