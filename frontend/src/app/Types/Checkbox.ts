import { IController } from "./IController";

export class Checkbox implements IController {
  label: string;
  constructor(label?: string) {
    // handeling optional attribute
    this.label = label ? label : "";
  }

  isCheckbox() {
    return true;
  }
}
