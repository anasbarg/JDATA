import { Component, OnInit, Input } from "@angular/core";
import { Slider } from "../Types/Slider";

@Component({
  selector: "app-slider",
  templateUrl: "./slider.component.html",
  styleUrls: ["./slider.component.scss"]
})
export class SliderComponent implements OnInit {
  @Input("slider-config")
  sliderConfig: Slider;
  constructor() {}

  ngOnInit() {}
}
