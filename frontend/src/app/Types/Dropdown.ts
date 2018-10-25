import { IController } from "./IController";

export class Dropdown implements IController {
  title: string;
  label: string;
  items: Array<any>;
  label2: string;
  items2: Array<any>;
  constructor(
    items: Array<any>,
    label?: string,
    title?: string,
    items2?: Array<any>,
    label2?: string
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
