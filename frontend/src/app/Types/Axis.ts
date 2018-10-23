export class Axis {
  min: Number;
  max: Number;
  scale_label: string;
  label_color: string;
  constructor(
    scale_label: string,
    label_color?: string,
    max?: Number,
    min?: Number
  ) {
    this.scale_label = scale_label;
    this.label_color = label_color ? label_color : "rgb(104, 104, 104)";
    this.min = min ? min : null;
    this.max = max ? max : null;
  }
}
