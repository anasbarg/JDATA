import { Component, OnInit, Input } from "@angular/core";
import { Chart } from "../Types/Chart";
@Component({
  selector: "app-chart-card",
  templateUrl: "./chart-card.component.html",
  styleUrls: ["./chart-card.component.scss"]
})
export class ChartCardComponent implements OnInit {
  @Input("chart")
  chart: Chart;

  constructor() {}

  ngOnInit() {}
}
