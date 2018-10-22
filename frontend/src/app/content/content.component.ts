import { Component, OnInit } from "@angular/core";

// Services
import { ChartConfigService } from "../services/chart-config.service";

@Component({
  selector: "app-content",
  templateUrl: "./content.component.html",
  styleUrls: ["./content.component.scss"]
})
export class ContentComponent implements OnInit {
  arr: Array<Number> = [1, 2, 3, 4];
  chartConfig: any;
  constructor(private _chartConfigService: ChartConfigService) {}

  ngOnInit() {
    this._chartConfigService
      .getChartConfig()
      .subscribe(conf => (this.chartConfig = conf));
  }
}
