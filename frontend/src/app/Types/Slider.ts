import { IController } from './IController';

export class Slider implements IController {
    constructor(
        public id: string,
        public title: string = '',
        public pips: Array<any> | null = null
    ) {}

    isSlider() {
        return true;
    }

    isDropdown() {
        return false;
    }

    isCheckbox() {
        return false;
    }
}
