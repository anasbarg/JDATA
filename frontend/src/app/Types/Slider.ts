import { IController } from "./IController";

export class Slider implements IController {
  type: string;
  label: string;
  pips: Array<any>;
  constructor(type: string, label?: string, pips?: Array<any>) {
    this.type = type;
    this.label = label ? label : "";
    this.pips = pips ? pips : null;
  }

  isSlider() {
    return true;
  }
}
