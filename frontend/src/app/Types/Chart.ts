import { IController } from "./IController";
import { Slider } from "./Slider";
import { Dataset } from "./Dataset";
import { Axis } from "./Axis";

export class Chart {
  data_provider: string;
  title: string;
  subtitle: string;
  type: string;
  fill_between: boolean;
  point_radius: Number;
  display_points: boolean;
  display_legend: boolean;
  animation: boolean;
  display_grid: boolean;
  controllers: Array<IController>;
  yAxis: Axis;
  xAxis: Axis;
  datasets: Array<Dataset>;
  constructor(
    data_provider: string,
    title: string,
    controllers: Array<IController>,
    yAxis: Axis,
    xAxis: Axis,
    datasets: Array<Dataset>,
    subtitle?: string,
    type?: string,
    fill_between?: boolean,
    point_radius?: Number,
    display_points?: boolean,
    display_legend?: boolean,
    animation?: boolean,
    display_grid?: boolean
  ) {
    // Requiered
    this.data_provider = data_provider;
    this.title = title;
    this.controllers = controllers;
    this.yAxis = yAxis;
    this.xAxis = xAxis;
    this.datasets = datasets;
    // Optionals
    this.subtitle = subtitle ? subtitle : "";
    this.type = type ? type : "line";
    this.fill_between = fill_between ? fill_between : false;
    this.point_radius = point_radius ? point_radius : 2;
    this.display_points = display_points ? display_points : true;
    this.display_legend = display_legend ? display_legend : false;
    this.animation = animation ? animation : true;
    this.display_grid = display_grid ? display_grid : true;
  }
}
