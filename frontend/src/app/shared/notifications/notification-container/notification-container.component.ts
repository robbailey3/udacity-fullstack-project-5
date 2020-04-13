import { Component, OnInit } from '@angular/core';
import { NotificationService } from '../notification.service';
import { Notification } from '../notification';

@Component({
  selector: 'app-notification-container',
  templateUrl: './notification-container.component.html',
  styleUrls: ['./notification-container.component.scss']
})
export class NotificationContainerComponent implements OnInit {
  public notifications: Notification[];
  constructor(private readonly notificationService: NotificationService) {}

  public ngOnInit(): void {
    this.subscribeToNotifications();
  }

  public subscribeToNotifications() {
    this.notificationService.getNotifications().subscribe({
      next: (response: Notification[]) => (this.notifications = response)
    });
  }
}
