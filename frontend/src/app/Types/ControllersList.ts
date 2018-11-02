import { IController } from './IController';

export class ControllersList {
  constructor(
    public header_text: string = 'Input',
    public controllers_list: Array<IController> = []
  ) {}
}
