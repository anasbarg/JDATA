import { Component, Input, OnInit } from '@angular/core';
import { Chart } from '../Types/Chart';
import { DataService } from '../services/data.service';

@Component({
    selector: 'app-chart',
    templateUrl: './chart.component.html',
    styleUrls: ['./chart.component.scss'],
})
export class ChartComponent implements OnInit {
    @Input()
    chart: Chart;
    Data: Array<any>;
    Labels: Array<any>;
    ChartType: string;
    DatasetsColors: Array<any>;
    Legend: boolean;
    Options: any;
    constructor(private _dataService: DataService) {}

    ngOnInit() {
        this.Legend = this.chart.display_legend;
        this.DatasetsColors = this.chart.datasets.map(dataset => {
            const color = this.RgbToList(dataset.color);
            const transparent = this.rgba(color[0], color[1], color[2], 0.15);
            const noColor = this.rgba(color[0], color[1], color[2], 0);
            const fullColor = this.rgba(color[0], color[1], color[2], 1);
            return {
                backgroundColor: transparent,
                borderColor: fullColor,
                pointBackgroundColor: fullColor,
                pointBorderColor: fullColor,
                pointHoverBackgroundColor: fullColor,
                pointHoverBorderColor: fullColor,
            };
        });
        this.ChartType = this.chart.type;
        this.Labels = this.chart.labels;
        this._dataService.getData(this.chart.data_provider).subscribe(data => {
            this.Data = this.chart.datasets.map(dataset => {
                return {
                    data: data[dataset.dataset_id]
                        ? data[dataset.dataset_id].map(point => ({
                              x: point[0],
                              y: point[1],
                          }))
                        : [],
                    label: dataset.label,
                    borderWidth: dataset.border_width,
                    fill: this.chart.fill_between
                        ? 1
                        : dataset.fill
                            ? true
                            : false,
                    tension: dataset.tension / 2,
                    lineTension: dataset.tension / 2,
                };
            });
        });
        this.Options = {
            responsive: true,
            animation: {
                duration: this.chart.animation ? 2000 : 0,
            },
            elements: {
                point: {
                    radius: this.chart.display_points
                        ? this.chart.point_radius
                        : 0,
                    pointStyle: 'circle',
                },
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
                                : undefined,
                            suggestedMin: this.chart.yAxis.min
                                ? this.chart.yAxis.min
                                : 0,
                            beginAtZero: true,
                        },
                        scaleLabel: {
                            display: this.chart.yAxis.scale_label
                                ? true
                                : false,
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
                            display: this.chart.xAxis.scale_label
                                ? true
                                : false,
                            labelString: this.chart.xAxis.scale_label,
                            fontColor: this.chart.xAxis.label_color,
                            fontSize: this.chart.xAxis.label_size,
                        },
                    },
                ],
            },
        };
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
