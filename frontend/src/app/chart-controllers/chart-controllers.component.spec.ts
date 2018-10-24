import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ChartControllersComponent } from './chart-controllers.component';

describe('ChartControllersComponent', () => {
  let component: ChartControllersComponent;
  let fixture: ComponentFixture<ChartControllersComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ChartControllersComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ChartControllersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
