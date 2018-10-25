import { IController } from "./IController";

export class Slider implements IController {
  type: string;
  title: string;
  pips: Array<any>;
  constructor(type: string, title?: string, pips?: Array<any>) {
    this.type = type;
    this.title = title ? title : "";
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
