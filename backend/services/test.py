from llm import ask
import lancedb

db = lancedb.connect("db")
sessions_table = db.open_table("sessions")

print(sessions_table.to_pandas())