export class Slider {
  type: string;
  label: string;
  pips: Array<any>;
  constructor(type: string, label?: string, pips?: Array<any>) {
    this.type = type;
    this.label = label ? label : "";
    this.pips = pips ? pips : null;
  }
}
