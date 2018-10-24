import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable, of } from "rxjs";
import { ChartConfig } from "../Types/ChartConfig";
import { Chart } from "../Types/Chart";
import { Slider } from "../Types/Slider";
import { Dataset } from "../Types/Dataset";
import { Axis } from "../Types/Axis";

@Injectable({
  providedIn: "root"
})
export class ChartConfigService {
  chartConfig: ChartConfig = new ChartConfig([
    new Chart(
      "Threshold_range",
      "Boudaries Of Average Income",
      [
        new Slider("RangeYearSlider", "Year Interval", [
          1992,
          2002,
          2006,
          2008,
          2010,
          2013
        ]),
        new Slider("RangePercentageSlider", "Percentage Interval")
      ],
      new Axis("Average Income"),
      new Axis("Year"),
      [new Dataset("min"), new Dataset("max")]
    ),
    new Chart(
      "share",
      "Share",
      [
        new Slider("RangeYearSlider", "Year Interval", [
          1992,
          2002,
          2006,
          2008,
          2010,
          2013
        ]),
        new Slider("RangePercentageSlider", "Percentage Interval")
      ],
      new Axis("Average Income"),
      new Axis("Year"),
      [new Dataset("share")]
    )
  ]);

  constructor(private http: HttpClient) {}

  public getChartConfig(): Observable<ChartConfig> {
    return of(this.chartConfig);
  }
}
