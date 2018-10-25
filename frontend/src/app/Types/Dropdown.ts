import { IController } from "./IController";

export class Dropdown implements IController {
  label: string;
  items: Array<any>;
  constructor(items: Array<any>, label?: string) {
    this.label = label ? label : ""; // handeling optional attribute
    this.items = items; // handeling required attribute
  }

  isDropdown() {
    return true;
  }
}
