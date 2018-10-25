import { Component, OnInit, Input } from "@angular/core";
import { Dropdown } from "../Types/Dropdown";

@Component({
  selector: "app-dropdown-controller",
  templateUrl: "./dropdown-controller.component.html",
  styleUrls: ["./dropdown-controller.component.scss"]
})
export class DropdownControllerComponent implements OnInit {
  @Input("dropdown-config")
  dropdownConfig: Dropdown;
  constructor() {}

  ngOnInit() {}

  is2Dropdowns() {
    return this.dropdownConfig.items && this.dropdownConfig.items2;
  }
}
