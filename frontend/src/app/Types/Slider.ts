export class Slider {
  label: string;
  type: string;
  pips: Array<any>;
  constructor(label: string, type: string, pips?: Array<any>) {
    this.label = label;
    this.type = type;
    this.pips = pips ? pips : null;
  }
}
