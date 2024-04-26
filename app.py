import streamlit as st
import requests
import random
import pprint as pp
import pandas as pd
from st_supabase_connection import SupabaseConnection
from PIL import Image

st.set_page_config(page_title='Home Page', layout='centered')
st.title('Guess Who? - Pokemon Edition')

conn = st.connection("supabase",type=SupabaseConnection)

col1, col2, col3 = st.columns(3)
with col2:
  if st.button('Re-Generate Pokemon'):
    idx = random.sample(range(1, 906), 30)
    name = []
    for i in idx:
      url2 = "https://pokeapi.co/api/v2/pokemon/{}/".format(i)
      responsex = requests.get(url2)
      nama = responsex.json()
      name.append(nama['name'].title())
    for j, k in zip(idx, name):
      conn.table("temp_pokemon").insert([{"id":j,"pokemon":k}], count="None").execute()
    
rose = conn.query("*", table="temp_pokemon", ttl="10m").execute()
df = pd.DataFrame(rose.data)
df = df.tail(30).reset_index(drop=True)

names = df['pokemon'].tolist()
datas = df['id'].tolist()
data = []
for i in datas:
  url = "https://github.com/PokeAPI/sprites/blob/ca5a7886c10753144e6fae3b69d45a4d42a449b4/sprites/pokemon/{id}.png?raw=true"
  pokemon_id = str(i)
  response = requests.get(url.format(id=pokemon_id))
  data.append(response.content)

n_cols = 6
n_rows = 1 + len(data) // int(n_cols)
rows = [st.container() for _ in range(n_rows)]
cols_per_row = [r.columns(n_cols) for r in rows]
cols = [column for row in cols_per_row for column in row]

for image_index, data in enumerate(data):
  cols[image_index].image(data, caption=names[image_index])

with st.expander("About this app"):
  st.markdown("Guess who, but Pokemon.")
