from supabase import create_client
from dotenv import load_dotenv
from datetime import timedelta, datetime, timezone
from live import predict
import os

load_dotenv()

db = create_client(os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_KEY"))

def save_prediction(city, prediction):
    date_pred = datetime.now(timezone(timedelta(hours=-3))) + timedelta(hours=24)
    new_row = {"ciudad": city, "temp_pred": prediction, "fecha_pred": date_pred.isoformat()}
    return db.table("predicciones").insert(new_row).execute()

def get_last_prediction(city):
    res = db.table("predicciones").select("*").eq("ciudad", city).order("id", desc=True).limit(1).execute()
    return None if not res.data else res.data[0]
