import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { Notification } from './notification';

@Injectable({
  providedIn: 'root'
})
export class NotificationService {
  public notifications: Notification[] = [];
  public subject = new BehaviorSubject<Notification[]>(this.notifications);
  constructor() {}

  public addNotification(notification: Notification) {
    this.notifications.push(notification);
    this.subject.next(this.notifications);
  }
  public getNotifications() {
    return this.subject;
  }
  public clearNotifications() {
    this.notifications = [];
    this.subject.next(this.notifications);
  }
}
