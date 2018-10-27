import { Dataset } from './Dataset';
import { Axis } from './Axis';
import { ControllersList } from './ControllersList';

export class Chart {
    constructor(
        public data_provider: string,
        public labels: Array<any>,
        public title: string,
        public controllers: ControllersList,
        public yAxis: Axis,
        public xAxis: Axis,
        public datasets: Array<Dataset>,
        public subtitle?: string,
        public type?: string,
        public fill_between?: boolean,
        public point_radius?: Number,
        public display_points?: boolean,
        public display_legend?: boolean,
        public animation?: boolean,
        public display_grid?: boolean
    ) {
        // Requiered
        this.data_provider = data_provider;
        this.title = title;
        this.controllers = controllers;
        this.yAxis = yAxis;
        this.xAxis = xAxis;
        this.datasets = datasets;
        // Optionals
        this.subtitle = subtitle ? subtitle : '';
        this.type = type ? type : 'line';
        this.fill_between = fill_between ? fill_between : false;
        this.point_radius = point_radius ? point_radius : 2;
        this.display_points = display_points ? display_points : true;
        this.display_legend = display_legend ? display_legend : false;
        this.animation = animation ? animation : true;
        this.display_grid = display_grid ? display_grid : true;
    }
}
