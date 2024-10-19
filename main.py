import pandas
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle

def return_results(gundams: list[str], gundam_df):

    gundam_copy = gundam_df.copy()

    user_copy = gundam_df.loc[gundams].mean().values.reshape(1,-1)
    gundam_copy = gundam_copy.drop(gundams, axis=0)

    new_result = cosine_similarity(user_copy, gundam_copy)

    new_result_df = pd.DataFrame(new_result.T, index=gundam_copy.index, columns=['Similarity Score'])
    return new_result_df.sort_values(by='Similarity Score', ascending=False)[:10]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gundam_recs = pd.read_csv('gundam_recs.csv',index_col='title')
    print(return_results(["1/144 HG Gundam Aerial","1/144 HG Gundam Barbatos","1/144 HG G-Self (Perfect Pack Equipment Type)","1/144 RG God Gundam"], gundam_recs))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
