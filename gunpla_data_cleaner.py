import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

gundam_data = pd.read_csv("gundam_data.csv", encoding="utf-8")
gundam_data = gundam_data.drop(["Release Date", "MSRP"], axis=1)

gundam_data["Grade"] = gundam_data["Grade"].replace(
    {
        "High Grade": "HG",
        "Master Grade": "MG",
        "Real Grade": "RG",
        "Perfect Grade": "PG",
        "Advanced Grade": "AG",
        "Full Mechanics": "Full_Mechanics",
    }
)

gundam_data["Full Name"] = gundam_data["Grade"] + " " + gundam_data["Product Name"]

gundam_data["feature_combine"] = gundam_data[["First appearance", "Grade"]].apply(
    lambda row: " ".join(row.astype(str)), axis=1
)

tfidf = TfidfVectorizer(stop_words="english", ngram_range=(2, 3))
tfidf_features = tfidf.fit_transform(gundam_data["feature_combine"])
feature_names = tfidf.get_feature_names_out()

gunpla_recs = pd.DataFrame(
    tfidf_features.toarray(), index=gundam_data["Full Name"], columns=feature_names
)

cosine_sim_array = cosine_similarity(gunpla_recs)
cosine_sim_df = pd.DataFrame(cosine_sim_array, index=gunpla_recs.index)

with open("gundam_recs.pkl", "wb") as mdl:
    pickle.dump(cosine_sim_df, mdl)
