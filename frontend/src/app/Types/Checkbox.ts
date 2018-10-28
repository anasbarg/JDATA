import { IController } from './IController';

export class Checkbox implements IController {
  constructor(public label: string = '', public title: string = '') {}

  isCheckbox() {
    return true;
  }

  isDropdown() {
    return false;
  }

  isSlider() {
    return false;
  }
}
