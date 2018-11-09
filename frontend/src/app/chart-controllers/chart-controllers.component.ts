import { Component, OnInit, Input } from '@angular/core';
import { ControllersList } from '../Types/ControllersList';
import { Dropdown } from '../Types/Dropdown';
import { DataService } from '../services/data.service';

@Component({
    selector: 'app-chart-controllers',
    templateUrl: './chart-controllers.component.html',
    styleUrls: ['./chart-controllers.component.scss'],
})
export class ChartControllersComponent implements OnInit {
    // tslint:disable-next-line:no-input-rename
    @Input('chart-controllers')
    chartControllers: ControllersList;
    // tslint:disable-next-line:no-input-rename
    @Input('data-provider')
    dataProvider: string;
    state: any = [];
    constructor(private _dataService: DataService) {}

    ngOnInit() {
        this.state = this.chartControllers.controllers_list.map(controller => {
            if (this.is2Dropdowns(controller)) {
                return {
                    selected: [
                        `${controller.items[0]}`,
                        `${controller.items2[controller.items2.length - 1]}`,
                    ],
                    type: controller.dropdown_type,
                };
            } else {
                return {
                    selected: [controller.items[0]],
                    type: controller.dropdown_type,
                };
            }
        });
    }

    is2Dropdowns(dropdownConfig: Dropdown) {
        return dropdownConfig.items && dropdownConfig.items2;
    }

    onChange(index: number, index2?: number) {
        this._dataService.setData(this.dataProvider, {
            year: this.getControllerStateByType('year').selected.map(x =>
                parseFloat(x)
            ),
            percentile: this.getControllerStateByType('percentile')
                ? this.getControllerStateByType('percentile').selected.map(x =>
                      parseFloat(x)
                  )
                : [],
        });
    }

    getControllerStateByType(
        type: string
    ): { selected: Array<any>; type: string } {
        for (let controller of this.state) {
            if (controller.type === type) {
                return controller;
            }
        }
    }
}
