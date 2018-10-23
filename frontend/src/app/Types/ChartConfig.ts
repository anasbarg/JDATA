import { Chart } from "./Chart";

export class ChartConfig {
  charts: Array<Chart>;
  constructor(charts: Array<Chart>) {
    this.charts = charts;
  }
}
