import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { ChartConfig } from '../Types/ChartConfig';
import { Chart } from '../Types/Chart';
import { Slider } from '../Types/Slider';
import { Dataset } from '../Types/Dataset';
import { YAxis, XAxis } from '../Types/Axes';
import { ControllersList } from '../Types/ControllersList';
import { Dropdown } from '../Types/Dropdown';

@Injectable({
  providedIn: 'root',
})
export class ChartConfigService {
  chartConfig: ChartConfig = new ChartConfig([
    new Chart(
      'Threshold_range',
      'Boudaries Of Average Income',
      [1992, 2002, 2004, 2006, 2008, 2010, 2013],
      new ControllersList(
        'Input Controllers',
        new Dropdown([1, 2, 3], 'Start', 'kkk', [2, 3, 5], 'End'),
        new Dropdown([5, 56, 34.6], 'Start', 'kkkk')
      ),
      new YAxis('Average Income'),
      new XAxis('Year'),
      [new Dataset('min', 'Min'), new Dataset('max', 'Max')],
      'subtitle',
      'line',
      false,
      1,
      true,
      true,
      true,
      true
    ),
    new Chart(
      'share',
      'Share',
      [1992, 2002, 2004, 2006, 2008, 2010, 2013],
      new ControllersList(
        'Input Controllers',
        new Slider('RangeYearSlider', 'Year Interval', [
          1992,
          2002,
          2006,
          2008,
          2010,
          2013,
        ]),
        new Slider('RangePercentageSlider', 'Percentage Interval')
      ),
      new YAxis('Average Income'),
      new XAxis('Year'),
      [new Dataset('share')]
    ),
  ]);

  constructor(private http: HttpClient) {}

  public getChartConfig(): Observable<ChartConfig> {
    return of(this.chartConfig);
  }
}
