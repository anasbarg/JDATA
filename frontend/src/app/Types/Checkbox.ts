import { IController } from "./IController";

export class Checkbox implements IController {
  constructor(public label?: string, public title?: string) {
    // handeling optional attribute
    this.label = label ? label : "";
    this.title = title ? title : "";
  }

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
