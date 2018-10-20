import { Component, OnInit } from "@angular/core";

@Component({
  selector: "app-content",
  templateUrl: "./content.component.html",
  styleUrls: ["./content.component.scss"]
})
export class ContentComponent implements OnInit {
  arr: Array<Number> = [1, 2, 3, 4];
  constructor() {}

  ngOnInit() {}
}
