from json import dumps
from RestApi.Types.ChartConfig import *


dist_chart = Chart(
    data_provider="dist",
    title="Income Distribution",
    subtitle="",
    type="line",
    fill_between=False,
    point_radius=2.0,
    display_points=False,
    display_legend=False,
    animation=True,
    display_grid=True,
    labels=[0, 1, 2, 3, 4, 5, 6],
    # Each Controller Should Have A Distinct Title.
    # If Two Controllers Have To Have The Same Title
    # Then Just Add An Extra Space To One Of Them.
    controllers=ControllersList(
        Dropdown(
            type="year",
            title="Year",
            label="",
            items=[1992, 2002, 2006, 2008, 2010, 2013],
        ),
        header_text="Input"
    ),
    yAxis=YAxis(min=0, scale_label="Probability",
                label_color="rgb(90, 20, 255)", label_size=12),
    xAxis=XAxis(scale_label="Monthly income (logarithmic scale: 3 means 1000 JD)",
                label_color="rgb(90, 20, 255)", label_size=15, type="linear"),
    datasets=[
        Dataset(
            dataset_id="dist",
            label="Distribution",
            color="rgb(90, 20, 255)",
            border_width=1.0,
            fill=True,
            tension=1.0
        )
    ]
)

range_chart = Chart(
    data_provider="range",
    title="Thrshold",
    subtitle="",
    type="line",
    fill_between=True,
    point_radius=2.0,
    display_points=True,
    display_legend=False,
    animation=True,
    display_grid=True,
    labels=[1992, 2002, 2006, 2008, 2010, 2013],
    # Each Controller Should Have A Distinct Title.
    # If Two Controllers Have To Have The Same Title
    # Then Just Add An Extra Space To One Of Them.
    controllers=ControllersList(
        Dropdown(
            type="percentile",
            title="Percentile Interval",
            label="Start",
            items=[i for i in range(0, 99)]+[99, 99.1, 99.2, 99.3, 99.4, 99.5,99.6,99.7,99.8,99.9,99.91,99.92,99.93,99.94,99.95,99.96,99.97,99.98,99.99,99.991,99.992,99.993,99.994,99.995,99.996,99.997,99.998,99.999,100],
            label2="End",
            items2=[i for i in range(0, 99)]+[99, 99.1, 99.2, 99.3, 99.4, 99.5,99.6,99.7,99.8,99.9,99.91,99.92,99.93,99.94,99.95,99.96,99.97,99.98,99.99,99.991,99.992,99.993,99.994,99.995,99.996,99.997,99.998,99.999,100]
        ),
        Dropdown(
            type="year",
            title="Year",
            label="from",
            items=[1992, 2002, 2006, 2008, 2010, 2013],
            label2="to",
            items2=[1992, 2002, 2006, 2008, 2010, 2013]
        ),
        header_text="Input"
    ),
    yAxis=YAxis(min=0, scale_label="Yearly income [JD]",
                label_color="rgb(90, 20, 255)", label_size=12),
    xAxis=XAxis(scale_label="",
                label_color="rgb(90, 20, 255)", label_size=15),
    datasets=[
        Dataset(
            dataset_id="min",
            label="Minimmum",
            color="rgb(90, 30, 255)",
            border_width=1.0,
            fill=False,
            tension=1.0
        ),
        Dataset(
            dataset_id="max",
            label="Maximum",
            color="rgb(90, 20, 255)",
            border_width=1.0,
            fill=False,
            tension=1.0
        )
    ]
)

