import { IController } from "./IController";

export class ControllersList {
  controllers_list: Array<IController>;

  constructor(
    public header_text?: string,
    ...controllers_list: Array<IController>
  ) {
    // Required Attribute
    this.controllers_list = controllers_list;
    // Optional Attribute
    this.header_text = header_text ? header_text : "Input";
  }
}
