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
    sliders = [
        Slider(label="Years Interval", type="RangeYearSlider", pips=[1992, 2002, 2006, 2008, 2010, 2013]),
        Slider(label="Percentage Interval", type="RangePercentageSlider")
    ],
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