average_chart = Chart(
    data_provider="average",
    title="Average Income",
    subtitle="",
    type="line",
    fill_between=True,
    point_radius=2.0,
    display_points=True,
    display_legend=False,
    animation=True,
    display_grid=True,
    labels=[1992, 2002, 2006, 2008, 2010, 2013],
    # Each Controller Should Have A Distinct Title.
    # If Two Controllers Have To Have The Same Title
    # Then Just Add An Extra Space To One Of Them.
    controllers=ControllersList(
        Dropdown(
            type="percentile",
            title="Percentile",
            label="Start",
            items=[i for i in range(0, 99)]+[99, 99.1, 99.2, 99.3, 99.4, 99.5,99.6,99.7,99.8,99.9,99.91,99.92,99.93,99.94,99.95,99.96,99.97,99.98,99.99,99.991,99.992,99.993,99.994,99.995,99.996,99.997,99.998,99.999,100],
            label2="End",
            items2=[i for i in range(0, 99)]+[99, 99.1, 99.2, 99.3, 99.4, 99.5,99.6,99.7,99.8,99.9,99.91,99.92,99.93,99.94,99.95,99.96,99.97,99.98,99.99,99.991,99.992,99.993,99.994,99.995,99.996,99.997,99.998,99.999,100]
        ),
        Dropdown(
            type="year",
            title="Year",
            label="from",
            items=[1992, 2002, 2006, 2008, 2010, 2013],
            label2="to",
            items2=[1992, 2002, 2006, 2008, 2010, 2013]
        ),
        header_text="Input"
    ),
    yAxis=YAxis(min=0, scale_label="Yearly income [JD]",
                label_color="rgb(90, 20, 255)", label_size=12),
    xAxis=XAxis(scale_label="",
                label_color="rgb(90, 20, 255)", label_size=15),
    datasets=[
        Dataset(
            dataset_id="min",
            label="Minimmum",
            color="rgb(90, 30, 255)",
            border_width=1.0,
            fill=False,
            tension=1.0
        ),
        Dataset(
            dataset_id="max",
            label="Maximum",
            color="rgb(90, 20, 255)",
            border_width=1.0,
            fill=False,
            tension=1.0
        )
    ]
)

share_chart = Chart(
    data_provider="share",
    title="Share",
    subtitle="",
    type="line",
    fill_between=False,
    point_radius=2.0,
    display_points=True,
    display_legend=False,
    animation=True,
    display_grid=True,
    labels=[1992, 2002, 2006, 2008, 2010, 2013],
    # Each Controller Should Have A Distinct Title.
    # If Two Controllers Have To Have The Same Title
    # Then Just Add An Extra Space To One Of Them.
    controllers=ControllersList(
        Dropdown(
            type="percentile",
            title="Percentile",
            label="Start",
            items=[i for i in range(0, 99)]+[99, 99.1, 99.2, 99.3, 99.4, 99.5,99.6,99.7,99.8,99.9,99.91,99.92,99.93,99.94,99.95,99.96,99.97,99.98,99.99,99.991,99.992,99.993,99.994,99.995,99.996,99.997,99.998,99.999,100],
            label2="End",
            items2=[i for i in range(0, 99)]+[99, 99.1, 99.2, 99.3, 99.4, 99.5,99.6,99.7,99.8,99.9,99.91,99.92,99.93,99.94,99.95,99.96,99.97,99.98,99.99,99.991,99.992,99.993,99.994,99.995,99.996,99.997,99.998,99.999,100]
        ),
        Dropdown(
            type="year",
            title="Year",
            label="from",
            items=[1992, 2002, 2006, 2008, 2010, 2013],
            label2="to",
            items2=[1992, 2002, 2006, 2008, 2010, 2013]
        ),
        header_text="Input"
    ),
    yAxis=YAxis(min=0, scale_label="Share %", max = 100,
                label_color="rgb(90, 20, 255)", label_size=12),
    xAxis=XAxis(scale_label="",
                label_color="rgb(90, 20, 255)", label_size=15),
    datasets=[
        Dataset(
            dataset_id="share",
            label="Minimmum",
            color="rgb(90, 30, 255)",
            border_width=1.0,
            fill=True,
            tension=1.0
        )
    ]
)


chart_config = ChartConfig(
    range_chart,
    dist_chart,
    share_chart,
    average_chart
)
