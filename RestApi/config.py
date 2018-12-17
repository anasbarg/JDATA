from json import dumps
import numpy as np
from RestApi.Types.ChartConfig import *



dist_chart = Chart(
    data_provider="dist",
    title="Income distribution",
    description="Income distribution\n is the probability density function of the monthly income at a chosen year. \n\n This graph answers questions like: \n what is the probability that the salary of a randomly chosen adult equals 1000 JD?",
    description_title="",
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
    yAxis=YAxis(scale_label="Probability", min = 0,
                label_color="rgb(90, 20, 255)", label_size=15),
    xAxis=XAxis(scale_label="Monthly income (logarithmic scale: 3 means 1000 JD, 4 means 10000 JD)",
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
    title="Threshold",
    description="Threshold  \n is the minimum pre-tax yearly income for a chosen percentile \n\n This graph answers questions like: \n what is the min income for those at the top 1%? It also allows comparing 2 percentiles",
    description_title="",
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
            title="Percentile [%]",
            label="first persentile",
            items=[i for i in range(1, 99)]+[
                99, 99.1, 99.2, 99.3, 99.4, 99.5,99.6,99.7,99.8,99.9,99.91,99.92,99.93,99.94,99.95,99.96,99.97,99.98,99.99,99.995,99.999],
            label2="second persentile",
            items2=[i for i in range(1, 99)]+[
                99, 99.1, 99.2, 99.3, 99.4, 99.5,99.6,99.7,99.8,99.9,99.91,99.92,99.93,99.94,99.95,99.96,99.97,99.98,99.99,99.995,99.999]
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
                label_color="rgb(90, 20, 255)", label_size=15),
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
    title="Gap in average income",
    description="Average income compares between the average pre-tax yearly income of 2 chosen percentiles. \n\n This graph answers questions like: \n what is the gap in average income between those ranked at the 90 percentile and those at 50 percentile",
    description_title="",
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
            title="Percentile [%]",
            label="first persentile",
            items=[i for i in range(0, 99)]+[
                99, 99.1, 99.2, 99.3, 99.4, 99.5,99.6,99.7,99.8,99.9,99.91,99.92,99.93,99.94,99.95,99.96,99.97,99.98,99.99,99.995,99.999],
            label2="second persentile",
            items2=[i for i in range(0, 99)]+[
                99, 99.1, 99.2, 99.3, 99.4, 99.5,99.6,99.7,99.8,99.9,99.91,99.92,99.93,99.94,99.95,99.96,99.97,99.98,99.99,99.995,99.999]
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
                label_color="rgb(90, 20, 255)", label_size=15),
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
    description="Share is the percentage of Pre-tax national income acquired by a given percentile group. \n\n This graph answers questions like: \n what percentage of the national income does the top 1% hold?",
    description_title="",
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
            title="Percentile group [%]",
            label="Start",
            items=[i for i in range(0, 99)]+[
                99, 99.1, 99.2, 99.3, 99.4, 99.5,99.6,99.7,99.8,99.9,99.91,99.92,99.93,99.94,99.95,99.96,99.97,99.98,99.99,99.995,99.999],
            label2="End",
            items2=[i for i in range(0, 99)]+[
                99, 99.1, 99.2, 99.3, 99.4, 99.5,99.6,99.7,99.8,99.9,99.91,99.92,99.93,99.94,99.95,99.96,99.97,99.98,99.99,99.995,99.999]
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
                label_color="rgb(90, 20, 255)", label_size=15),
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


rank_chart = Chart(
    data_provider="rank",
    description="Rank is the percentile of a chosen monthly income (salary) when ranked among the monthly income of adult population \n\n This graph answers questions like: \n what is the percentile rank of an adult with 1000 JD salary?",
    description_title="",
    title="Rank",
    subtitle="find the percentile according to a monthly income/salary",
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
            title="Monthly income/salary",
            label="",
            items=[int(i) for i in (list(np.arange(0, 200, 5))+list(np.arange(200, 900, 20))+list(np.arange(900, 1400, 50))+list(
                np.arange(1400, 3000, 100))+ list(np.arange(3000, 20000, 500))+list(np.arange(20000, 50000, 1000))+list(
                np.arange(50000, 100000, 5000))+list(np.arange(100000, 1000000, 10000))+list(np.arange(1000000, 500000,10000000)))]
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
    yAxis=YAxis(min=0, scale_label="Percentile rank %", max = 100,
                label_color="rgb(90, 20, 255)", label_size=15),
    xAxis=XAxis(scale_label="",
                label_color="rgb(90, 20, 255)", label_size=15),
    datasets=[
        Dataset(
            dataset_id="rank",
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
    average_chart,
    rank_chart
)

