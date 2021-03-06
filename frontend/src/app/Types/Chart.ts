import { Dataset } from './Dataset';
import { XAxis, YAxis } from './Axes';
import { ControllersList } from './ControllersList';

export class Chart {
    constructor(
        public data_provider: string,
        public title: string,
        public labels: Array<any>,
        public controllers: ControllersList,
        public yAxis: YAxis,
        public xAxis: XAxis,
        public datasets: Array<Dataset>,
        public subtitle: string = '',
        public type: string = 'line',
        public fill_between: boolean = false,
        public point_radius: Number = 2,
        public display_points: boolean = true,
        public display_legend: boolean = false,
        public animation: boolean = true,
        public display_grid: boolean = true,
        public description: string = '',
        public description_title: string = ''
    ) {
        /*
    if (this.datasets.length < 2 && this.fill_between) {
      this.fill_between = false;
    }
    */
    }
}
