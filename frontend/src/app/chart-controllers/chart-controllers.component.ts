import { Component, OnInit, Input } from "@angular/core";
import { Slider } from "../Types/Slider";
@Component({
  selector: "app-chart-controllers",
  templateUrl: "./chart-controllers.component.html",
  styleUrls: ["./chart-controllers.component.scss"]
})
export class ChartControllersComponent implements OnInit {
  @Input("chart")
  chart: Array<Slider>;
  constructor() {}

  ngOnInit() {
    console.log(this.chart);
  }
}
