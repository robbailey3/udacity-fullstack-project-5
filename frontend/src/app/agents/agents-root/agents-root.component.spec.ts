import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AgentsRootComponent } from './agents-root.component';

describe('AgentsRootComponent', () => {
  let component: AgentsRootComponent;
  let fixture: ComponentFixture<AgentsRootComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AgentsRootComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AgentsRootComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
