import { Slider } from "./Slider";
import { Dataset } from "./Dataset";
import { ChartOptions } from "./ChartOptions";

export interface Chart {
  dataProvider: string;
  title: string;
  subtitle: string;
  type: string;
  fillBetween: boolean;
  sliders: Array<Slider>;
  datasets: Array<Dataset>;
  options: ChartOptions;
}
