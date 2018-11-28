import { Injectable } from '@angular/core';
import { BehaviorSubject, Subject } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { ChartConfigService } from './chart-config.service';

@Injectable({
    providedIn: 'root',
})
export class DataService {
    private rangeData: Subject<any> = new BehaviorSubject({});
    private currentRangeData = this.rangeData.asObservable();
    private shareData: Subject<any> = new BehaviorSubject({});
    private currentShareData = this.shareData.asObservable();
    private distributionData: Subject<any> = new BehaviorSubject({});
    private currentDistributionData = this.distributionData.asObservable();
    private averageIncomeData: Subject<any> = new BehaviorSubject({});
    private currentAverageIncomeData = this.averageIncomeData.asObservable();
    private rankData: Subject<any> = new BehaviorSubject({});
    private currentRankData = this.rankData.asObservable();
    constructor(
        private _http: HttpClient,
        private _chartConfig: ChartConfigService
    ) {
        this._chartConfig.getChartConfig().subscribe(conf => {
            conf.charts.forEach(chart => {
                this.setData(chart.data_provider, {
                    year: [1992, 2013],
                    percentile: [0.000001, 99.99999],
                });
            });
        });
    }

    private setRangeData(p_start, p_end, year_from, year_to) {
        this._http
            .get(
                `/api/range/${p_start + 0.000001}/${p_end +
                    0.000001}/${year_from}/${year_to}`
            )
            .subscribe(data => {
                this.rangeData.next(data);
            });
    }

    private setAverageIncomeData(p_start, p_end, year_from, year_to) {
        this._http
            .get(
                `/api/average/${p_start + 0.000001}/${p_end +
                    0.000001}/${year_from}/${year_to}`
            )
            .subscribe(data => {
                this.averageIncomeData.next(data);
            });
    }

    private setShareData(p_start, p_end, year_from, year_to) {
        this._http
            .get(
                `/api/share/${p_start + 0.000001}/${p_end +
                    0.000001}/${year_from}/${year_to}`
            )
            .subscribe(data => {
                this.shareData.next(data);
            });
    }

    private setRankData(salary, year_from, year_to) {
        this._http
            .get(`/api/rank/${salary + 0.000001}/${year_from}/${year_to}`)
            .subscribe(data => {
                this.rankData.next(data);
            });
    }

    private setDistributionData(year) {
        this._http.get(`/api/distribution/${year}`).subscribe(data => {
            this.distributionData.next(data);
        });
    }
    public getData(data_provider: string) {
        if (data_provider === 'dist') {
            return this.currentDistributionData;
        } else if (data_provider === 'share') {
            return this.currentShareData;
        } else if (data_provider === 'range') {
            return this.currentRangeData;
        } else if (data_provider === 'average') {
            return this.currentAverageIncomeData;
        } else if (data_provider === 'rank') {
            return this.currentRankData;
        }
    }
    public setData(
        data_provider: string,
        kwargs: {
            year: number[];
            percentile: number[];
        }
    ) {
        if (data_provider === 'dist') {
            this.setDistributionData(kwargs.year[0]);
        } else if (data_provider === 'share') {
            this.setShareData(
                kwargs.percentile[0],
                kwargs.percentile[1],
                kwargs.year[0],
                kwargs.year[1]
            );
        } else if (data_provider === 'range') {
            this.setRangeData(
                kwargs.percentile[0],
                kwargs.percentile[1],
                kwargs.year[0],
                kwargs.year[1]
            );
        } else if (data_provider === 'average') {
            this.setAverageIncomeData(
                kwargs.percentile[0],
                kwargs.percentile[1],
                kwargs.year[0],
                kwargs.year[1]
            );
        } else if (data_provider === 'rank') {
            console.log(data_provider, kwargs);
            this.setRankData(
                kwargs.percentile[0],
                kwargs.year[0],
                kwargs.year[1]
            );
        }
    }
}
