# from llm import ask
import lancedb
from services.embedder import embed
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
db = lancedb.connect("db")
sessions_table = db.open_table("personal_info")
personal_info = (
    sessions_table.search()
    .where(f"user_id = {1}")
    .limit(8)
    .to_pandas()
)
# if personal_info:
#     print("found")

tags = ['RAG', 'parsing', 'context', 'queries', 'similarity']
tag_score = []

# Precompute and reshape query tag embeddings
# embedded_tags = [np.array(embed(tag)).reshape(1, -1) for tag in tags]

print((sessions_table).to_pandas())
# for info_tags in personal_info['tags']:
#     score_value = 0
#     for info_tag in info_tags:
#         print(info_tag)
#         if info_tag in tags:
#             score_value+=1
#     tag_score.append(score_value)
# print(tag_score)
# history_prompt = (
#     sessions_table.search()
#     .where(f"user_id = {1} AND session_id = {7}")
#     .to_pandas()
# )
# print(history_prompt)
# print(sessions_table.to_pandas()['history_prompt'].iloc[2])