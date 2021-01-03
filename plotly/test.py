import plotly.graph_objs as go
import random

f = go.FigureWidget()
f.layout.hovermode = 'closest'
f.layout.hoverdistance = -1 #ensures no "gaps" for selecting sparse data
default_linewidth = 2
highlighted_linewidth_delta = 2

# just some traces with random data points  
num_of_traces = 5
random.seed = 42
for i in range(num_of_traces):
    y = [random.random() + i / 2 for _ in range(100)]
    trace = go.Scatter(y=y, mode='lines', line={ 'width': default_linewidth })
    f.add_trace(trace)

# our custom event handler
def update_trace(trace, points, selector):
    # this list stores the points which were clicked on
    # in all but one trace they are empty
    if len(points.point_inds) == 0:
        return
        
    for i,_ in enumerate(f.data):
        f.data[i]['line']['width'] = default_linewidth + highlighted_linewidth_delta * (i == points.trace_index)


# we need to add the on_click event to each trace separately       
for i in range( len(f.data) ):
    f.data[i].on_click(update_trace)

# let's show the figure 
f.show()