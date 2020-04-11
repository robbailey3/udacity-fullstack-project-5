import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AgentsProfileComponent } from './agents-profile.component';

describe('AgentsProfileComponent', () => {
  let component: AgentsProfileComponent;
  let fixture: ComponentFixture<AgentsProfileComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AgentsProfileComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AgentsProfileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
