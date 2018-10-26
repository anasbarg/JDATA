import { IController } from "./IController";

export class Dropdown implements IController {
  constructor(
    public items: Array<any>,
    public label?: string,
    public title?: string,
    public items2?: Array<any>,
    public label2?: string
  ) {
    this.items = items; // handeling required attribute
    this.label = label ? label : ""; // handeling optional attribute
    this.items2 = items2 ? items2 : undefined; // handeling optional attribute
    this.label2 = label2 ? label2 : ""; // handeling optional attribute
    this.title = title ? title : ""; // handeling optional attribute
  }

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
