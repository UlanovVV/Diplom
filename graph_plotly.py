import plotly.graph_objects as go
import plotly.express as px
import numpy as np
np.random.seed(1)


# Создание линейных графиков
N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 8
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 8

fig = go.Figure()
fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                    mode='lines',
                    name='Линия',
                    line=dict(color='firebrick', width=2, dash='dot')))
fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                    mode='lines+markers',
                    name='Линия и маркер',
                    line=dict(color='#B734B7', width=2, dash='dash')))
fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                    mode='markers',
                    name='Маркер'))
fig.update_layout(
    title='Линейный график',
    xaxis_title='0х',
    yaxis_title='0у',
    xaxis_tickangle=-45,
    template='plotly_white',
    margin=dict(l=40, r=40, t=60, b=40))
fig.show()


# Создание гистограммы

x0 = np.random.randn(500)
x1 = np.random.randn(500) + 1

gist = go.Figure()
gist.add_trace(go.Histogram(
    x=x0,
    histnorm='percent',
    name='date1',
    xbins=dict(
        start=-4.0,
        end=4.0,
        size=0.5
    ),
    marker_color='#EB68B5',
    opacity=0.5
))
gist.add_trace(go.Histogram(
    x=x1,
    histnorm='percent',
    name='date2',
    xbins=dict(
        start=-4.0,
        end=4,
        size=0.5
    ),
    marker_color='#330C53',
    opacity=0.5
))

gist.update_layout(
    title_text='Создание гистограммы',
    xaxis_title_text='0x',
    yaxis_title_text='0у',
    bargap=0.2,     # расстояние между столбцами в разных значениях 0х
    bargroupgap=0.1     # расстояние между столбцами в одном значении 0х
)

gist.show()


# Создание трехмерного графика

z3d = np.linspace(0, 1, 100)
x3d = z3d * np.sin(25 * z3d)
y3d = z3d * np.cos(25 * z3d)

fig3d = go.Figure(data=[go.Scatter3d(
    x=x3d,
    y=y3d,
    z=z3d,
    mode='markers',
    marker=dict(
        size=10,
        color="#30C04C",
        colorscale='Viridis',
        opacity=0.7
    )
)])
fig3d.show()

# Создание подвижных графиков

dvig = go.Figure(
    data=[go.Scatter(x=[0, 1], y=[0, 2])],
    layout=go.Layout(
        xaxis=dict(range=[0, 7], autorange=False),
        yaxis=dict(range=[0, 7], autorange=False),
        title=dict(text="Начальный заголовок"),
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Начать",
                          method="animate",
                          args=[None])])]
    ),
    frames=[go.Frame(data=[go.Scatter(x=[1, 1], y=[1, 2])]),
            go.Frame(data=[go.Scatter(x=[1, 6], y=[1, 6])]),
            go.Frame(data=[go.Scatter(x=[3, 6], y=[5, 6])],
                     layout=go.Layout(title_text="Конечный заголовок"))]
)

dvig.show()


# Создание графика с ползунком

fig = go.Figure()

# Создание графика
for step in np.arange(0, 5, 0.1):
    fig.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color="#00CED1", width=6),
            name="𝜈 = " + str(step),
            x=np.arange(0, 10, 0.01),
            y=np.sin(step * np.arange(0, 10, 0.01))))

# Отображение начального положения графика
fig.data[10].visible = True


# Создание ползунка
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "Ползунок переключился на шаг: " + str(i)}],
    )
    step["args"][0]["visible"][i] = True
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Частота: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

fig.show()