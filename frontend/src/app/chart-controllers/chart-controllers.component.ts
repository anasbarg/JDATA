import { Component, OnInit, Input } from "@angular/core";
import { IController } from "../Types/IController";
@Component({
  selector: "app-chart-controllers",
  templateUrl: "./chart-controllers.component.html",
  styleUrls: ["./chart-controllers.component.scss"]
})
export class ChartControllersComponent implements OnInit {
  @Input("chart")
  chart: Array<IController>;
  constructor() {}

  ngOnInit() {
    console.log(this.chart);
  }
}
