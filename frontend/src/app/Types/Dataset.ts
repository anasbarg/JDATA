export class Dataset {
  constructor(
    public dataset_id: string,
    public label: string = '',
    public color: string = 'rgb(63, 81, 181)',
    public border_width: Number = 1.0,
    public fill: boolean = false,
    public tension: number = 1.0
  ) {}
}
