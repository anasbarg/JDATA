import { Component, OnInit } from "@angular/core";
import { ChartConfig } from "../Types/ChartConfig";
// Services
import { ChartConfigService } from "../services/chart-config.service";

@Component({
  selector: "app-content",
  templateUrl: "./content.component.html",
  styleUrls: ["./content.component.scss"]
})
export class ContentComponent implements OnInit {
  chartConfig: ChartConfig;
  constructor(private _chartConfigService: ChartConfigService) {}

  ngOnInit() {
    this._chartConfigService
      .getChartConfig()
      .subscribe(conf => (this.chartConfig = conf));
  }
}
