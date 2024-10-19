import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle


@st.cache_data
def fetch_data():
    return pickle.load(open("gundam_recs.pkl", "rb"))


def return_results(gundams: list[str], gundam_df):

    gundam_copy = gundam_df.copy()

    user_copy = gundam_df.loc[gundams].mean().values.reshape(1, -1)
    gundam_copy = gundam_copy.drop(gundams, axis=0)

    new_result = cosine_similarity(user_copy, gundam_copy)

    new_result_df = pd.DataFrame(
        new_result.T, index=gundam_copy.index, columns=["Similarity Score"]
    )
    return new_result_df.sort_values(by="Similarity Score", ascending=False)[:10]


if __name__ == "__main__":
    gundam_recs = fetch_data()
    st.title("Gunpla Recommender")
    st.write(
        "Worried about which Gundam you want to buy or build. Don't worry. Here you go."
    )
    st.write(
        "Select multiple gundams, zakus or mechs of your choice and let the recommendation system do it for you."
    )
    st.write(
        "Note : This is currently a project I made for fun. More adjustments are on the way."
    )
    select_gundams = st.multiselect("Choose your gundam", gundam_recs.index)

    if st.button("Show me some Gundams"):
        selec_gundams = pd.DataFrame(return_results(select_gundams, gundam_recs))
        st.write(selec_gundams.index)
