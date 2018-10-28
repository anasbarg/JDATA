import { IController } from './IController';

export class Dropdown implements IController {
  constructor(
    public items: Array<any>,
    public label: string = '',
    public title: string = '',
    public items2: Array<any> | null = null,
    public label2: string = ''
  ) {}

  isDropdown() {
    return true;
  }

  isSlider() {
    return false;
  }

  isCheckbox() {
    return false;
  }
}
