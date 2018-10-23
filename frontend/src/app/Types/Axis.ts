export class Axis {
  min: Number;
  max: Number;
  scale_label: string;
  label_color: string;
  constructor(
    min: Number,
    max: Number,
    scale_label: string,
    label_color: string
  ) {
    this.scale_label = scale_label;
    this.label_color = label_color;
    this.min = min ? min : null;
    this.max = max ? max : null;
  }
}
