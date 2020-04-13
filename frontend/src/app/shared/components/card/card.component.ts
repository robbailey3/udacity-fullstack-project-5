import { Component, OnInit, Input, HostBinding } from '@angular/core';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss']
})
export class CardComponent implements OnInit {
  @Input() public headerImage: string;
  @Input() public cardTitle: string;
  @Input() public backgroundColor = '#fff';

  constructor() {}

  public ngOnInit(): void {}
}
