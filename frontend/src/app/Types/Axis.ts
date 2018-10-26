export class Axis {
  constructor(
    public scale_label: string,
    public label_color?: string,
    public max?: Number,
    public min?: Number
  ) {
    this.scale_label = scale_label;
    this.label_color = label_color ? label_color : "rgb(104, 104, 104)";
    this.min = min ? min : null;
    this.max = max ? max : null;
  }
}
