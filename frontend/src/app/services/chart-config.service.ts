import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable, of } from "rxjs";

@Injectable({
  providedIn: "root"
})
export class ChartConfigService {
  chartConfig: Object = {
    charts: [
      {
        data_provider: "Threshold_range",
        title: "Boundaries Of Average Income",
        subtitle: "Please Specify The Intervals",
        type: "line",
        fillBetween: "true",
        sliders: [
          {
            type: "yearSlider",
            labels: "[1992, 2002, 2006, 2008, 2010, 2013]"
          },
          {
            type: "percentageSlider"
          }
        ],
        datasets: [
          {
            dataset_id: "min",
            label: "A label",
            color: "rgb(90, 30, 255)",
            borderWidth: "1",
            fill: true
          },
          {
            dataset_id: "max",
            label: "A label",
            color: "rgb(90, 20, 255)",
            borderWidth: "1",
            fill: true
          }
        ],
        options: {
          pointRadius: "2",
          legendDisplay: true,
          yAxis: {
            min: "0",
            max: "1",
            scaleLabel: ""
          },
          xAxis: {
            scaleLabel: ""
          }
        }
      },
      {
        data_provider: "Threshold_range",
        title: "Income Distribution",
        subtitle: "Please Select The Year",
        type: "line",
        fillBetween: "true",
        sliders: [
          {
            type: "yearSlider",
            labels: "[1992, 2002, 2006, 2008, 2010, 2013]"
          },
          {
            type: "percentageSlider"
          }
        ],
        datasets: [
          {
            dataset_id: "min",
            label: "A label",
            color: "rgb(90, 30, 255)",
            borderWidth: "1",
            fill: true
          },
          {
            dataset_id: "max",
            label: "A label",
            color: "rgb(90, 20, 255)",
            borderWidth: "1",
            fill: true
          }
        ],
        options: {
          pointRadius: "2",
          legendDisplay: true,
          yAxis: {
            min: "0",
            max: "1",
            scaleLabel: ""
          },
          xAxis: {
            scaleLabel: ""
          }
        }
      },
      {
        data_provider: "Threshold_range",
        title: "Share",
        subtitle: "Please Specify The Intervals",
        type: "line",
        fillBetween: "true",
        sliders: [
          {
            type: "yearSlider",
            labels: "[1992, 2002, 2006, 2008, 2010, 2013]"
          },
          {
            type: "percentageSlider"
          }
        ],
        datasets: [
          {
            dataset_id: "min",
            label: "A label",
            color: "rgb(90, 30, 255)",
            borderWidth: "1",
            fill: true
          },
          {
            dataset_id: "max",
            label: "A label",
            color: "rgb(90, 20, 255)",
            borderWidth: "1",
            fill: true
          }
        ],
        options: {
          pointRadius: "2",
          legendDisplay: true,
          yAxis: {
            min: "0",
            max: "1",
            scaleLabel: ""
          },
          xAxis: {
            scaleLabel: ""
          }
        }
      }
    ]
  };

  constructor(private http: HttpClient) {}

  public getChartConfig(): Observable<Object> {
    return of(this.chartConfig);
  }
}
