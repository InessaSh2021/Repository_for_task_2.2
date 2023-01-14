# Визуализация модели .STL
import numpy
import stl
import plotly
import numpy as np
import plotly.graph_objects as go
import urllib
from stl import mesh

!wget
https: // lotus1.org / content / blocks / files / sthe_stl_model_22606154.stl

my_mesh = mesh.Mesh.from_file('sthe_stl_model_22606154.stl')


def stl2mesh3d(stl_mesh):
    p, q, r = stl_mesh.vectors.shape  # (p, 3, 3)
    vertices, ixr = np.unique(stl_mesh.vectors.reshape(p * q, r), return_inverse=True, axis=0)

    I = np.take(ixr, [3 * k for k in range(p)])
    J = np.take(ixr, [3 * k + 1 for k in range(p)])
    K = np.take(ixr, [3 * k + 2 for k in range(p)])

    return vertices, I, J, K


title = "Mesh3d LOTUS STHE"
layout = go.Layout(paper_bgcolor='rgb(1,1,1)',
                   title_text=title, title_x=0.5,
                   font_color='white',
                   width=800,
                   height=800,
                   scene_camera=dict(eye=dict(x=1.25, y=-1.25, z=1)),
                   scene_xaxis_visible=False,
                   scene_yaxis_visible=False,
                   scene_zaxis_visible=False)

vertices, I, J, K = stl2mesh3d(my_mesh)
x, y, z = vertices.T
colorscale = [[0, '#555555'], [1, '#e5dee5']]
mesh3D = go.Mesh3d(
    x=x,
    y=y,
    z=z,
    i=I,
    j=J,
    k=K,
    flatshading=True,
    colorscale=colorscale,
    intensity=z,
    name='LOTUS STHE',
    showscale=False)
fig = go.Figure(data=[mesh3D], layout=layout)

fig.show()