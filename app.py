from flask import Flask, send_from_directory
from flask import jsonify
import RestApi.data as data
from RestApi.config import chart_config
import json
import re

data_path = "data.csv"
app = Flask(__name__, static_url_path='/../frontend')


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['Acess-Control-Allow-Origin'] = '*'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route("/")
@app.route("/home")
def home():
    return send_from_directory('frontend/dist/frontend', "index.html")


@app.route("/<path:path>")
def js(path):
    if ".js" in path:
        return send_from_directory('frontend/dist/frontend', path)
    elif ".css" in path:
        return send_from_directory('frontend/dist/frontend', path)
    else:
        return app.response_class(status=404)


@app.route("/css/<path:path>")
def css(path):
    return send_from_directory('frontend/css', path)


@app.route("/nouislidercss/<path:path>")
def nouislider_css(path):
    return send_from_directory('frontend/node_modules/nouislider/distribute/', path)


@app.route("/api/distribution/<int:year>")
def distribution_data(year):
    smoothing_factor = 0.4
    x, y, z = data.distribution(year, smoothing_factor, data_path)
    dist_out = x.to_frame().reset_index()[['AverageIncome']].join(
        z.to_frame())  # combine 2 pandas series in a dataframe
    dist_out.columns = ["AverageIncome",
                        "SmoothDistribution"]  # naming columns
    dist_list = {"AverageIncome": list(
        dist_out["AverageIncome"]), "SmoothedDistribution": list(dist_out["SmoothDistribution"])}
    points = list(zip(dist_list["AverageIncome"],
                      dist_list["SmoothedDistribution"]))
    points = {"dist": points}
    response = app.response_class(
        response=json.dumps(points),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/api/share/<float:p_start>/<float:p_end>/<int:year_from>/<int:year_to>")
def share_data(p_start, p_end, year_from, year_to):
    share_out = data.share(p_start, p_end, year_from, year_to, data_path)
    share_out_dict = share_out.to_dict()['Share']
    share_out_points = [list(i) for i in zip(
        share_out_dict.keys(), share_out_dict.values())]
    share_out_points = {"share": share_out_points}
    response = app.response_class(
        response=json.dumps(share_out_points),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/api/average/<float:p_start>/<float:p_end>/<int:year_from>/<int:year_to>")
def average_income_data(p_start, p_end, year_from, year_to):
    avg_income = data.AverageIncome(
        p_start, p_end, year_from, year_to, data_path)
    data_ = {"min": [list(i) for i in list(zip(avg_income.to_dict()[('AverageIncome', 'Average_min')].keys(),
                                               avg_income.to_dict()[('AverageIncome', 'Average_min')].values()))],
             "max": [list(i) for i in list(zip(
                 avg_income.to_dict()[('AverageIncome', 'Average_max')].keys(
                 ), avg_income.to_dict()[('AverageIncome', 'Average_max')].values()
             ))]}
    response = app.response_class(
        response=json.dumps(data_),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/api/range/<float:p_start>/<float:p_end>/<int:year_from>/<int:year_to>")
def range_data(p_start, p_end, year_from, year_to):
    df_range = data.Threshold_range(
        p_start, p_end, year_from, year_to, data_path)
    indecies = [index for index, row in df_range.iterrows()]
    threshold_min = [row["Threshold(JOD)"]["threshold_min"]
                     for index, row in df_range.iterrows()]
    threshold_max = [row["Threshold(JOD)"]["threshold_max"]
                     for index, row in df_range.iterrows()]
    threshold_min_xy_points = [list(i) for i in zip(indecies, threshold_min)]
    threshold_max_xy_points = [list(i) for i in zip(indecies, threshold_max)]
    datasets = {
        "min": threshold_min_xy_points,
        "max": threshold_max_xy_points
    }
    response = app.response_class(
        response=json.dumps(datasets),
        status=200,
        mimetype='application/json'
    )
    return response

"""
@app.route("/api/range/<float:Msalary>/<int:year_from>/<int:year_to>")
def rank_data(Msalary, year_from, year_to):
    df_rank = data.Rank_salary(
        Msalary, year_from, year_to, data_path)
    indecies = [index for index, row in df_range.iterrows()]
    percentile_max = [row["start"]["percentile_max"]
                     for index, row in df_range.iterrows()]
    perscetile_max_xy_points = [list(i) for i in zip(indecies, percentile_max)]
    datasets = {
        "max": perscetile_max_xy_points
    }
    response = app.response_class(
        response=json.dumps(datasets),
        status=200,
        mimetype='application/json'
    )
    return response
"""

"""
def percentile(Salary, Year_from,Year_to,path):
    df = pd.read_csv(path)
    YearlyIncome = 12*Salary
    df_percentile = df[(df.year>=Year_from)&(df.year<=Year_to)&(df['Threshold(JOD)']<=YearlyIncome)].copy()   
    df_percentile1 = df_percentile.groupby('year')
    aggregation = {'start':'max'}
    
    return df_percentile1.agg(aggregation)
"""



@app.route("/api/chart_config")
def chart_config_json():
    data = chart_config
    response = app.response_class(
        response=json.dumps(data.to_dict()),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(port=80)
