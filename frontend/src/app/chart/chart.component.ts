import { Component, OnInit, Input } from '@angular/core';
import { Chart } from '../Types/Chart';

@Component({
    selector: 'app-chart',
    templateUrl: './chart.component.html',
    styleUrls: ['./chart.component.scss'],
})
export class ChartComponent implements OnInit {
    @Input()
    chart: Chart;

    constructor() {}

    ngOnInit() {}
}
