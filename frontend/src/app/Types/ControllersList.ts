import { IController } from './IController';
import { Dropdown } from './Dropdown';
import { Slider } from './Slider';

export class ControllersList {
  constructor(
    public header_text: string = 'Input',
    public controllers_list: Array<Dropdown> = []
  ) {}
}
