import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NotificationContainerComponent } from './notification-container/notification-container.component';
import { NotificationComponent } from './notification/notification.component';

@NgModule({
  declarations: [NotificationContainerComponent, NotificationComponent],
  exports: [NotificationContainerComponent, NotificationComponent],
  imports: [CommonModule]
})
export class NotificationsModule {}
