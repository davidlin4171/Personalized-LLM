
import lancedb
from sentence_transformers import SentenceTransformer
import numpy as np

#uri = "mongodb+srv://wko21:uc17hzSAgrHNAsgP@personalized-llm.ziratuz.mongodb.net/?retryWrites=true&w=majority&appName=Personalized-LLM"

# Create a new client and connect to the server
#client = MongoClient(uri, server_api=ServerApi('1'))
#db = client["test_database"]
'''
Structure - 1 table for storing session/conversation history, 1 table for personal info
Table: Sessions
    Column: session_id -> int
    Column: user_id -> int?
    Column: prompt and answer -> text

Table: Personal Info
    Column: user_id -> int?
    Column: info_chunk -> text
    Column: info_chunk_embedding -> vector embedding
'''
embedder = SentenceTransformer("all-MiniLM-L6-v2")
db = lancedb.connect("db")

#def save_profile_data(profile):
#    user_id = profile.get("id")
    #collection = db[user_id]
#    old_user = collection.find_one({"personal_info.id": user_id})
#    wrapped_profile = {"personal_info": profile}
#    if not old_user:
#        collection.insert_one(wrapped_profile)
#        return "inserted"
#    else:
#        collection.update_one({"personal_info.id": user_id}, {"$set": wrapped_profile})
#        return "updated"

def save_user_data(data, user_id):
    personal_table = db.open_table("personal_info")
    interests = data.get("interests", [])
    interests_str = ", ".join(interests)
    data_text = f"{data.get('name', '')}, {data.get('email', '')}, {data.get('gender', '')}, {data.get('location', '')}, {data.get('occupation', '')}, {interests_str}"
    embedding = embedder.encode(data_text, convert_to_tensor=True).tolist()
    rows = personal_table.to_pandas()
    new_record = {
        "user_id": user_id,
        "info_chunk": data_text,
        "info_chunk_embedding": embedding
    }
    personal_table.add([new_record])
    status = "success"
    return status

def save_answer_data(data, user_id):
    personal_table = db.open_table("personal_info")
    answer_data = data.get("answer")
    embedding = embedder.encode(answer_data, convert_to_tensor=True).tolist()
    rows = personal_table.to_pandas()
    new_record = {
        "user_id": user_id,
        "info_chunk": answer_data,
        "info_chunk_embedding": embedding
    }
    personal_table.add([new_record])
    status = "success"
    return status




try:
    # example data
    example_sessions = [
        {
            "session_id": 1,
            "user_id": 1, 
            "prompt_answer": "Q: Who invented the plane? A: The Wright Brothers \n Q: When was it invented? A: 1903"
        },
        {
            "session_id": 2,
            "user_id": 1, 
            "prompt_answer": "Q: When was 9/11 A: September 11, 2001 \n Q: Who did it? A: Bush"
        }
    ]
    example_personal_info = [
        {
            "user_id": 1,
            "info_chunk": "user is interested in planes",
            "vector": embedder.encode("user is interested in planes", convert_to_tensor=True).tolist()
        }
    ]
    # setup tables
    #if "sessions" not in db.table_names():
    #    session_table = db.create_table("sessions", data=example_sessions)
    #else:
    #    session_table = db.open_table("sessions")
    #    session_table.add(example_sessions)


    #if "personal_info" not in db.table_names():
    #    personal_table = db.create_table("personal_info", data=example_personal_info)
    #else:
    #    personal_table = db.open_table("personal_info")
    #    personal_table.add(example_personal_info)
    #print("Tables in DB:", db.table_names())
    for table_name in db.table_names():
         table = db.open_table(table_name)
         print(f"\n--- Contents of table: {table_name} ---")
         print(table.to_pandas())
    #for table_name in db.table_names():
    #    table = db.open_table(table_name)
    #    table.delete(where="true")

    
except Exception as e:
    print(e)