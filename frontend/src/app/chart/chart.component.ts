import {
  Component,
  AfterViewInit,
  Input,
  ElementRef,
  ViewChild,
} from '@angular/core';
import { Chart } from '../Types/Chart';
import * as Chartjs from 'chart.js';

@Component({
  selector: 'app-chart',
  templateUrl: './chart.component.html',
  styleUrls: ['./chart.component.scss'],
})
export class ChartComponent implements AfterViewInit {
  @Input()
  chart: Chart;
  @ViewChild('mychart')
  canvas: ElementRef;
  rChart = [];

  constructor() {}
  ngAfterViewInit() {
    this.rChart = new Chartjs.Chart(
      this.canvas.nativeElement.getContext('2d'),
      {
        type: this.chart.type,
        data: {
          labels: this.chart.labels,
          datasets: this.chart.datasets.map((dataset, index) => {
            const color = this.RgbToList(dataset.color);
            return {
              label: dataset.label,
              data: [1, 2, 3, 4, 5, 6, 7].map((x, idx) => ({
                x: this.chart.labels[idx],
                y: x * (index + 1),
              })),
              backgroundColor: this.rgba(color[0], color[1], color[2], 0.15),
              borderColor: dataset.color,
              borderWidth: dataset.border_width,
              fill: this.chart.fill_between ? 1 : dataset.fill ? true : false,
              lineTension: dataset.tension,
              tension: dataset.tension,
            };
          }),
        },
        options: {
          animation: {
            duration: this.chart.animation ? 1000 : 0,
          },
          elements: {
            point: {
              radius: this.chart.display_points ? this.chart.point_radius : 0,
              pointStyle: 'circle',
            },
          },
          legend: {
            display: this.chart.display_legend,
          },
          scales: {
            yAxes: [
              {
                gridLines: {
                  display: this.chart.display_grid,
                },
                ticks: {
                  suggestedMax: this.chart.yAxis.max
                    ? this.chart.yAxis.max
                    : 10,
                  suggestedMin: this.chart.yAxis.min ? this.chart.yAxis.min : 0,
                },
                scaleLabel: {
                  display: this.chart.yAxis.scale_label ? true : false,
                  labelString: this.chart.yAxis.scale_label,
                  fontColor: this.chart.yAxis.label_color,
                  fontSize: this.chart.yAxis.label_size,
                },
              },
            ],
            xAxes: [
              {
                gridLines: {
                  display: this.chart.display_grid,
                },
                ticks: {
                  stepSize: 1,
                  autoSkip: false,
                },
                type: this.chart.xAxis.type,
                position: 'bottom',
                scaleLabel: {
                  display: this.chart.xAxis.scale_label ? true : false,
                  labelString: this.chart.xAxis.scale_label,
                  fontColor: this.chart.xAxis.label_color,
                  fontSize: this.chart.xAxis.label_size,
                },
              },
            ],
          },
        },
      }
    );
  }

  private RgbToList(rgb: string) {
    const m = rgb.match(/^rgb\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)$/i);
    if (m) {
      return [m[1], m[2], m[3]];
    }
  }

  private rgba(red, green, blue, opacity) {
    return `rgba(${red}, ${green}, ${blue}, ${opacity})`;
  }
}
