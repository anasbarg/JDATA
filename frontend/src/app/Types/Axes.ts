export class Axis {
  constructor(public scale_label: string, public label_color: string) {}
}

export class XAxis extends Axis {
  constructor(
    public scale_label: string = '',
    public label_color: string = 'rgb(104, 104, 104)',
    public type: string = 'category'
  ) {
    super(scale_label, label_color);
  }
}

export class YAxis extends Axis {
  constructor(
    public scale_label: string = '',
    public label_color: string = 'rgb(104, 104, 104)',
    public max?: Number | undefined,
    public min?: Number | undefined
  ) {
    super(scale_label, label_color);
  }
}
