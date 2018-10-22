from flask import Flask, send_from_directory
from flask import jsonify
from rest_api.helper_functions import xml_to_dict
import rest_api.data as data
import json

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

@app.route("/js/<path:path>")
def js(path):
    print(path)
    return send_from_directory('frontend/dist/frontend/', path)

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
    dist_out = x.to_frame().reset_index()[['AverageIncome']].join(z.to_frame()) #combine 2 pandas series in a dataframe
    dist_out.columns  = ["AverageIncome", "SmoothDistribution"] #naming columns
    dist_list = {"AverageIncome": list(dist_out["AverageIncome"]), "SmoothedDistribution": list(dist_out["SmoothDistribution"])}
    points = list(zip(dist_list["AverageIncome"], dist_list["SmoothedDistribution"]))
    #points = data.smooth_distribution_generator(points, 3)
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
    share_out_points = [list(i) for i in zip(share_out_dict.keys(), share_out_dict.values())]
    response = app.response_class(
        response=json.dumps(share_out_points),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/api/range/<float:p_start>/<float:p_end>/<int:year_from>/<int:year_to>")
def range_data(p_start, p_end, year_from, year_to):
    df_range = data.Threshold_range(p_start,p_end, year_from, year_to, data_path)
    indecies = [index for index, row in df_range.iterrows()]
    threshold_min = [row["Threshold(JOD)"]["threshold_min"] for index, row in df_range.iterrows()]
    threshold_max = [row["Threshold(JOD)"]["threshold_max"] for index, row in df_range.iterrows()]
    threshold_min_xy_points = [list(i) for i in zip(indecies, threshold_min)]
    threshold_max_xy_points = [list(i) for i in zip(indecies, threshold_max)]
    datasets = {
        "threshold_min_xy_points":threshold_min_xy_points,
        "threshold_max_xy_points":threshold_max_xy_points
    }
    response = app.response_class(
        response=json.dumps(datasets),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/api/chart_config")
def chart_config_json():
    with open("chart_config.json") as f:
        data = json.load(f)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(port=80)
