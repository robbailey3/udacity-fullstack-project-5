import { Component, OnInit, Input } from '@angular/core';
import { Notification } from '../notification';

@Component({
  selector: 'app-notification',
  templateUrl: './notification.component.html',
  styleUrls: ['./notification.component.scss']
})
export class NotificationComponent implements OnInit {
  @Input() public notification: Notification;
  constructor() {}

  ngOnInit(): void {}
}
