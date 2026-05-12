from data.database import get_connection

def save_plan(event_name, location, budget):
    supabase = get_connection()

    supabase.table("saved_plans").insert({
        "event_name": event_name,
        "location": location,
        "budget": budget
    }).execute()

    return True


import pandas as pd

def fetch_saved_plans():
    supabase = get_connection()

    response = supabase.table(
        "saved_plans"
    ).select("*").execute()

    return pd.DataFrame(response.data)
