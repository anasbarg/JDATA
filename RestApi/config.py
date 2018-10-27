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
        Slider(title="Percentage Interval", type="RangePercentageSlider"),
        Dropdown(
            title="Year Interval",
            label="Start",
            items=[1992,2002,2006,2008,2010,2013],
            label2="End",
            items2=[1992,2002,2006,2008,2010,2013]
        ),
        header_text = "Input"
    ),
    yAxis = Axis(min=0, max=1, scale_label="Average Yearly Income", label_color="rgb(90, 20, 255)"),
    xAxis = Axis(scale_label="Average Yearly Income", label_color="rgb(90, 20, 255)"),
    datasets = [
        Dataset(
            dataset_id = "min",
            label = "A label",
            color = "rgb(90, 30, 255)",
            border_width = 1.0,
            fill = False,
            tension = 1.0
        ),
        Dataset(
            dataset_id = "max",
            label = "A label",
            color = "rgb(90, 20, 255)",
            border_width = 1.0,
            fill = False,
            tension = 1.0
        )
    ]
)


chart_config = ChartConfig(
    range_chart
)