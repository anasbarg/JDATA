import { IController } from './IController';

export class Slider implements IController {
  constructor(
    public type: string,
    public title: string = '',
    public pips?: Array<any>
  ) {
    this.pips = pips ? pips : null;
  }

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
