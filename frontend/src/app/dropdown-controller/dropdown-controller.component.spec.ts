import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DropdownControllerComponent } from './dropdown-controller.component';

describe('DropdownControllerComponent', () => {
  let component: DropdownControllerComponent;
  let fixture: ComponentFixture<DropdownControllerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DropdownControllerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DropdownControllerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
