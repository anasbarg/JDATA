export class Dataset {
  dataset_id: string;
  label: string;
  color: string;
  border_width: Number;
  fill: boolean;
  tension: Number;

  constructor(
    dataset_id: string,
    label?: string,
    color?: string,
    border_width?: Number,
    fill?: boolean,
    tension?: Number
  ) {
    this.dataset_id = dataset_id;
    this.label = label ? label : "";
    this.color = color ? color : "rgb(63,81,181)";
    this.border_width = border_width ? border_width : 1.0;
    this.fill = fill ? fill : false;
    this.tension = tension ? tension : 1.0;
  }
}
