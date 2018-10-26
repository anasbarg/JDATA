export class Dataset {
  constructor(
    public dataset_id: string,
    public label?: string,
    public color?: string,
    public border_width?: Number,
    public fill?: boolean,
    public tension?: Number
  ) {
    this.dataset_id = dataset_id;
    this.label = label ? label : "";
    this.color = color ? color : "rgb(63,81,181)";
    this.border_width = border_width ? border_width : 1.0;
    this.fill = fill ? fill : false;
    this.tension = tension ? tension : 1.0;
  }
}
