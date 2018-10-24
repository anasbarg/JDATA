import { Component, OnInit, Input } from "@angular/core";
import { ControllersList } from "../Types/ControllersList";
import { Slider } from "../Types/Slider";
@Component({
  selector: "app-chart-controllers",
  templateUrl: "./chart-controllers.component.html",
  styleUrls: ["./chart-controllers.component.scss"]
})
export class ChartControllersComponent implements OnInit {
  @Input("chart-controllers")
  chartControllers: ControllersList;
  constructor() {}

  ngOnInit() {}
}
