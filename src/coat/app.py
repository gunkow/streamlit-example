from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import pathlib
import sys


st.write("__file__:")
__file__
st.divider()

def add_sys_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)
"str(pathlib.Path(__file__).resolve().parent.parent.parent)"
st.write(str(pathlib.Path(__file__).resolve().parent.parent.parent))

st.divider()

add_sys_path(str(pathlib.Path(__file__).resolve().parent.parent.parent))
# add_sys_path(str(pathlib.Path().absolute()).split("/src")[0] + "/src")
# add_sys_path(str(pathlib.Path().absolute()).split("/src")[0] + "/src/mod")
# add_sys_path(str(pathlib.Path().absolute()).split("/src")[0] + "/src/coat")
# add_sys_path()

"sys path:"
st.write(sys.path)
st.divider()

# import root
# "root.sosed :"
# root.root.sosed

# import mod
# f"src.mod {mod}"
# "src.mod.mod.hi :"
# mod.mod.hi

"pew"
import src
dir(src)
st.divider()

from src import coat

import src.coat
import src.coat.coat_utils
src.coat.coat_utils.coat_util




# import src.mod
# st.write(src.mod.hi.la)

# import sosed
# sosed.sos

# import utils
# utils.utils


# with st.echo(code_location='below'):
#     total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
#     num_turns = st.slider("Number of turns in spiral", 1, 100, 9)
#     "huinia"
#     Point = namedtuple('Point', 'x y')
#     data = []

#     points_per_turn = total_points / num_turns

#     for curr_point_num in range(total_points):
#         curr_turn, i = divmod(curr_point_num, points_per_turn)
#         angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
#         radius = curr_point_num / total_points
#         x = radius * math.cos(angle)
#         y = radius * math.sin(angle)
#         data.append(Point(x, y))

#     st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
#         .mark_circle(color='#0068c9', opacity=0.5)
#         .encode(x='x:Q', y='y:Q'))
