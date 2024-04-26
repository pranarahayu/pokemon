import streamlit as st
import requests
import random
import pprint as pp

st.set_page_config(page_title='Match Center', layout='centered')
st.title('Guess Who? - Pokemon Edition')

with st.sidebar:
  st.header("Regenerate Pokemon")
  with st.expander("About this app"):
    st.markdown("Guess who, but Pokemon.")

idx = random.sample(range(1, 906), 30)

n_cols = 6
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

n_rows = 1 + len(data) // int(n_cols)
rows = [st.container() for _ in range(n_rows)]
cols_per_row = [r.columns(n_cols) for r in rows]
cols = [column for row in cols_per_row for column in row]

for image_index, data in enumerate(data):
  cols[image_index].image(data, caption=name[image_index])
