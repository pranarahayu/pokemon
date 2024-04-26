import streamlit as st
import requests
import random
import pprint as pp
import pandas as pd
from st_supabase_connection import SupabaseConnection

st.set_page_config(page_title='Match Center', layout='centered')
st.title('Guess Who? - Pokemon Edition')

conn = st.connection("supabase",type=SupabaseConnection)

with st.sidebar:
  st.header("Regenerate Pokemon")
  col1, col2 = st.columns(2)
  with col1:
    if st.button('Regenerate Pokemon'):
      idx = random.sample(range(1, 906), 30)
      data = []
      name = []
      for i in idx:
        url = "https://github.com/PokeAPI/sprites/blob/ca5a7886c10753144e6fae3b69d45a4d42a449b4/sprites/pokemon/{id}.png?raw=true"
        pokemon_id = str(i)
        response = requests.get(url.format(id=pokemon_id))
        data.append(response.content)
  
        url2 = "https://pokeapi.co/api/v2/pokemon/{}/".format(i)
        responsex = requests.get(url2)
        nama = responsex.json()
        for item in nama['forms']:
          name.append(item['name'].title())
      conn.table("temp_pokemon").insert([{"id":idx,"pokemon":name}], count="None").execute()
  with st.expander("About this app"):
    st.markdown("Guess who, but Pokemon.")
    
rose = conn.query("*", table="temp_pokemon", ttl="10m").execute()
df = pd.DataFrame(rose.data)
df = df.tail(30).reset_index(drop=True)

fixed = "https://github.com/PokeAPI/sprites/blob/ca5a7886c10753144e6fae3b69d45a4d42a449b4/sprites/pokemon/0.png?raw=true"
fixed_r = requests.get(fixed)

datas = df['id'].tolist()
names = df['pokemon'].tolist()

n_cols = 6
n_rows = 1 + len(datas) // int(n_cols)
rows = [st.container() for _ in range(n_rows)]
cols_per_row = [r.columns(n_cols) for r in rows]
cols = [column for row in cols_per_row for column in row]

for image_index, datas in enumerate(datas):
  cols[image_index].image(datas, caption=names[image_index])
