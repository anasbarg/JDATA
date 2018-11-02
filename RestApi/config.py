from RestApi.Types.ChartConfig import *


range_chart = Chart(
    data_provider = "Threshold_range",
    title = "Boundaries Of Average Income",
    subtitle =  "Please Specify The Intervals",
    type = "line",
    fill_between = True,
    point_radius = 2.0,
    display_points = True,
    display_legend = True,
    animation = True,
    display_grid = True,
    labels = [1992, 2002, 2006, 2008, 2010, 2013],
    # Each Controller Should Have A Distinct Title.
    # If Two Controllers Have To Have The Same Title
    # Then Just Add An Extra Space To One Of Them. 
    controllers = ControllersList(
        Dropdown(
            title="Percentile Interval",
            label="Start",
            items=[i for i in range(0, 101)],
            label2="End",
            items2=[i for i in range(0, 101)]
        ),
        Dropdown(
            title="Year Interval",
            label="Start",
            items=[1992,2002,2006,2008,2010,2013],
            label2="End",
            items2=[1992,2002,2006,2008,2010,2013]
        ),
        header_text = "Input Controllers"
    ),
    yAxis = YAxis(min=0, scale_label="Average Yearly Income", label_color="rgb(90, 20, 255)", label_size=12),
    xAxis = XAxis(scale_label="Average Yearly Income", label_color="rgb(90, 20, 255)", label_size=12),
    datasets = [
        Dataset(
            dataset_id = "min",
            label = "Minimmum",
            color = "rgb(90, 30, 255)",
            border_width = 1.0,
            fill = False,
            tension = 1.0
        ),
        Dataset(
            dataset_id = "max",
            label = "Maximum",
            color = "rgb(90, 20, 255)",
            border_width = 1.0,
            fill = False,
            tension = 1.0
        )
    ]
)


dist_chart = Chart(
    data_provider = "dist",
    title = "Distribution",
    subtitle =  "Please Specify The Intervals",
    type = "line",
    fill_between = False,
    point_radius = 2.0,
    display_points = True,
    display_legend = True,
    animation = True,
    display_grid = True,
    labels = [1992, 2002, 2006, 2008, 2010, 2013],
    # Each Controller Should Have A Distinct Title.
    # If Two Controllers Have To Have The Same Title
    # Then Just Add An Extra Space To One Of Them. 
    controllers = ControllersList(
        Dropdown(
            title="Year Interval",
            label="Start",
            items=[1992,2002,2006,2008,2010,2013],
            label2="End",
            items2=[1992,2002,2006,2008,2010,2013]
        ),
        header_text = "Input"
    ),
    yAxis = YAxis(min=0, scale_label="Average Yearly Income", label_color="rgb(90, 20, 255)"),
    xAxis = XAxis(scale_label="Average Yearly Income", label_color="rgb(90, 20, 255)", type="linear"),
    datasets = [
        Dataset(
            dataset_id = "dist",
            label = "Distribution",
            color = "rgb(90, 30, 255)",
            border_width = 1.0,
            fill = True,
            tension = 1.0
        )
    ]
)

chart_config = ChartConfig(
    range_chart,
    dist_chart
)

import json
print(json.dumps(chart_config.to_dict()))