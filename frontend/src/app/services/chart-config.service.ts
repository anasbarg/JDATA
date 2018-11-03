import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject, Subject } from 'rxjs';
import { ChartConfig } from '../Types/ChartConfig';
import { Chart } from '../Types/Chart';
import { Slider } from '../Types/Slider';
import { Dataset } from '../Types/Dataset';
import { YAxis, XAxis } from '../Types/Axes';
import { ControllersList } from '../Types/ControllersList';
import { Dropdown } from '../Types/Dropdown';

@Injectable({
  providedIn: 'root',
})
export class ChartConfigService {
  chartConfig: Subject<ChartConfig> = new BehaviorSubject<ChartConfig>(
    new ChartConfig()
  );

  constructor(private _http: HttpClient) {}

  private JsonToChartConfig(response: any): ChartConfig {
    let conf = new ChartConfig();
    conf.charts = response.charts.map(chart => {
      // constructing ControllersList
      let controllers: ControllersList = new ControllersList();
      controllers.header_text = chart.controllers.header_text;
      controllers.controllers_list = chart.controllers.controllers_list.map(
        controller => {
          if (controller.type === 'dropdown') {
            return new Dropdown(
              controller.items,
              controller.label,
              controller.title,
              controller.items2,
              controller.label2
            );
          } else if (controller.type === 'slider') {
            return new Slider(
              controller.slider_type,
              controller.title,
              controller.pips
            );
          } else {
            return null;
          }
        }
      );
      // constructing a Array<Dataset>
      let datasets: Array<Dataset> = chart.datasets;
      let new_chart = new Chart(
        chart.data_provider,
        chart.title,
        chart.labels,
        controllers,
        new YAxis(
          chart.yAxis.scale_label,
          chart.yAxis.label_color,
          chart.yAxis.label_size,
          chart.yAxis.max,
          chart.yAxis.min
        ),
        new XAxis(
          chart.xAxis.scale_label,
          chart.xAxis.label_color,
          chart.xAxis.label_size,
          chart.xAxis.type
        ),
        datasets,
        chart.subtitle,
        chart.type,
        chart.fill_between,
        chart.point_radius,
        chart.display_points,
        chart.display_legend,
        chart.animation,
        chart.display_grid
      );
      return new_chart;
    });
    console.log(conf);
    return conf;
  }
  private getConfigFromAPI() {
    this._http.get<ChartConfig>('/assets/chart_config.json').subscribe(res => {
      console.log(res);
      this.chartConfig.next(this.JsonToChartConfig(res));
    });
  }

  public getChartConfig(): Observable<ChartConfig> {
    this.getConfigFromAPI();
    return this.chartConfig.asObservable();
  }
}
