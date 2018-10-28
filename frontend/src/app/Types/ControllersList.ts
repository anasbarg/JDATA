import { IController } from './IController';

export class ControllersList {
  controllers_list: Array<IController>;

  constructor(
    public header_text: string = 'Input',
    ...controllers_list: Array<IController>
  ) {
    // Required Attribute
    this.controllers_list = controllers_list;
  }
}
