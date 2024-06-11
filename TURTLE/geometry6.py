import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Sample data (replace with actual monthly historical data)
elon_musk_net_worths = [50_000_000, 55_000_000, 60_000_000, ...,]  # Add actual values
mark_zuckerberg_net_worths = [30_000_000, 35_000_000, 40_000_000, ...,]  # Add actual values

# Assuming data is monthly from 2010 to 2018
months = pd.date_range(start="2010-01-01", end="2018-12-01", freq="M")[:len(elon_musk_net_worths)]

# Create a DataFrame
data = {'Month': months, 'Elon Musk': elon_musk_net_worths, 'Mark Zuckerberg': mark_zuckerberg_net_worths}
df = pd.DataFrame(data)

# Create subplot
fig = make_subplots(rows=2, cols=1, subplot_titles=['Elon Musk Net Worth', 'Mark Zuckerberg Net Worth'])

# Add traces
trace1 = go.Scatter(x=df['Month'], y=df['Elon Musk'], mode='lines+markers', name='Elon Musk', line=dict(color='blue'))
trace2 = go.Scatter(x=df['Month'], y=df['Mark Zuckerberg'], mode='lines+markers', name='Mark Zuckerberg', line=dict(color='green'))

fig.add_trace(trace1, row=1, col=1)
fig.add_trace(trace2, row=2, col=1)

# Update layout
fig.update_layout(title_text='Net Worth Comparison: Elon Musk vs Mark Zuckerberg',
                  xaxis=dict(title='Month'),
                  yaxis=dict(title='Net Worth (in billions)'),
                  showlegend=True)

# Update frames for animation
frames = [go.Frame(data=[go.Scatter(x=df['Month'][:i+1], y=df['Elon Musk'][:i+1], mode='lines+markers',
                                   line=dict(color='blue')),
                         go.Scatter(x=df['Month'][:i+1], y=df['Mark Zuckerberg'][:i+1], mode='lines+markers',
                                   line=dict(color='green'))],
                   traces=[0, 1]) for i in range(1, len(df))]

# Add frames to the animation
fig.frames = frames

# Show the animated chart
fig.show()
