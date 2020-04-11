import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ActorsRootComponent } from './actors-root.component';

describe('ActorsRootComponent', () => {
  let component: ActorsRootComponent;
  let fixture: ComponentFixture<ActorsRootComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ActorsRootComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ActorsRootComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
