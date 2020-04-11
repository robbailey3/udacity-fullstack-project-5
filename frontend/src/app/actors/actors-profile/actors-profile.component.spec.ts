import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ActorsProfileComponent } from './actors-profile.component';

describe('ActorsProfileComponent', () => {
  let component: ActorsProfileComponent;
  let fixture: ComponentFixture<ActorsProfileComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ActorsProfileComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ActorsProfileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
