import streamlit as st
import requests
import random

st.set_page_config(page_title='Match Center', layout='centered')
st.markdown('# Guess Who? - Pokemon Edition')

idx = random.sample(range(1, 1026), 25)

'''
for col in row1 + row2 + row3 + row4 + row5 + row6:
    tile = col.container(height=100)
    for i in idx:
        url = "https://github.com/PokeAPI/sprites/blob/ca5a7886c10753144e6fae3b69d45a4d42a449b4/sprites/pokemon/{id}.png?raw=true"
        pokemon_id = str(i)
        response = requests.get(url.format(id=pokemon_id))
    tile.image(response.content)
for i in idx:
    url = "https://github.com/PokeAPI/sprites/blob/ca5a7886c10753144e6fae3b69d45a4d42a449b4/sprites/pokemon/{id}.png?raw=true"
    pokemon_id = str(i)
    response = requests.get(url.format(id=pokemon_id))
    for col in row1 + row2 + row3 + row4 + row5:
        tile = col.container(border=True)
        tile.image(response.content)
'''
n_cols = 5
data = []
for i in idx:
  url = "https://github.com/PokeAPI/sprites/blob/ca5a7886c10753144e6fae3b69d45a4d42a449b4/sprites/pokemon/{id}.png?raw=true"
  pokemon_id = str(i)

  response = requests.get(url.format(id=pokemon_id))
  data.append(response.content)

n_rows = 1 + len(data) // int(n_cols)
rows = [st.container() for _ in range(n_rows)]
cols_per_row = [r.columns(n_cols) for r in rows]
cols = [column for row in cols_per_row for column in row]

for image_index, data in enumerate(data):
    cols[image_index].image(data)
